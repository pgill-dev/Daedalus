## Phase I Usage

Daedalus Phase I focuses on generating structured engineering packages from controlled prompt contracts.

The current Phase I runner combines:

- The Daedalus system prompt
- A workflow-specific engineering request
- The engineering package output contract

It then produces a Markdown engineering package that can be reviewed, committed to Git, converted into project tasks, or used as an implementation planning baseline.

### Current Workflow

The current acceptance workflow is:

```text
Design a production-style Vaultwarden deployment for the Zero Trust Engineering Lab.
```

The workflow requires Daedalus to generate:

- Requirement interpretation
- Assumptions and constraints
- Proposed architecture
- Security considerations
- Threat model
- Implementation phases
- Repository structure
- Kubernetes manifest skeletons
- Ansible skeletons
- Validation checklist
- Rollback plan
- ClickUp-style task breakdown
- Architecture decision records
- Human approval gates

### Run the Phase I Engineering Package Generator

From the repository root:

```bash
python scripts/run_engineering_package.py
```

Expected output:

```text
examples/vaultwarden-engineering-package.md
```

### Review the Generated Package

Open the generated Markdown file:

```bash
cat examples/vaultwarden-engineering-package.md
```

Or open it in VS Code:

```bash
code examples/vaultwarden-engineering-package.md
```

### Commit Updated Output

If the generated package changes and the output is acceptable:

```bash
git status
git add examples/vaultwarden-engineering-package.md
git commit -m "Update Vaultwarden engineering package output"
git push
```

### Human Approval Boundary

The Phase I runner does not execute infrastructure changes.

Daedalus may generate:

- Plans
- Documentation
- Templates
- Skeleton manifests
- Validation steps
- Rollback plans
- Task structures

Daedalus may not:

- Deploy infrastructure
- Modify Proxmox
- Modify Kubernetes
- Change DNS
- Change firewall rules
- Create secrets
- Approve its own changes

The engineer remains responsible for review, approval, and execution.
