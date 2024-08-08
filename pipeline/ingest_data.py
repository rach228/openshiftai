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

# retrieve the metadata of contents within the bucket
objects = s3.list_objects_v2(Bucket=bucket_name)

# output the name of each object within the bucket
for obj in objects["Contents"]:
    print(obj["Key"])

# Download the file "input.txt" from the specified S3 bucket and save it locally as "input.txt"
s3.download_file(bucket_name, "input.txt", "input.txt")

# Open the file "input.txt" for reading and write each line to "ingest_output.txt"
with open("ingest_output.txt", "w") as out:
    with open("input.txt", "r") as f:
        for line in f:
            print(line)
            out.write(line)
