# Daedalus Architecture

## Overview

Daedalus is designed as a controlled engineering copilot for infrastructure planning and documentation. It converts engineering requests into repeatable, reviewable outputs.

The first version should prioritize structured reasoning and artifact generation before connecting to live systems.

## Conceptual Architecture

```text
User Request
    ↓
Daedalus System Prompt
    ↓
Workflow Prompt
    ↓
Output Contract
    ↓
Generated Engineering Package
    ↓
Human Review / Approval
    ↓
Optional Future Execution Layer
```

## Primary Components

### 1. Local LLM Runtime

Purpose:

- Run a local model through Ollama or a similar runtime.
- Keep sensitive lab context local where practical.
- Support iterative prompt testing.

Initial tools:

- Ollama
- Open WebUI
- Python
- VS Code

### 2. Prompt Library

Purpose:

- Store system prompts, workflow prompts, and output contracts as version-controlled files.
- Keep Daedalus narrow and engineering-focused.

Prompt categories:

- System identity
- Engineering planning
- Architecture generation
- Security review
- Change management
- Validation planning
- Rollback planning
- Documentation generation

### 3. Output Contracts

Purpose:

- Force predictable, reusable engineering responses.
- Prevent Daedalus from becoming a generic chatbot.

Expected output sections:

1. Requirement interpretation
2. Assumptions and constraints
3. Proposed architecture
4. Security considerations
5. Dependencies
6. Implementation phases
7. Generated artifacts
8. Validation procedure
9. Rollback procedure
10. Approval gates
11. Documentation updates
12. Project-management tasks

### 4. Templates

Purpose:

- Provide reusable scaffolds for infrastructure artifacts.

Template types:

- Ansible skeletons
- Kubernetes manifests
- Runbooks
- Threat models
- Change plans
- ADRs

### 5. Memory Layer

Purpose:

- Preserve architecture decisions, design rationale, inventory context, and lessons learned.

Phase I memory can be document-based.

Future memory options:

- Markdown knowledge base
- Vector database
- SQLite metadata store
- Git-backed engineering memory

### 6. Integration Layer

Purpose:

- Connect Daedalus to external systems in controlled phases.

Future integrations:

- ClickUp
- Gitea or GitHub
- Proxmox
- Kubernetes
- Proxmox Backup Server
- Rapid7
- CIS/STIG content

Initial access model:

- Phase I: no live integrations
- Phase II: project-management and Git integrations
- Phase III: read-only infrastructure inventory
- Phase VI: human-approved execution only

## Security Boundary

Daedalus must not store secrets directly. Secrets should remain in dedicated secret stores such as Vault, Kubernetes Secrets with encryption, SOPS, sealed-secrets, or another approved mechanism.

Daedalus should generate plans and templates, not expose passwords, tokens, or private keys.

## Approval Boundary

All generated changes must pass through human review before execution.

Approval artifacts should include:

- Change summary
- Risk assessment
- Validation plan
- Rollback plan
- Expected impact
- Required maintenance window, if any

## Phase I Target State

By the end of Phase I, Daedalus should produce a complete engineering package from one infrastructure request without live infrastructure access.
