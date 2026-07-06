# IaC Package Output Contract

## Purpose

This output contract defines the required structure for Daedalus-generated Infrastructure as Code packages.

## Required Sections

Every IaC package must include:

- Metadata
- Summary
- Scope
- Assumptions
- Required variables
- Secrets handling
- Generated files
- Proposed file contents
- Safety notes
- Validation steps
- Rollback steps
- Human approval gate
- Follow-up actions

## Status Rules

IaC packages are `Proposed` by default.

IaC packages may only be marked `Approved` after human review.

## Safety Requirements

Generated IaC must:

- Avoid hard-coded secrets
- Avoid destructive defaults
- Prefer least privilege
- Prefer idempotent behavior
- Include validation
- Include rollback
- State assumptions
- State human approval requirements

## Forbidden Defaults

Daedalus must not generate defaults that:

- Expose services publicly without clear approval
- Grant broad administrative privileges without justification
- Disable authentication
- Disable authorization
- Disable logging
- Disable backups
- Store credentials in plaintext
- Delete data without explicit warning and approval
- Apply changes automatically

## Completion Criteria

A valid IaC package is complete when a human can review the proposed files, understand the risks, know how to validate the result, and know how to roll back safely.
