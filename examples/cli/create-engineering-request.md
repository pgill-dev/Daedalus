# CLI Example: Create Engineering Request

## Goal

Create a proposed engineering request for deploying an internal documentation service.

## Command

```powershell
python -m daedalus.cli new-request "Deploy internal documentation service"
```

## Expected Output

```text
Created engineering request: memory/plans/YYYY-MM-DD-deploy-internal-documentation-service-engineering-request.md
```

## Generated File Location

```text
memory/plans/
```

## Next Steps

1. Open the generated engineering request.
2. Fill in current state, desired outcome, constraints, and risk level.
3. Confirm the human approval acknowledgement.
4. Commit the proposed request.

## Commit Example

```powershell
git status
git add memory/plans/
git commit -m "Add internal docs service engineering request"
git push origin main
git status
```

## Safety Notes

This command only creates a Markdown file.

It does not deploy infrastructure, change access policies, create DNS records, or run commands.
