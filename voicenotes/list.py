import json
import os

from voicenotes import decimalencoder
from datetime import datetime
from math import floor
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    queryStringParams = event['queryStringParameters']
    startDate = None
    endDate = None
    if queryStringParams is not None:
        if 'startDate' in queryStringParams:
            startDate = queryStringParams['startDate']
        if 'endDate' in queryStringParams:
            endDate = queryStringParams['endDate']

    if startDate is not None:
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        startDate = floor(startDate.timestamp() * 1000)
    if endDate is not None:
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
        endDate = floor(endDate.timestamp() * 1000)
        ## do scan by enddate and startdate
    if startDate is not None and endDate is not None:
        # fetch all notes from the database
        result = table.scan(
            FilterExpression=Key('id').between(startDate, endDate)
        )
    else:
        result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
