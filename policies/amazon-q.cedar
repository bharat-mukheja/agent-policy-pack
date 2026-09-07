permit(principal, action, resource);

forbid(principal, action == Action::"s3:DeleteBucket", resource)
unless { context has approval };