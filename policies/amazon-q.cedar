permit(principal, action, resource);

forbid(principal, action == Action::"s3:DeleteBucket", resource)
unless { context has approval };
forbid(principal, action == Action::"iam:DeleteUser", resource)
unless { context has approval };
forbid (principal, action == Action::"ec2:TerminateInstances", resource)
unless { context has approval };