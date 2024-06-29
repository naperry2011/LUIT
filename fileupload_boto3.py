# Importing the boto3 library, which is the AWS SDK for Python
import boto3

# Creating an S3 client object to interact with Amazon S3
s3 = boto3.client('s3')

# Opening the local file "test_text.txt" in read-binary mode ('rb')
with open("test_text.txt", 'rb') as f:
    s3.put_object(Bucket="nperry-boto3-06252024", Key="test_text.txt", Body=f, ContentType="text/plain")

# Uploading the file to S3 bucket "nperry-boto3-06252024"
    # Setting the key (name) of the object in S3 as "test_text.txt"
    # Using the file contents from 'f' as the Body of the S3 object
    # Setting the Content-Type of the object to "text/plain"


# s3.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
# s3.upload_file('test_text.txt', 'nperry-boto3-06252024', 'test_text_upload.txt', ExtraArgs={'ContentType': "text/plain"})