import boto3
import json
import base64
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="ap-south-1"):
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)

        if 'SecretString' in response:
            secret = response['SecretString']

            # Try parsing JSON
            try:
                return json.loads(secret)
            except json.JSONDecodeError:
                return secret  # return as plain string

        else:
            return base64.b64decode(response['SecretBinary'])

    except ClientError as e:
        print(f"Error: {e}")
        raise

print(get_secret("demo20260420065211386600000001"))