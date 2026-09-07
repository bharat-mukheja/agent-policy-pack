# agent-policy-pack

The SCP playbook rewritten for a subject whose action set isn't known until runtime.

Deterministic authorization for AI agent tool calls, evaluated outside the model, in Cedar.

## The pattern

Cedar denies everything by default. Every policy in this pack follows the same shape:

```cedar
permit(principal, action, resource);

forbid(principal, action == Action::"<some-action>", resource)
unless { context has approval };
```
`permit` is the baseline, without it there's nothing to carve an exception out of. Each `forbid` names one action that isn't allowed to run without an approval claim present in the request context.

## What's here

| File | Bounds | Actions |
| --- | --- | --- |
| `policies/amazon-q.cedar` | Amazon Q VS Code wiper, July 2025 | `s3:DeleteBucket`, `iam:DeleteUser`, `ec2:TerminateInstances` |

Grows as more policies are added.

## How this is tested

Every policy here is proven, not just reviewed, a script fires real requests at it and checks the decidions. A policy that references an action name off by one character (Wrong case, wrong plural) isn't a weaker rule, it's an absent one, and reading the file doesn't make that evident. Running the test will.

## The limit

Deterministic authorization bounds a hijacked agent. It doesn't prevent the hijack. The model can still be talked into forming a malicious goal and calling a tool toward it. What changes is what happens next; the call lands on a deny and an audit record instead of executing.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No Rust, no AWS account, no network calls at evaluation time.
