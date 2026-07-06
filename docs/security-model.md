# Daedalus Security Model

## Security Objective

Daedalus must assist infrastructure engineering without becoming an uncontrolled automation risk.

The core security principle is controlled generation with human approval.

## Trust Boundaries

### User Boundary

The engineer provides requirements and approves or rejects outputs.

### Model Boundary

The LLM can reason, plan, summarize, and generate artifacts. It should not be trusted to execute changes without review.

### Infrastructure Boundary

Infrastructure systems are external targets. During early phases, access should be read-only or unavailable.

### Secret Boundary

Daedalus must not directly store secrets, private keys, credentials, API tokens, or recovery codes.

## Access Model by Phase

| Phase | Access Level | Description |
|---|---|---|
| Phase I | No live access | Generates plans, docs, and templates only |
| Phase II | Limited API access | Creates project tasks and Git artifacts with user approval |
| Phase III | Read-only infrastructure access | Reads inventory, health, and status |
| Phase IV | Read-only memory access | Retrieves design rationale and engineering context |
| Phase V | Read-only security data | Uses scan findings and benchmark data for recommendations |
| Phase VI | Controlled execution | Executes only after explicit human approval |

## Prohibited Behaviors

Daedalus must not:

- Execute infrastructure changes automatically during Phase I
- Store raw secrets
- Generate destructive commands without warnings and rollback planning
- Bypass change approval
- Hide assumptions
- Present unvalidated outputs as production-ready
- Modify production systems without human approval

## Required Output Controls

Any proposed infrastructure change should include:

- Assumptions
- Dependencies
- Security impact
- Risk level
- Validation checklist
- Rollback plan
- Approval gate

## Human Approval Gate

Before any future execution action, Daedalus must produce:

1. Proposed change summary
2. Target systems
3. Expected impact
4. Validation plan
5. Rollback plan
6. Approval question

Execution should proceed only after explicit approval.

## Secret Handling

Daedalus may reference where secrets should be stored, but should not collect or display secret values.

Acceptable examples:

- `VAULTWARDEN_ADMIN_TOKEN` should be stored in the approved secret store.
- Kubernetes secrets should be encrypted at rest.
- SOPS or sealed-secrets may be used for GitOps workflows.

Unacceptable examples:

- Hardcoding passwords into generated manifests
- Storing API tokens in Markdown files
- Printing private keys into documentation

## Logging Considerations

Generated artifacts and prompts may contain sensitive architecture details. Repository visibility should be intentionally selected.

Recommended default:

- Private repository during development
- Public sanitized portfolio version later
