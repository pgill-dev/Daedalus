# Workflow Prompt: Engineering Plan

Use this workflow when the user asks Daedalus to design, build, deploy, migrate, secure, or improve infrastructure.

## Input

Infrastructure request:

```text
{{REQUEST}}
```

Known environment context:

```text
{{ENVIRONMENT_CONTEXT}}
```

## Required Output

Generate a complete engineering plan using the following structure:

# Engineering Plan: {{PROJECT_NAME}}

## 1. Requirement Interpretation

Restate what is being requested in engineering terms.

## 2. Assumptions and Constraints

List assumptions, missing information, and constraints.

## 3. Proposed Architecture

Describe the recommended architecture and major components.

## 4. Security Considerations

Identify authentication, authorization, network isolation, secrets, logging, patching, backup, and monitoring considerations.

## 5. Dependencies

List hardware, software, network, DNS, storage, certificate, and access dependencies.

## 6. Implementation Phases

Break the work into phases with clear deliverables.

## 7. Generated Artifacts

List files, templates, manifests, playbooks, runbooks, and docs that should be generated.

## 8. Validation Procedure

Provide a checklist to confirm the deployment or change works correctly.

## 9. Rollback Procedure

Provide steps to reverse the change safely.

## 10. Approval Gates

List required human approvals before execution.

## 11. Documentation Updates

List documentation that should be created or updated.

## 12. Project-Management Tasks

Generate ClickUp-style tasks with epics, tasks, subtasks, acceptance criteria, and priorities.
