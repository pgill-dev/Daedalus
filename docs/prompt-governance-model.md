# Daedalus Prompt Governance Model

## Purpose

This document defines how Daedalus prompts are created, reviewed, versioned, tested, and maintained.

Daedalus prompts are not casual chatbot instructions. They are engineering control artifacts that shape how the platform reasons, documents, plans, validates, and prepares infrastructure work.

Prompt governance exists to prevent Daedalus from drifting into vague advice, autonomous behavior, unsafe recommendations, or inconsistent engineering outputs.

## Core Principle

Daedalus prompts must keep the system narrow.

Daedalus is an Infrastructure Security Engineering copilot.

It should focus on:

- Infrastructure architecture
- Security engineering
- Documentation
- Risk analysis
- Change management
- Automation planning
- Validation planning
- Rollback planning
- Engineering memory

It should avoid becoming:

- A general chatbot
- A creative writing assistant
- An autonomous infrastructure operator
- A secrets manager
- A replacement for human engineering review
- A tool that claims execution without approval

## Prompt Categories

Daedalus prompts are organized into three primary categories.

### 1. System Prompts

Location:

```text
prompts/system/
```

Purpose:

System prompts define the identity, boundaries, operating behavior, safety rules, and engineering responsibilities of Daedalus.

System prompts answer:

- What is Daedalus?
- What role does it perform?
- What is it allowed to do?
- What must it refuse or avoid?
- How should it structure reasoning outputs?
- How does it keep the human in the approval loop?

Examples:

```text
prompts/system/daedalus-system-prompt.md
```

### 2. Workflow Prompts

Location:

```text
prompts/workflows/
```

Purpose:

Workflow prompts define specific engineering workflows that Daedalus must support.

Workflow prompts answer:

- What task is being tested?
- What request should Daedalus handle?
- What outputs are required?
- What success criteria apply?
- What failure criteria apply?

Examples:

```text
prompts/workflows/vaultwarden-engineering-request.md
```

### 3. Output Contracts

Location:

```text
prompts/output-contracts/
```

Purpose:

Output contracts define the required structure of Daedalus responses.

Output contracts answer:

- What sections must every engineering package include?
- What format should Daedalus produce?
- What must be included before output is acceptable?
- What must not be omitted?

Examples:

```text
prompts/output-contracts/engineering-package-v1.md
```

## Prompt Change Rules

Prompt changes must be treated as engineering changes.

A prompt change may affect:

- Output quality
- Security recommendations
- Human approval boundaries
- Generated documentation
- Generated IaC skeletons
- Validation procedures
- Rollback procedures
- Project memory
- Future automation behavior

Because of this, prompt changes should not be made casually.

## Required Review Questions

Before changing a prompt, answer the following questions:

1. What problem does this prompt change solve?
2. Does the change keep Daedalus within its engineering role?
3. Does the change preserve the human approval boundary?
4. Does the change improve output quality or consistency?
5. Does the change introduce unsafe assumptions?
6. Does the change conflict with existing docs, ADRs, or output contracts?
7. Does the change require a new test case?
8. Does the change require an ADR?

## Prompt Versioning

Prompt versions should be tracked through Git commits.

Major prompt changes should be reflected in:

- Commit message
- Changelog entry, if applicable
- ADR, if the change affects architecture or governance
- Test plan update, if validation behavior changes

Recommended commit message format:

```text
Update <prompt-name> to <reason>
```

Examples:

```text
Update engineering package contract to require rollback impact analysis
Update system prompt to clarify read-only Phase I behavior
Add Wazuh deployment workflow prompt
```

## Prompt Review Levels

### Minor Prompt Change

A minor prompt change improves clarity without changing behavior.

Examples:

- Fixing wording
- Improving formatting
- Clarifying section names
- Correcting typos

Requirements:

- Git commit
- Local review

### Functional Prompt Change

A functional prompt change alters what Daedalus produces.

Examples:

- Adding a required output section
- Changing validation requirements
- Adding a new workflow
- Changing acceptance criteria

Requirements:

- Git commit
- Regenerate example output
- Review against validation checklist
- Update documentation if needed

### Governance Prompt Change

A governance prompt change affects authority, safety, approval, memory, or integration behavior.

Examples:

- Changing execution boundaries
- Allowing a new integration mode
- Changing what Daedalus may remember
- Changing approval-gate requirements
- Changing secret-handling rules

Requirements:

- Git commit
- ADR review
- Test plan review
- Human approval before acceptance

## Prompt Testing

Every meaningful prompt change should be tested against a known workflow.

For Phase I, the primary test workflow is:

```text
prompts/workflows/vaultwarden-engineering-request.md
```

The primary expected generated artifact is:

```text
examples/vaultwarden-engineering-package.md
```

Prompt changes should be evaluated against:

- `docs/phase-i-test-plan.md`
- `docs/phase-i-validation-checklist.md`
- `prompts/output-contracts/engineering-package-v1.md`
- `docs/change-management-model.md`
- `docs/integration-boundary-model.md`
- `docs/engineering-memory-model.md`

## Prompt Acceptance Criteria

A prompt is acceptable when it causes Daedalus to generate outputs that are:

- Specific
- Actionable
- Structured
- Security-aware
- Reviewable
- Aligned to output contracts
- Aligned to human approval boundaries
- Useful for Git documentation
- Useful for project task creation
- Clear about assumptions and constraints
- Clear about validation and rollback

## Prompt Failure Criteria

A prompt fails governance if it causes Daedalus to:

- Produce vague advice
- Skip validation
- Skip rollback planning
- Skip risk analysis
- Skip human approval gates
- Claim infrastructure was changed
- Generate secrets or credentials
- Assume access to systems it does not have
- Recommend unsafe defaults
- Ignore network segmentation
- Ignore TLS requirements where applicable
- Ignore backup and recovery requirements
- Drift into general chatbot behavior
- Generate outputs that cannot be reviewed

## Human Approval Boundary

Prompts must preserve the following boundary:

```text
Daedalus may plan, document, generate skeletons, validate, and recommend.
The engineer approves.
Execution requires explicit human approval.
```

No prompt may instruct Daedalus to automatically perform infrastructure changes in Phase I.

No prompt may instruct Daedalus to bypass human approval.

No prompt may instruct Daedalus to store or invent secrets.

## Secrets Handling

Prompts must never ask Daedalus to generate, store, or expose production secrets.

Daedalus may use placeholders such as:

```text
<VAULTWARDEN_ADMIN_TOKEN>
<TRAEFIK_TLS_SECRET>
<BACKUP_ENCRYPTION_KEY>
```

Daedalus must not generate real values for:

- Passwords
- Tokens
- Private keys
- API keys
- Recovery keys
- Encryption keys
- Production credentials

## Prompt Library Growth

New prompts should be added only when they support a defined engineering workflow.

Do not add prompts for random one-off conversations.

Each new workflow prompt should define:

- Purpose
- Test request
- Required output
- Success criteria
- Failure criteria
- Human approval boundaries

Recommended future workflow prompts:

```text
prompts/workflows/wazuh-engineering-request.md
prompts/workflows/traefik-ingress-engineering-request.md
prompts/workflows/proxmox-backup-engineering-request.md
prompts/workflows/kubernetes-service-engineering-request.md
prompts/workflows/rapid7-validation-engineering-request.md
```

## Relationship to ADRs

Prompt changes require ADRs when they alter the way Daedalus operates.

Examples that should trigger ADR review:

- Changing Daedalus from offline-only to read-only integration mode
- Allowing API-based inventory collection
- Changing execution boundaries
- Adding memory authority
- Adding new integration classes
- Changing output contract structure
- Changing approval-gate behavior

ADR location:

```text
docs/adr/
```

ADR operating model:

```text
docs/adr/adr-operating-model.md
```

## Relationship to Memory

Prompts may instruct Daedalus to reference reviewed memory artifacts.

Prompts must not treat unreviewed generated output as authoritative memory.

Prompt-generated memory candidates must remain reviewable before becoming accepted project memory.

Memory model:

```text
docs/engineering-memory-model.md
```

## Relationship to Integrations

Prompts must respect the integration maturity model.

For Phase I, prompts must assume:

- No live infrastructure access
- No API execution
- No automatic deployment
- No live inventory reads unless explicitly provided by the engineer
- Generate-only behavior

Integration boundary model:

```text
docs/integration-boundary-model.md
```

## Phase I Requirements

During Phase I, prompt governance requires:

- At least one system prompt
- At least one workflow prompt
- At least one output contract
- At least one generated example
- At least one validation checklist
- Clear human approval language
- Clear failure criteria
- No autonomous execution behavior

## Phase I Exit Criteria

Prompt governance is acceptable for Phase I when:

- The Vaultwarden workflow produces a complete engineering package
- Output structure matches the engineering package contract
- Generated output passes the Phase I validation checklist
- Human approval boundaries are preserved
- No secrets are generated
- No infrastructure execution is claimed
- Prompt changes can be reviewed through Git history

## Operating Summary

Daedalus prompts are engineering artifacts.

They must be:

- Versioned
- Reviewed
- Tested
- Scoped
- Security-aware
- Bound by human approval
- Aligned with architecture decisions

The quality of Daedalus depends on the quality of its prompts.
