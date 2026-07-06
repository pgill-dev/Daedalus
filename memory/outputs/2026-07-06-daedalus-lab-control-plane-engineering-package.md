# Engineering Package: Daedalus Lab Control Plane MVP

## Package Metadata

**Package ID:** LAB-PKG-0001  
**Date:** 2026-07-06  
**Author:** Daedalus  
**Status:** Proposed  
**Related Request:** memory/plans/2026-07-06-daedalus-lab-control-plane-engineering-request.md  
**Related ADRs:** memory/decisions/0002-daedalus-control-plane-mvp.md  
**Related Memory Records:** memory/architecture/current-lab-context.md  
**Risk Level:** Medium  

## Request Summary

Define how Daedalus should be used as the engineering control plane for the self-hosted Zero Trust lab.

This package is process-oriented and does not authorize infrastructure changes.

## Scope

### In Scope

- Define Daedalus as the planning and documentation control plane
- Define where engineering artifacts are stored
- Define how lab engineering work enters the workflow
- Define approval boundaries
- Define validation and rollback record expectations
- Define security review triggers
- Create ADR for this control-plane model

### Out of Scope

- Deploying Daedalus as a web service
- Applying infrastructure changes
- Changing Proxmox, Cloudflare, Kubernetes, or Guacamole configuration
- Creating DNS records
- Creating public routes
- Managing secrets
- Automating live infrastructure execution

## Current State

### Confirmed Facts

- Daedalus is repository-based.
- Daedalus has a local CLI for generating proposed artifacts.
- Daedalus has validation scripts and CI.
- Daedalus has project memory directories.
- Daedalus uses proposed-by-default artifacts.
- Daedalus requires human approval for infrastructure-impacting work.

### Unknowns

- Whether Daedalus will later have a web interface
- Whether Daedalus will integrate with a private Git server
- Whether Daedalus will integrate with local LLM tooling
- Which lab service will be the first live implementation target
- Which approval method will be used long-term

## Desired Outcome

Daedalus becomes the standard entry point for lab engineering work.

All meaningful lab changes should begin as a request, become a proposed engineering package, receive security review when needed, include validation and rollback guidance, and update project memory after human review.

## Assumptions

- GitHub remains the primary repository for the current phase.
- The human engineer remains the final approval authority.
- Live lab changes are performed manually or through a future controlled process.
- Daedalus should remain useful even before a web UI exists.
- The local CLI is the first tooling layer for generating artifacts.

## Risks

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Daedalus becomes documentation-only | Platform may not influence real work | Medium | Use CLI and real lab packages |
| Approval gates become unclear | Proposed work could be mistaken for approved work | Low | Keep status fields and approval sections explicit |
| Project memory becomes stale | Future work may rely on outdated context | Medium | Update memory after major changes |
| Too much process slows progress | User may avoid workflow | Medium | Keep CLI generation simple |
| Sensitive lab details are over-documented | Exposure risk if repository visibility changes | Medium | Avoid secrets and avoid unnecessary sensitive detail |

## Proposed Engineering Plan

### Phase 1: Establish Control-Plane Rule

- Treat Daedalus as the starting point for meaningful lab engineering work.
- Use engineering requests for new work.
- Use engineering packages for proposed changes.
- Use ADRs for significant design decisions.
- Use validation and rollback records for infrastructure-impacting work.

### Phase 2: Use CLI for Artifact Creation

- Use `daedalus new-request` for new engineering requests.
- Use `daedalus new-package` for proposed engineering packages.
- Use `daedalus new-validation` for validation checklists.
- Use `daedalus new-rollback` for rollback plans.
- Use `daedalus new-adr` for decisions.

### Phase 3: Preserve Human Review

- Keep all generated artifacts as `Proposed`.
- Review artifacts manually before implementation.
- Do not treat CLI output as approved.
- Record approval status in the artifact.

### Phase 4: Update Project Memory

- Store plans in `memory/plans/`.
- Store generated packages in `memory/outputs/`.
- Store ADRs in `memory/decisions/`.
- Store security reviews in `memory/threat-models/`.
- Store validation records in `memory/validation/`.
- Store rollback records in `memory/rollback/`.

### Phase 5: Validate Repository Health

- Run repository validation before push.
- Run schema validation before push.
- Run pytest before push.
- Confirm GitHub Actions passes.

## Generated Artifacts

| Path | Purpose |
|---|---|
| `memory/plans/2026-07-06-daedalus-lab-control-plane-engineering-request.md` | Defines the request |
| `memory/outputs/2026-07-06-daedalus-lab-control-plane-engineering-package.md` | Defines the proposed package |
| `memory/threat-models/2026-07-06-daedalus-lab-control-plane-security-review.md` | Reviews risk |
| `memory/validation/2026-07-06-daedalus-lab-control-plane-validation-checklist.md` | Defines validation checks |
| `memory/rollback/2026-07-06-daedalus-lab-control-plane-rollback-plan.md` | Defines rollback for process adoption |
| `memory/decisions/0002-daedalus-control-plane-mvp.md` | Records the decision |

## Validation Checklist

| Check | Expected Result | Pass/Fail | Notes |
|---|---|---|---|
| Confirm package files exist | All package files are present | Not Tested | Human or CI validates |
| Confirm repo validation passes | `python scripts/validate_repo.py` passes | Not Tested | Human executes |
| Confirm schema validation passes | `python scripts/validate_schemas.py` passes | Not Tested | Human executes |
| Confirm tests pass | `python -m pytest` passes | Not Tested | Human executes |
| Confirm GitHub Actions passes | Green check on push | Not Tested | Human confirms |
| Confirm approval gates remain explicit | Artifacts state proposed status | Not Tested | Human reviews |

## Rollback Plan

### Rollback Trigger

Rollback should begin if this control-plane model creates confusion, breaks validation, weakens approval gates, or causes generated work to be treated as approved without review.

### Rollback Steps

1. Stop using the new package as authoritative.
2. Mark the ADR as rejected or superseded.
3. Revert the package commit if needed.
4. Restore prior operating documentation.
5. Preserve notes explaining why the model was rolled back.
6. Re-run validation and tests.

### Rollback Validation

- Repository validation passes.
- Schema validation passes.
- Tests pass.
- README and operating manual still describe the correct model.
- No proposed artifact is marked approved incorrectly.

## Threat Model Notes

### Assets

- Daedalus repository
- Project memory
- Generated engineering packages
- Lab architecture notes
- Human approval process
- GitHub Actions validation

### Trust Boundaries

- Human request to Daedalus-generated proposal
- Proposed artifact to approved artifact
- Repository documentation to live lab implementation
- Local CLI generation to committed repository state

### Threats

| Threat | Impact | Mitigation |
|---|---|---|
| Proposed output mistaken for approved work | Unsafe change may be applied | Explicit status and approval gates |
| Sensitive details committed | Lab exposure risk | Avoid secrets and minimize sensitive operational details |
| Broken CI ignored | Repository quality degrades | Require green CI before major milestones |
| Stale memory reused | Bad assumptions in future packages | Update memory after real changes |

## Human Approval Gate

Human approval is required before:

- Treating this package as the official lab operating model
- Using Daedalus artifacts for a live lab change
- Applying any future generated configuration
- Changing access, identity, backup, or exposure paths
- Marking any related artifact approved

## Completion Criteria

- [x] Scope is documented
- [x] Risks are documented
- [x] Security review is included
- [x] Validation checklist is included
- [x] Rollback plan is included
- [x] ADR is included
- [x] Human approval gate is identified
- [ ] CI passes after commit

## Follow-Up Actions

- Use Daedalus CLI for the next real lab request.
- Create a release checklist.
- Tag the first MVP milestone after Step 25.
