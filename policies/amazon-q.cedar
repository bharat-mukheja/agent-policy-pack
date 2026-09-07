// Amazon Q VS Code wiper, July 2025.
//
// A pull request to the Amazon Q Developer extension repo was merged with
// write access, carrying a system prompt instructing the agent to wipe the
// machine and everything in the AWS account it could reach. Shipped in
// v1.84.0, installed 900,000+ times, reverted in v1.85.
//
// AWS's advisory (GHSA-7g7f-ff96-5gcw) put the root cause on an
// inappropriately scoped GitHub token in their CodeBuild configuration.
// Credential-scoping failure, not an AI-specific one — so the fix below is
// a scoping fix: gate the three destructive actions from this incident
// behind an approval claim.
//
// Two bugs this file had before it was tested, neither visible on read:
//   - Action::"S3:DeleteBucket" here vs "s3:DeleteBucket" in the caller —
//     Cedar is case-sensitive, so the forbid silently never matched.
//   - "ec2:TerminateInstance" in a test vs the real AWS action name
//     "ec2:TerminateInstances" here — same failure, different cause.
// Both allowed the exact call they were supposed to deny. Run every policy
// against real requests before trusting it.

permit(principal, action, resource);

forbid(principal, action == Action::"s3:DeleteBucket", resource)
unless { context has approval };
forbid(principal, action == Action::"iam:DeleteUser", resource)
unless { context has approval };
forbid (principal, action == Action::"ec2:TerminateInstances", resource)
unless { context has approval };