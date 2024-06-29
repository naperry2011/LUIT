import boto3

# Create an S3 client using boto3
s3 = boto3.client('s3')

# Create a new S3 bucket
response = s3.create_bucket(
    Bucket='nperry-boto3-06252024',  # Name of the S3 bucket to be created
)

# Print the response from creating the bucket
print(response)
