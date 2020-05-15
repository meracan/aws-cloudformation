import json
import boto3

from meracanapi import Cognito

def handler(event, context):
    print(event,context)
    # Cognito
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }