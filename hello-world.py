#!/usr/bin/python3

def lambda_handler(event, lambda_context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "Hello world!"
    }

if __name__ == "__main__":
    lambda_handler('demo', 'run')





