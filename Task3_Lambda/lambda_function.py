
import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from AWS Lambda!",
            "internship": "Alfido Tech Cloud Computing Internship",
            "task": "Task 3 - Serverless Function",
            "status": "Success"
        })
    }

    return response
