import boto3

s3 = boto3.resource("s3")

def show_bucket(s3):
        for bucket in s3.buckets.all():
         print("These are bucket present in AWS console: ", bucket)
show_bucket(s3)

#creating bucket in aws using python
def create_bucket(s3):
    s3.create_bucket(
        Bucket='mynewbucket-affu-12345',   # make sure this is unique
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )
    print("Bucket created successfully")

create_bucket(s3)

#backup lekar s3 par upload bhi krna h  