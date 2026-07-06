# CLI Example: Create ADR

## Goal

Create a proposed Architecture Decision Record for a major design decision.

Example decision:

```text
Use identity-aware access for internal documentation
```

## Command

```powershell
python -m daedalus.cli new-adr "Use identity-aware access for internal documentation"
```

## Expected Output

```text
Created ADR: memory/decisions/0003-use-identity-aware-access-for-internal-documentation.md
```

The exact ADR number depends on existing ADR files.

## Generated File Location

```text
memory/decisions/
```

## Next Steps

1. Open the generated ADR.
2. Complete the context, decision, options considered, rationale, and consequences.
3. Document security, validation, and rollback impacts.
4. Leave status as `Proposed` until reviewed.
5. Commit the proposed ADR.

## Commit Example

```powershell
git status
git add memory/decisions/
git commit -m "Add identity-aware access ADR"
git push origin main
git status
```

## Safety Notes

Daedalus may propose ADRs.

Daedalus must not mark an ADR as approved unless a human approves it.
