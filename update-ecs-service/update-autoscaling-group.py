import boto3
######### Enter All the variable values to run this scripts ##########
region = input("Enter your Region: ") # variables getting input from user
asg_name = input("Enter your AutoScaling Name: ")
asg_minhealthy_percentage = int(input("Enter your MinHealthyPercentage for asg update : "))
asg_instance_warmup = int(input("Enter your InstanceWarmup for asg update : "))
#################################################################################

client = boto3.client('autoscaling',region) # Initilizing boto3.client for Autoscaling service of AWS

### Using Boto3 predefined function to discribe a ASG for more info see : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_groups

response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        asg_name,
    ]
)
desired_capacity=response['AutoScalingGroups'][0]['DesiredCapacity']

print ("Current Running Instance Count is : ", desired_capacity)

### To Refresh Instance in ASG used predefined function please see : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling.Client.start_instance_refresh

response = client.start_instance_refresh(
    AutoScalingGroupName=asg_name,
    Strategy='Rolling',
    Preferences={
        'MinHealthyPercentage': asg_minhealthy_percentage,
        'InstanceWarmup': asg_instance_warmup,
    }
)
print(response['InstanceRefreshId'])