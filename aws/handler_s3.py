import boto3
from decouple import config
import shutil

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACESS_KEY')
S3_BUCKET = config('S3_BUCKET')

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

s3 = boto3.resource('s3', 
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_bucket_s3(ilustracao, id):
    path = f"/tmp/{ilustracao.filename}"
    bucket_path = 'books/' + id + "/" + id +'_'+ ilustracao.filename

    with open(path, "wb+") as file_object:
        shutil.copyfileobj(ilustracao.file, file_object)

    client.upload_file(path, S3_BUCKET, bucket_path)

    return bucket_path

def delete_folder_s3(id): 
    bucket = s3.Bucket(S3_BUCKET)
    bucket.objects.filter(Prefix="books/"+ id).delete()
