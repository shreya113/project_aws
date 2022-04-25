import boto3

# 1. function to create instance 

def create_inst():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-04505e74c0741db8d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

    print(instances["Instances"][0]["InstanceId"])

# 2. function to terminate insatnce

def terminate_inst(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)
    
# 3. function to stop insatnce
    
def stop_inst(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)    
    
# 4. Sfunction to start instanec
    
def start_inst(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    print(response)      

# 5. list all instnaces 

def get_running_inst():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
    list1=[]
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            dict1={}
            dict1["instance_id"]= instance_id
            dict1["instance_type"]=instance_type
            dict1["public_ip"]=public_ip
            dict1["private_ip"]=private_ip
            list1.append(dict1)
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")    
    return list1