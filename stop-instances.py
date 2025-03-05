#stop ec2 instances

import boto3

#Create a python script that stops all running EC2 instances.
#Push your code to GitHub and include the link in your write up.

def lambda_handler(event, context):

    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
    ec2 = boto3.client('ec2')

    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
    #get all running instances
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]
            }
        ]
    )

    #get all instance IDs
    instance_ids = []
    # Loop through each reservation in the response
    for reservation in response['Reservations']:
        # Loop through each instance in the reservation
        for instance in reservation['Instances']:
            # Extract the Instance ID and add it to the list
            instance_ids.append(instance['InstanceId'])


    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html
    #stop the instances if they're running
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopping instances: {instance_ids}")
    else:
        print("No running instances found")