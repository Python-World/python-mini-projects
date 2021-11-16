import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'XXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
LOCAL_FILE = 'local_file_name'
BUCKET_NAME = 'bucket_name'
S3_FILE_NAME = 'file_name_on_s3'

def upload_to_s3(local_file, bucket, s3_file):
    ## This function is responsible for uploading the file into the S3 bucket using the specified credentials. 
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)