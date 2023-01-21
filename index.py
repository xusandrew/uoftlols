from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/set-new-message', methods=['POST'])
async def set_new_message():
    ''' 
    Get data from post request body, then upload to database
    '''

    message = request.form.get('message')
    sent_user = request.form.get('sent-user')
    received_user = request.form.get('received-user')

    # Upload to database


@app.route('/get-response-messages')
async def get_response_messages():
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
    responses = {}
    return jsonify(responses)


@app.route('/get-profile-stats')
async def get_response_messages():
    ''' 
    Get profile stats from database, 

    for ex:
        profile_data = {
            "Happy" : [],
            "Sad" : [],
            "Best Friends" : [],
            ...
        }

    and return JSON data for them
    '''

    # Which users, passed in the query string
    user = request.args.get("user")

    # Query db for data pertaining to only this user

    # Process data into responses

    profile_data = {}
    return jsonify(profile_data)


async def run_analysis():
    '''
    Based on current data in the database, generate responses
    and profile data 
    '''
    pass
