import boto3    
import pprint
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
pp = pprint.PrettyPrinter(width=20, indent=4)

for reservation in response["Reservations"]:
    print(reservation)
    for instance in reservation["Instances"]:
        # pp.pprint(instance)
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]
        instance_pri_addr = instance["PrivateIpAddress"]
        instance_tags = instance["Tags"]
        print(instance_tags[0]["Value"])
        # instance_pub_addr = instance["PublicIpAddress"]
        print(instance_id)
        print(instance_type)
        print(instance_pri_addr)
        # print(instance_tags)
        # print(instance_pub_addr)
        # pp.pprint(instance_id + instance_type, + instance_pri_addr + instance_pub_addr)
