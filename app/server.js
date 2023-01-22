const express = require('express')
const app = express()
const cors = require('cors')
const pool = require('./src/db')
const { spawn } = require('child_process')

app.use(cors())
app.use(express.json())

app.post('/set-new-message', async (req, res) => {
  /* Get data from post request body, then upload to database*/
  try {
    const { message, sent_user_id, received_user_id } = req.body

    const new_message = await pool.query(
      `INSERT INTO chatdata(message, sentuserid, receiveduserid) VALUES
      ('${message}', ${sent_user_id}, ${received_user_id});`
    )
    res.json(new_message)
  } catch (err) {
    console.error(err)
  }
})

app.get('/get-response-message', async (req, res) => {
  /* Get user response from last message sent*/
  try {
    const cur_user_id = req.query['curuserid']
    const other_user_id = req.query['otheruserid']

    const messages = await pool.query(`SELECT * FROM chatdata WHERE
    sentuserid=${other_user_id} AND receiveduserid=${cur_user_id}
    ORDER BY time;`)
    let message = messages.rows.slice(-1)[0].message

    // message is last string, generate a response from it and return
    // classify_sentiment
    // recommendation generator
    let sentiment
    let response

    const sentiment_script = await spawn('python3', [
      'src/sentiment_classifier.py',
      message,
    ])

    sentiment_script.stdout.on('data', data => {
      sentiment = data.toString()
    })

    sentiment_script.on('close', async () => {
      const response_script = await spawn('python3', [
        'src/recommendation_generator.py',
        sentiment,
        message,
      ])

      response_script.stdout.on('data', data => {
        response = data.toString().slice(0, -2)
      })

      response_script.on('close', () => {
        res.json({ message, sentiment, response })
      })
    })
  } catch (err) {
    console.error(err)
  }
})

app.listen(5000, () => {
  console.log('Server has started on port 5000')
})
