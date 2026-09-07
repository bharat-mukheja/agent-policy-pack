import cedarpy

policy = open("policies/amazon-q.cedar").read()

#S3
no_approval = {
    "principal": 'Agent::"amazon-q"',
    "action": 'Action::"s3:DeleteBucket"',
    "resource": 'Bucket::"cineflow-prod"',
    "context": {},
}
with_approval = dict(no_approval, context={"approval": True})
read_call = dict(no_approval, action='Action::"s3:GetObject"')

print("s3:\n")
print("delete, no approval  :", cedarpy.is_authorized(no_approval, policy, []).decision)
print("delete, with approval:", cedarpy.is_authorized(with_approval, policy, []).decision)
print("read, no approval     :", cedarpy.is_authorized(read_call, policy, []).decision)

#IAM
no_approval = {
    "principal": 'Agent::"amazon-q"',
    "action": 'Action::"iam:DeleteUser"',
    "resource": 'User::"cineflow-prod"',
    "context": {},
}
with_approval = dict(no_approval, context={"approval": True})
read_call = dict(no_approval, action='Action::"iam:GetUser"')

print("IAM:\n")
print("delete, no approval  :", cedarpy.is_authorized(no_approval, policy, []).decision)
print("delete, with approval:", cedarpy.is_authorized(with_approval, policy, []).decision)
print("read, no approval     :", cedarpy.is_authorized(read_call, policy, []).decision)

#EC2
no_approval = {
    "principal": 'Agent::"amazon-q"',
    "action": 'Action::"ec2:TerminateInstances"',
    "resource": 'Instance::"cineflow-prod"',
    "context": {},
}
with_approval = dict(no_approval, context={"approval": True})
read_call = dict(no_approval, action='Action::"ec2:GetInstance"')

print("EC2:\n")
print("delete, no approval  :", cedarpy.is_authorized(no_approval, policy, []).decision)
print("delete, with approval:", cedarpy.is_authorized(with_approval, policy, []).decision)
print("read, no approval     :", cedarpy.is_authorized(read_call, policy, []).decision)