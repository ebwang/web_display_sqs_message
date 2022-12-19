import boto3
import json
import flask

# create the flask app 
app = flask.Flask(__name__)

# aws sqs credentials 

# get the url of the queue you wish to paginate
url = "https://sqs.us-west-2.amazonaws.com/055139393900/SQS_TESTE_WANG"

# set the initial page size
page_size = 10   
client = boto3.client('sqs')
# the service endpoint for retrieving messages from the queue
@app.route('/')
def index():
    return 'Index Page'

@app.route("/receive", methods=['GET'])
def get_messages():
  response = client.receive_message(
      QueueUrl=url,
      AttributeNames=[
          'SentTimestamp'
      ],
      MaxNumberOfMessages=1,
      MessageAttributeNames=[
          'All'
      ],
      VisibilityTimeout=0,
      WaitTimeSeconds=0
  )

  message = response['Messages'][0]
  receipt_handle = message['ReceiptHandle']
  return message

@app.route("/write", methods=['GET'])
def write_message():
    response = client.send_message(
      QueueUrl=url,
      DelaySeconds=10,
      MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
      },
      MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
      )
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)