import boto3

s3 = boto3.resource("s3")

def create_bucket(s3, bucket_name, region):
    s3.create_bucket(
        Bucket=bucket_name,   # make sure this is unique
        CreateBucketConfiguration={
            'LocationConstraint': region,
        },
    )
    print("Bucket created successfully")
#bucket_name = "backup-buket1235"
#region = 'eu-west-1'
#create_bucket(s3, bucket_name, region)

def upload_bucket(s3,file_name,bucket_name,key_name):  # s3 me ek file name jo ki ek bucket ke andar wo ek koi(key-name) name se create hojayegi
  #Upload a given file path to a given s3 bucket with a new name(key)
   
   data = open(file_name, 'rb') #files gets read in binary
   s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)  #Key---capital K in Key and B in Bucket
   print("Backup uplodaded successfully")

bucket_name = "backup-buket1235"
region = "eu-west-1"
file_name= "/Users/mehrunnisa/Documents/Linux/Pyhton/backups/bckup_2026-04-01.tar.gz.tar.gz"
upload_bucket(s3,file_name,bucket_name,"my-backup.tar.gz")  #function call

   #open ----is used to open the file
   #rb--- binary me ready krega
   #put_object--- object ko put krna h--mtlb kch data insert krna h
   # #file name copy path from backup folder of backup_2026_04_01 right click copy path
   #key name--jo hame name dena h wo


