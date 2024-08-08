import os
import boto3

# Retrieve credentials and endpoint from environment variables
key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
endpoint = os.getenv("AWS_S3_ENDPOINT")
bucket_name = os.getenv("AWS_S3_BUCKET")

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=key_id,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint,
    verify=False
)

# Printing the Environment Variables
print('environment')
print(os.environ)
print('-----')

# Listing Files in the Current Directory
print(os.listdir('.'))
print('-----')

# Reading from input_output.txt and Writing to enrich_output.txt
with open("enrich_output.txt", "w") as out:
    with open("ingest_output.txt", "r") as f:
        for line in f:
            print(line)
            out.write('enrich: ' + line)
