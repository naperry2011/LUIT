import boto3

# Create an S3 client using boto3
s3 = boto3.client('s3')

# Define our variables
bucket = 'nperry-boto3-06252024'  # Name of the S3 bucket
key = 'test_text_upload.txt'  # Key (filename) of the object we want to upload

# Set up public access configuration for the bucket
response = s3.put_public_access_block(
    Bucket=bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,  # Allow public ACLs
        'IgnorePublicAcls': False,  # Do not ignore public ACLs
        'BlockPublicPolicy': False,  # Allow public bucket policies
        'RestrictPublicBuckets': False  # Do not restrict public buckets
    },
)

# Set up bucket ownership controls
response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'  # Prefer bucket owner for object ownership
            },
        ]
    }
)

# Set the bucket ACL (Access Control List) to public-read
response = s3.put_bucket_acl(
    ACL='public-read',  # Allow public read access to the bucket
    Bucket=bucket,
)

# Set the object ACL to public-read
response = s3.put_object_acl(
    ACL='public-read',  # Allow public read access to the object
    Bucket=bucket,
    Key=key
)

# Print the response from setting the object ACL
print(response)
