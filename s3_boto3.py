import boto3

# Create an S3 client using boto3
s3 = boto3.client('s3')

# List all S3 buckets in the account
response = s3.list_buckets()

# Extract the list of buckets from the response
buckets = response['Buckets']

# Iterate through each bucket in the list
for bucket in buckets:
    # Print the name and creation date of each bucket
    print(bucket["Name"], bucket["CreationDate"])

# Print the entire response from the list_buckets operation
print(response)
