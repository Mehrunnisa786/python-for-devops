"""
This is a script to take backup from loca to AWS s3 bucket
boto3 --> used to do AWS tasks using python
"""
import boto3
"""
s3 = boto3.resource("s3")
def show_bucket(s3):
    for bucket in s3.bucket.all():
        print(bucket.name)

def  create_bucket(s3):
    s3.create_bucket(Bucket="python-for-devops-afrahhhhh", 
                     CreateBucketConfiguration={
                         'LocationConstraint': 'us-east-1',
                     },)
    print("bucket created successfully")

    create_bucket(s3)
    show_bucket(s3)
"""
#import boto3

s3 = boto3.resource("s3")

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(
        Bucket="python-for-devops-afrahhhhh"
    )
    print("Bucket created successfully")

# 👇 Call functions OUTSIDE
create_bucket(s3)
show_bucket(s3)