import boto3
import pprint
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
# instancetype = ec2client.describe_instance_types()
# region = ec2client.describe_regions()
pp = pprint.PrettyPrinter(width=20, indent=4)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        pp.pprint(instance["InstanceId"])
        netlist = instance["NetworkInterfaces"]
        for net in netlist:
            if "Association" in net:
                pp.pprint((net["Association"])["PublicIp"])
            else:
                pp.pprint(net["PrivateIpAddress"])
            # pp.pprint(net["PrivateIpAddresses"][0])
        # pp.pprint(instance["Tags"]) ## Tags is List