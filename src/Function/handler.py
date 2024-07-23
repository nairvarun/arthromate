import os
import json
import boto3
from random import randint

def handler(event, context):
    print(999, event, context)
    dynamodb = boto3.resource('dynamodb')
    t = os.environ['TABLE_TABLE_NAME']
    table = dynamodb.Table(t)
    table.put_item(
        Item={
            'id': str(randint(0, 100)),
            'n': randint(0, 1000),
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
