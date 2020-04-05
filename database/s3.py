import boto3

global session
session = boto3.session.Session()

def initialize_s3(app):

    session.client = boto3.client(
        's3',
        aws_access_key_id=app.config['S3']['accessKey'],
        aws_secret_access_key=app.config['S3']['sharedSecret'],
        endpoint_url=app.config['S3']['accessHost']
    )
    session.client.create_bucket(Bucket='devbucket0')


