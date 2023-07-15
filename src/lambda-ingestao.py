import boto3

# Listar objetos
s3 = boto3.client('s3')
response = s3.list_objects(
    Bucket='bkt-pod-academy-hackathon-data-eng'
)
print(response)