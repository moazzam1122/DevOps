import sys
import boto3
######### Enter All the variable values to run this scripts ##########
region = sys.argv[1]
cluster_name = sys.argv[2]
service_name = sys.argv[3]
#################################################################################

client = boto3.client('ecs',region) # Initilizing boto3.client for ECS service of AWS


### Using Boto3 predefined function to update ECS service for more info see :https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service
response = client.update_service(
    cluster=cluster_name,
    service=service_name,
    forceNewDeployment=True)

print (response)