const express = require('express')
const app = express()
const cors = require('cors')
const pool = require('./src/db')

app.use(cors())
app.use(express.json())

app.post('/set-new-message', async (req, res) => {
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

app.listen(5000, () => {
  console.log('Server has started on port 5000')
})
