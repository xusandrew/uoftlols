from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

api_key = "EST3529db50-91c5-4d65-8ea3-4b32c39c863dARY"

conn = psycopg2.connect(
    host="chatappdata.c1rgmh92t4a4.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432")

cur = conn.cursor()


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/set-new-message', methods=['POST'])
async def set_new_message():
    '''
    Get data from post request body, then upload to database
    Assumes names are fully typed out
    '''

    message = request.form.get('message')
    sent_user = request.form.get('sentuser')
    received_user = request.form.get('receivedsuser')

    # Testing code... can discard
    await cur.execute(
        f'SELECT * FROM users;')
    data = await cur.fetchall()
    return await jsonify(data)

    # Upload to database
    cur.execute(
        f"INSERT INTO chatdata (message, sentuserid, recieveduserid) VALUES ('{message}', {sent_user}, {received_user});")


@app.route('/get-response-messages')
async def get_response_messages():
    pass
    '''
    Get user responses from current conversation, with the emotion that each
    of the responses are. Query conversation from database and process the
    data in responses.

    for ex:
        responses = {
            "Happy" : [],
            "Sad" : [],
            ...
        }

    and return JSON data for them
    '''

    # Which users, passed in the query string
    cur_user = request.args.get("cur-user")
    other_user = request.args.get("other-user")

    # Query db for data pertaining to only this conversation

    # Process data into responses

    # Return
    # responses = {}
    # return jsonify(responses)


# @app.route('/get-profile-stats')
# async def get_response_messages():
#     pass
#     '''
#     Get profile stats from database,

#     for ex:
#         profile_data = {
#             "Happy" : [],
#             "Sad" : [],
#             "Best Friends" : [],
#             ...
#         }

#     and return JSON data for them
#     '''

#     # Which users, passed in the query string
#     user = request.args.get("user")

#     # Query db for data pertaining to only this user

#     # Process data into responses

#     # profile_data = {}
#     # return jsonify(profile_data)


# async def run_analysis():
#     '''
#     Based on current data in the database, generate responses
#     and profile data
#     '''
#     pass
