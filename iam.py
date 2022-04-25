import boto3

# Create an IAM user

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)            

# list all users

def list_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_users')
    list2=[]
    for response in paginator.paginate():
        for user in response["Users"]:
            dict2={}
            dict2["UserName"]=user['UserName']
            dict2["Arn"]=user['Arn']
            list2.append(dict2)
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")   
    return list2                 

# Delete IAM user

def delete_user(username):
    # Create IAM client
    iam = boto3.client('iam')

    # Delete a user
    response = iam.delete_user(
        UserName=username
    )
    print(response)
