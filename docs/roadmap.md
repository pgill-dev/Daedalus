# Daedalus Roadmap

## Purpose

This roadmap tracks planned development for Daedalus.

Daedalus is being built in phases, starting with repository structure and engineering workflows before moving into tooling and interface development.

## Phase 1: Baseline Framework

Status: Complete

Goals:

- Establish repository structure
- Define mission and scope
- Create project memory
- Create baseline workflows
- Create templates and schemas
- Create operating manual
- Create end-to-end example

Completed:

- [x] Baseline repository
- [x] Project memory
- [x] Engineering request workflow
- [x] Engineering package output contract
- [x] Security review workflow
- [x] Validation and rollback workflow
- [x] IaC generation guardrails
- [x] ADR workflow
- [x] Operating manual
- [x] Project index
- [x] Workflow map
- [x] End-to-end example
- [x] Portfolio README and roadmap

## Phase 2: Local Tooling

Status: Planned

Goals:

- Add simple local tooling to generate artifacts from templates
- Add repository validation helpers
- Add schema validation
- Improve repeatability

Planned work:

- [ ] Create CLI skeleton
- [ ] Add command to create engineering request
- [ ] Add command to create engineering package
- [ ] Add command to create ADR
- [ ] Add command to create validation checklist
- [ ] Add command to create rollback plan
- [ ] Add command to validate schemas
- [ ] Add command to print workflow map
- [ ] Add basic tests

## Phase 3: Daedalus Web Interface

Status: Planned

Goals:

- Create a simple web interface for the Daedalus workflow
- Allow humans to submit requests and generate structured artifacts
- Keep approval gates visible

Planned work:

- [ ] Build basic web UI
- [ ] Add request intake form
- [ ] Add artifact preview
- [ ] Add approval status fields
- [ ] Add links to project memory
- [ ] Add export-to-Markdown support
- [ ] Add GitHub issue integration option

## Phase 4: Lab Integration

Status: Planned

Goals:

- Connect Daedalus artifacts to real lab workflows without autonomous execution
- Keep implementation manual or approval-gated

Planned work:

- [ ] Add Proxmox planning templates
- [ ] Add Cloudflare Tunnel planning templates
- [ ] Add Kubernetes service planning templates
- [ ] Add Ansible role proposal templates
- [ ] Add backup and restore package examples
- [ ] Add identity-aware access examples
- [ ] Add internal service deployment examples

## Phase 5: Security and Compliance Expansion

Status: Planned

Goals:

- Improve threat modeling and security review depth
- Add stronger validation and guardrail checks

Planned work:

- [ ] Add threat model examples
- [ ] Add abuse-case library
- [ ] Add Zero Trust checklist
- [ ] Add secrets handling checklist
- [ ] Add public exposure checklist
- [ ] Add backup safety checklist
- [ ] Add privileged automation checklist

## Phase 6: Portfolio Polish

Status: In Progress

Goals:

- Make the project understandable to engineers, recruiters, and future maintainers
- Show real engineering judgment and process

Planned work:

- [x] Portfolio summary
- [x] README refresh
- [ ] Add diagrams
- [ ] Add screenshots
- [ ] Add architecture overview
- [ ] Add demo workflow
- [ ] Add LinkedIn-ready project summary

## Future Ideas

Potential future additions:

- Local SQLite project memory index
- Static site documentation output
- GitHub Actions validation
- Markdown linting
- Schema linting
- Mermaid diagrams
- Request-to-package generator
- Human approval tracker
- Artifact status dashboard
- Integration with a local LLM
- Integration with a private Git server
- Integration with a lab web portal
