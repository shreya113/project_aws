import boto3
from flask import Flask, redirect, url_for, request, render_template
import instance
import iam
import s3bucket

app = Flask(__name__)

# DISPLAY HOME PAGE DEFAULT

@app.route('/')
def root():
    return render_template("index.html")

# EC2 INSTANCE SERVICES

# 1. Create An Ec2 Instance Service 

@app.route('/create_ec2')
def create_ec2():
    instance.create_inst()
    return render_template("index.html")

# 1. Terminate An Ec2 Instance Service by redirect to a terminate_ec2_form.html page

@app.route('/terminate_ec2')
def terminate_ec2():
    return render_template("terminate_ec2.html")

# Finally Terminated

@app.route('/terminated_ec2', methods=["POST"])
def terminated_ec2():
    if request.method == "POST":
        terminate_id = request.form["terminate_id"]
        instance.terminate_inst(terminate_id)
        return render_template("index.html")
# 1. Stop An Ec2 Instance Service by redirect to a stop_ec2_form.html page

@app.route('/stop_ec2')
def stop_ec2():
    return render_template("stop_ec2.html")

# Finally Stopped

@app.route('/stopped_ec2', methods=["POST"])
def stopped_ec2():
    if request.method == "POST":
        stop_id= request.form["stop_id"]
        instance.stop_inst(stop_id)
        return render_template("index.html")

# 1. Start An Ec2 Instance Service Again by redirect to a start_ec2_form.html

@app.route('/start_ec2')
def start_ec2():
    return render_template("start_ec2.html")

# Finally started Ec2 Instance Service basically it will start the instance again

@app.route('/started_ec2', methods=["POST"])
def started_ec2():
    if request.method == "POST":
        start_id= request.form["start_id"]
        instance.start_inst(start_id)
        return render_template("index.html")

# It is showing the all Ec2 Running Instances 

@app.route('/running_ec2')
def running_ec2():
    list1=instance.get_running_inst()
    return render_template("list_ec2.html",list1=list1)
    
    
# CREATE IAM SERVICES    

# 1. Create IAM User by redirect to the create_iam_userform.html 

@app.route('/create_iam_user')
def create_iam_user():
    return render_template("create_iam.html")

# Created IAM user successfully

@app.route('/created_iam_user', methods=["POST"])
def created_iam_user():
    if request.method == "POST":
        iamuser_id= request.form["iamuser_id"]
        iam.create_user(iamuser_id)
        return render_template("index.html") 

# 2. List all the IAM Users

@app.route('/listall_iam_users')
def listall_iam_users():
    list2=iam.list_users()
    return render_template("list_iam.html",list2=list2)

# 3. Delete the IAM User by redirecting to the delete_iam_userform.html() file

@app.route('/delete_iam_user')
def delete_iam_user():
    return render_template("delete_iam.html")

# Finally Terminated

@app.route('/deleted_iam_user', methods=["POST"])
def deleted_iam_user():
    if request.method == "POST":
        delete_iam_user_id = request.form["delete_iam_user_id"]
        iam.delete_user(delete_iam_user_id)
        return render_template("index.html")



# S3 BUCKET SERVICES ROUTES

# 1. CREATE A S3 BUCKET

@app.route('/create_bucket')
def create_s3_bucket():
    return render_template("create_bucket.html")

# Finally S3 Bucket Created

@app.route('/created_s3_bucket', methods=["POST"])
def created_s3_bucket():
    if request.method == "POST":
        s3bucket_id= request.form["s3bucket_id"]
        s3bucket.create_bucket(s3bucket_id)
        return render_template("index.html")

# 2. DELETE A S3 BUCKET

@app.route('/delete_s3_bucket')
def delete_s3_bucket():
    return render_template("delete_bucket.html")

# Finally S3 Bucket DELETED

@app.route('/deleted_s3_bucket', methods=["POST"])
def deleted_s3_bucket():
    if request.method == "POST":
        s3bucketdelete_id= request.form["s3bucketdelete_id"]
        s3bucket.delete_bucket(s3bucketdelete_id)
        return redirect(url_for("listbucket"))

@app.route('/listbucket')
def listbucket():
    list3=s3bucket.list_bucket()
    return render_template("list_bucket.html",list3=list3)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


