import cedarpy

policy = open("policies/test-policy.cedar").read()

no_approval = {
    "principal": 'Agent::"amazon-q"',
    "action": 'Action::"s3:DeleteBucket"',
    "resource": 'Bucket::"cineflow-prod"',
    "context": {},
}
with_approval = dict(no_approval, context={"approval": True})
read_call = dict(no_approval, action='Action::"s3:GetObject"')

print("delete, no approval  :", cedarpy.is_authorized(no_approval, policy, []).decision)
print("delete, with approval:", cedarpy.is_authorized(with_approval, policy, []).decision)
print("read, no approval     :", cedarpy.is_authorized(read_call, policy, []).decision)
