import sys, boto3

tag_key = sys.argv[1] if len(sys.argv) > 1 else input("Tag key: ")
tag_value = sys.argv[2] if len(sys.argv) > 2 else input("Tag value: ")

ec2 = boto3.client("ec2")

r = ec2.describe_instances(
    Filters=[{"Name": f"tag:{tag_key}", "Values": [tag_value]}]
)

for res in r["Reservations"]:
    for i in res["Instances"]:
        print(i.get("PrivateIpAddress"))
