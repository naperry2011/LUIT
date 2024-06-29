import boto3

# here we generate a presigned url given a client its method and arguments
s3=boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "nperry-boto3-06252024",'Key': "test_text_upload.txt"},ExpiresIn=300)


print(response)