import json

def lambda_handler(event, context):
    #1 Parse out query string params
    print(event)

    transactionId = event['queryStringParameters']['transactionId']

    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId = ' + transactionId)
    print('transactionType = ' + transactionType)
    print('transactionAmount = ' + str(transactionAmount))

    #2 Construct body of response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from lambda world'

    #3 Construct heep response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    #4 Return ResponseObject
    return responseObject
