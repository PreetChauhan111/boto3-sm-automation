import os
import sys
import json
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

def update_secret(secret_name, region_name="ap-south-1"):
    new_value = os.getenv("secret")

    if not new_value:
        raise ValueError("secret not found in .env file")

    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        try:
            json.loads(new_value)
        except:
            pass

        response = client.update_secret(
            SecretId=secret_name,
            SecretString=new_value
        )

        return response

    except ClientError as e:
        print(f"Error updating secret: {e}")
        raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Please provide secret_name as argument")

    secret_name = sys.argv[1]

    print("Updating secret:", secret_name)
    update_secret(secret_name)
    
# update_secret("demo20260420065211386600000001")