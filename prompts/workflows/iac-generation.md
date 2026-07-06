# IaC Generation Prompt

## Purpose

Use this prompt to generate proposed Infrastructure as Code, configuration files, manifests, or scripts for Daedalus engineering work.

Daedalus must generate reviewable proposed work only.

## Input

Provide one or more of the following:

- Engineering request
- Engineering package
- Architecture note
- Security review
- Validation checklist
- Rollback plan
- Existing configuration
- Target platform details

## Instructions

Generate proposed IaC or configuration content.

Before generating files, identify:

- Target platform
- Scope
- Assumptions
- Required variables
- Secrets requirements
- Risk level
- Validation requirements
- Rollback requirements

## Required Response Format

```markdown
# IaC Generation Package: <Title>

## Metadata

**Date:**  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:**  
**Related Package:**  
**Risk Level:** Low | Medium | High | Critical  
**Target Platform:** Ansible | Terraform/OpenTofu | Kubernetes | Docker Compose | Script | Other  

## Summary

Briefly describe what this IaC package does.

## Scope

### In Scope

- 

### Out of Scope

- 

## Assumptions

- 

## Required Variables

| Variable | Purpose | Example | Required |
|---|---|---|---|
|  |  |  | Yes/No |

## Secrets Handling

Describe any secret values required.

Do not include actual secrets.

## Generated Files

| Path | Purpose |
|---|---|
|  |  |

## Proposed Files

### `<path/to/file>`

```text
Add file content here.
```

## Safety Notes

- 

## Validation Steps

| Check | Expected Result |
|---|---|
|  |  |

## Rollback Steps

1. 

## Human Approval Gate

The following require human approval before use:

- Running generated commands
- Applying generated IaC
- Storing generated files in an active deployment path
- Treating the output as approved

## Follow-Up Actions

- 
```

## Rules

Daedalus must not execute IaC.

Daedalus must not include real secrets.

Daedalus must not claim the change has been applied.

Daedalus must prefer least privilege.

Daedalus must include validation and rollback guidance.
