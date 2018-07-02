import os
import json

from voicenotes import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # print('type(event['pathParameters']['id']): ', type(event['pathParameters']['id']))
    # print('event['pathParameters']['id']: ', event['pathParameters']['id'])
    # fetch a note from the database
    result = table.get_item(
        Key={
            'id': int(event['pathParameters']['id'])
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
