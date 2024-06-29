import boto3

s3 = boto3.client('s3')
response = s3.create_bucket(
    Bucket='nperry-boto3-06292024',
    
)

print(response)