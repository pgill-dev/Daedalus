# Phase I Operating Workflow

## Purpose

This document defines the Phase I operating workflow for Daedalus.

The goal is to describe how an engineering request moves through Daedalus from initial prompt to reviewable engineering package while preserving the core operating boundary:

> Daedalus plans.  
> The engineer reviews.  
> Execution requires explicit human approval.

Phase I does not connect to live infrastructure systems. It is focused on repeatable reasoning, structured output, documentation quality, validation planning, rollback planning, and engineering decision capture.

## Workflow Summary

The Phase I workflow follows this path:

```text
User Engineering Request
        ↓
Daedalus System Prompt
        ↓
Workflow Contract
        ↓
Output Contract
        ↓
Local Runner
        ↓
Generated Engineering Package
        ↓
Human Review
        ↓
Validation Checklist
        ↓
ADR / Memory / Task Recommendations
        ↓
Approved Planning Baseline
```

## Operating Modes

Phase I supports only the following modes:

| Mode | Description | Allowed in Phase I |
|---|---|---|
| Plan | Produce architecture, risks, tasks, validation, and rollback | Yes |
| Generate | Produce documentation and code skeletons | Yes |
| Review | Compare output against contracts and checklists | Yes |
| Remember | Recommend memory and ADR entries for human approval | Yes |
| Execute | Apply infrastructure changes | No |
| Modify Live Systems | Change Proxmox, Kubernetes, DNS, firewall, secrets, or storage | No |

## Step 1 — Receive Engineering Request

The workflow begins with a bounded infrastructure request.

Example:

```text
Design a production-style Vaultwarden deployment for my self-hosted Zero Trust Engineering Lab.

Use Kubernetes, Traefik, persistent storage, encrypted backups, monitoring, restricted administrative access, and human-approved deployment.
```

The request should describe:

- The target service or platform
- The deployment environment
- Required technologies
- Security expectations
- Operational constraints
- Human approval requirements

## Step 2 — Apply Daedalus System Prompt

The system prompt constrains Daedalus to act as an Infrastructure Security Engineer rather than a general-purpose chatbot.

Daedalus should focus on:

- Infrastructure architecture
- Security engineering
- Risk analysis
- Change management
- Documentation
- Automation planning
- Validation
- Rollback
- Engineering memory

Daedalus should avoid:

- General conversation
- Unsupported assumptions
- Creative filler
- Autonomous action claims
- Live system modification
- Secret generation
- Unreviewed production guidance

## Step 3 — Apply Workflow Contract

The workflow contract defines the specific engineering scenario being tested.

For Phase I, the primary acceptance workflow is:

```text
prompts/workflows/vaultwarden-engineering-request.md
```

This workflow defines:

- The test request
- Required output sections
- Engineering standards
- Non-goals
- Human approval model
- Pass criteria
- Failure criteria

A generated package must satisfy the workflow contract before it can be considered a valid Phase I output.

## Step 4 — Apply Output Contract

The output contract defines the required structure of the generated engineering package.

Primary contract:

```text
prompts/output-contracts/engineering-package-v1.md
```

The output contract ensures every generated package includes:

- Requirement interpretation
- Assumptions
- Constraints
- Proposed architecture
- Security considerations
- Threat model
- Implementation phases
- Repository structure
- Infrastructure-as-Code skeletons
- Validation checklist
- Rollback plan
- Task breakdown
- ADR recommendations
- Human approval gates

This prevents Daedalus from producing vague advice or unstructured responses.

## Step 5 — Run Local Generator

The Phase I runner is responsible for combining prompt inputs and producing a Markdown engineering package.

Primary runner:

```text
scripts/run_engineering_package.py
```

Expected command:

```powershell
python scripts\run_engineering_package.py
```

Expected generated artifact:

```text
examples/vaultwarden-engineering-package.md
```

The runner should not:

- Connect to Proxmox
- Connect to Kubernetes
- Connect to PBS
- Connect to Rapid7
- Connect to ClickUp
- Connect to GitHub APIs
- Execute Ansible
- Apply Kubernetes manifests
- Modify secrets
- Modify DNS
- Modify firewall rules

The runner is a local generation tool only.

## Step 6 — Review Generated Engineering Package

After generation, the human engineer reviews the output.

Review should confirm:

- The request was interpreted correctly
- Assumptions are clearly labeled
- Risks are not hidden
- Security considerations are specific
- Validation is testable
- Rollback is realistic
- Tasks are actionable
- ADR recommendations are appropriate
- No live execution is implied
- No credentials or secrets were generated

The generated package should be treated as a draft engineering artifact, not as approved implementation guidance.

## Step 7 — Apply Validation Checklist

The generated package must be checked against:

```text
docs/phase-i-validation-checklist.md
```

Validation should include:

- Repository state checks
- Runner execution checks
- Output contract checks
- Security checks
- Human approval gate checks
- Rollback quality checks
- ADR quality checks
- Memory readiness checks

A package should not be considered acceptable if it skips rollback, validation, approval gates, or security review.

## Step 8 — Identify ADR Candidates

Daedalus should recommend ADRs when the generated output includes decisions such as:

- Deployment platform selection
- Ingress approach
- Storage design
- Backup design
- Secrets handling
- Network segmentation
- Monitoring approach
- Human approval boundary
- Integration mode

ADR recommendations should follow:

```text
docs/adr/adr-operating-model.md
```

ADR recommendations are not automatically accepted. They require human review before becoming authoritative project memory.

## Step 9 — Identify Memory Candidates

Daedalus may recommend engineering memory entries when the generated package establishes durable project context.

Examples:

- Why a VLAN is isolated
- Why an integration remains read-only
- Why a service is deployed on Kubernetes instead of a VM
- Why a backup strategy was selected
- Why human approval is required before execution

Memory recommendations must follow:

```text
docs/engineering-memory-model.md
```

Daedalus must not store:

- Secrets
- Passwords
- API tokens
- Private keys
- Recovery codes
- Sensitive credentials
- Unreviewed assumptions as facts

## Step 10 — Generate Task Recommendations

The generated package should include task recommendations suitable for future project management tooling.

Phase I may generate task structures, but it must not push tasks into ClickUp automatically.

Task recommendations should include:

- Epic name
- Milestones
- Implementation tasks
- Validation tasks
- Documentation tasks
- Security review tasks
- Rollback preparation tasks
- Approval gates

Future ClickUp integration must follow:

```text
docs/integration-boundary-model.md
```

## Step 11 — Establish Planning Baseline

A generated package becomes a planning baseline only after human review.

A planning baseline means:

- The output is acceptable for further design work
- Risks and assumptions are visible
- Approval gates are documented
- Validation and rollback exist
- ADR and memory candidates are identified
- No execution has occurred

A planning baseline does not mean:

- The system has been deployed
- The design is production ready
- The generated code is final
- Security review is complete
- The engineer has approved execution

## Human Approval Gates

Phase I requires approval before any movement from planning into execution.

Required approval gates:

| Gate | Required Before |
|---|---|
| Architecture Approval | Treating design as implementation baseline |
| Security Approval | Accepting threat model and control assumptions |
| Change Approval | Applying changes to infrastructure |
| Secret Approval | Creating or referencing real secrets |
| Execution Approval | Running automation or applying manifests |
| Rollback Approval | Confirming recovery procedure is usable |

In Phase I, these gates are documented only. They are not automated enforcement mechanisms yet.

## Failure Conditions

The Phase I operating workflow fails if Daedalus:

- Produces vague guidance instead of structured output
- Skips required output contract sections
- Claims it deployed or changed infrastructure
- Generates real credentials
- Stores secrets
- Recommends exposing services without TLS
- Ignores rollback planning
- Ignores validation planning
- Treats assumptions as facts
- Creates unreviewed memory as authoritative
- Pushes tasks or code to external systems automatically
- Suggests bypassing human approval

## Success Criteria

The Phase I operating workflow succeeds when Daedalus can consistently:

- Accept a bounded engineering request
- Produce a complete engineering package
- Follow the output contract
- Include specific security analysis
- Include validation and rollback plans
- Recommend ADRs and memory entries
- Generate task breakdowns
- Preserve human approval boundaries
- Avoid live system execution
- Produce reviewable Markdown suitable for Git

## Phase I Exit Criteria

Phase I is complete when the following are true:

- The Vaultwarden workflow can be run repeatedly
- The output follows the engineering package contract
- The generated package passes the Phase I validation checklist
- The package includes realistic security, validation, and rollback content
- ADR recommendations are clear and reviewable
- Memory recommendations follow the memory model
- No live infrastructure access is required
- The process is documented well enough for another engineer to reproduce

## Related Files

```text
prompts/system/daedalus-system-prompt.md
prompts/workflows/vaultwarden-engineering-request.md
prompts/output-contracts/engineering-package-v1.md
scripts/run_engineering_package.py
examples/vaultwarden-engineering-package.md
docs/phase-i-execution-plan.md
docs/phase-i-test-plan.md
docs/phase-i-validation-checklist.md
docs/change-management-model.md
docs/engineering-memory-model.md
docs/integration-boundary-model.md
docs/prompt-governance-model.md
docs/adr/adr-operating-model.md
```

## Operating Principle

Daedalus is useful only if it improves engineering discipline.

The system should not be judged by whether it sounds intelligent. It should be judged by whether it produces better engineering artifacts:

- Better plans
- Better documentation
- Better risk visibility
- Better validation
- Better rollback
- Better task structure
- Better memory
- Better decision traceability

Phase I proves the reasoning workflow before any live integration is added.
