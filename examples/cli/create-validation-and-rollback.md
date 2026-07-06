# CLI Example: Create Validation and Rollback Artifacts

## Goal

Create proposed validation and rollback artifacts for an engineering package.

Example target:

```text
Deploy internal documentation service
```

## Commands

```powershell
python -m daedalus.cli new-validation "Deploy internal documentation service"
python -m daedalus.cli new-rollback "Deploy internal documentation service"
```

## Expected Output

```text
Created validation checklist: memory/validation/YYYY-MM-DD-deploy-internal-documentation-service-validation-checklist.md
Created rollback plan: memory/rollback/YYYY-MM-DD-deploy-internal-documentation-service-rollback-plan.md
```

## Generated File Locations

```text
memory/validation/
memory/rollback/
```

## Next Steps

1. Open the generated validation checklist.
2. Fill in pre-change, post-change, negative, and rollback validation.
3. Open the generated rollback plan.
4. Fill in rollback trigger, known-good state, rollback steps, validation, and escalation.
5. Commit the proposed artifacts.

## Commit Example

```powershell
git status
git add memory/validation/ memory/rollback/
git commit -m "Add internal docs validation and rollback plans"
git push origin main
git status
```

## Safety Notes

The CLI does not run validation commands.

The CLI does not execute rollback steps.

Human confirmation is required before validation or rollback is considered complete.
