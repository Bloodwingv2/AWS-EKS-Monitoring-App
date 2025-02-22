import boto3

ecr_client = boto3.client('ecr')

repository_name = 'my-cloud-native'
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)