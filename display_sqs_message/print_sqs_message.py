import boto3
import json
import flask

# create the flask app 
app = flask.Flask(__name__)

# aws sqs credentials 

# get the url of the queue you wish to paginate
url = "https://sqs.eu-west-2.amazonaws.com/account-id/queue-name"

# set the initial page size
page_size = 10   

# the service endpoint for retrieving messages from the queue
@app.route("/messages", methods=['GET'])
def get_messages():
   
    # retrieve the message using the sqs method receive messages 
    response = sqsClient.receive_message(
      QueueUrl=url,
      MaxNumberOfMessages=page_size
    )
   
    # response from sqs is json
    messages = response['Messages']

    # format of each message is as follows
    messages_formatted = []
    for message in messages:
        messages_formatted.append(json.loads(message['Body']))

    # return the response
    return json.dumps({'messages': messages_formatted})
