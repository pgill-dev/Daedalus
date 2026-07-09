# Local Ollama Setup for Daedalus

## Purpose

This document describes how to configure a local Ollama runtime for Daedalus Phase I.

Daedalus uses a local LLM as a reasoning engine. The LLM does not define Daedalus by itself. Daedalus is the engineering control layer that provides prompts, workflows, output contracts, validation expectations, approval gates, memory rules, and documentation structure.

Phase I uses Ollama only to generate Markdown engineering packages. It does not execute infrastructure changes.

## Operating Model

```text
Daedalus repository
    ↓
System prompt + workflow contract + output contract
    ↓
Local Ollama model
    ↓
Generated Markdown engineering package
    ↓
Human review and Git-based approval
```

## Phase I Boundary

During Phase I, Ollama is allowed to:

- Receive assembled engineering prompts from the Daedalus runner.
- Generate Markdown engineering packages.
- Generate architecture plans, task breakdowns, validation checklists, rollback plans, and ADR recommendations.
- Assist with documentation and automation planning.

During Phase I, Ollama must not:

- Execute infrastructure commands.
- Modify Proxmox, Kubernetes, PBS, Rapid7, ClickUp, GitHub, Gitea, DNS, firewall, or production systems.
- Store secrets.
- Generate production credentials.
- Claim changes were deployed.
- Bypass human approval.

## Windows 11 Labadmin VM Setup

Daedalus is currently being developed from the Windows 11 labadmin VM.

Install Ollama from the official installer, then confirm it is available from PowerShell:

```powershell
ollama --version
```

Confirm the Ollama service is responding:

```powershell
ollama list
```

If Ollama is installed correctly but no models are present, the list may be empty. That is expected before pulling a model.

## Recommended Phase I Models

Start with one general-purpose model and one code-focused model.

Recommended starting point:

```powershell
ollama pull llama3.1:8b
```

Optional code-focused model:

```powershell
ollama pull qwen2.5-coder:7b
```

The first Phase I runner should default to the general-purpose model unless a specific workflow requires a code-focused model.

## Basic Ollama Test

Run a simple generation test:

```powershell
ollama run llama3.1:8b
```

Test prompt:

```text
You are Daedalus, an Infrastructure Security Engineer. In one paragraph, explain why Phase I should generate Markdown engineering packages instead of executing infrastructure changes.
```

Expected behavior:

- The model responds locally.
- The response does not require internet access.
- The response aligns with human approval and generate-only Phase I behavior.

Exit the interactive session with:

```text
/bye
```

## API Test

Ollama exposes a local API by default at:

```text
http://localhost:11434
```

A later Daedalus runner should call:

```text
http://localhost:11434/api/generate
```

PowerShell API smoke test:

```powershell
$body = @{
  model = "llama3.1:8b"
  prompt = "Return the text: Daedalus local Ollama API test successful."
  stream = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body $body -ContentType "application/json"
```

Expected behavior:

- The request returns a response object.
- The `response` field contains model output.
- No external API key is required.

## Python Dependency Notes

The Daedalus runner may need Python dependencies such as:

```text
pyyaml
requests
```

Install manually during early development:

```powershell
python -m pip install pyyaml requests
```

The project should eventually track these dependencies in `pyproject.toml`.

## Configuration Relationship

The local Ollama runner should read from:

```text
config/daedalus.local.example.yml
```

A user-specific local copy may later be created as:

```text
config/daedalus.local.yml
```

The real local config should not store secrets. If future integrations require tokens, those values should be provided through environment variables or an external secret manager, not committed to Git.

## Expected Phase I Runner Behavior

The future Ollama runner should:

1. Load the Daedalus local configuration.
2. Load the system prompt.
3. Load the selected workflow contract.
4. Load the engineering package output contract.
5. Assemble a controlled prompt.
6. Send the prompt to Ollama.
7. Save the generated Markdown package to the configured output directory.
8. Print the generated output path.
9. Require human review before any output is treated as approved.

## First Acceptance Test

The first semi-working Daedalus test should be:

```powershell
python scripts\run_ollama_engineering_package.py --workflow vaultwarden
```

Expected output path:

```text
memory/outputs/vaultwarden-engineering-package-YYYYMMDD-HHMM.md
```

The generated package should include:

- Requirement interpretation
- Assumptions
- Constraints
- Proposed architecture
- Security considerations
- Threat model
- Implementation phases
- Repository structure
- Kubernetes skeletons
- Ansible skeletons
- Validation checklist
- Rollback plan
- ClickUp-style task breakdown
- ADR recommendations
- Human approval gates

## Troubleshooting

### Ollama command is not found

Restart PowerShell after installation. If it still fails, confirm Ollama was installed correctly and added to the user path.

### Model is not found

Pull the model again:

```powershell
ollama pull llama3.1:8b
```

### API does not respond

Confirm Ollama is running:

```powershell
ollama list
```

Then retry the API smoke test.

### Python cannot import yaml

Install PyYAML:

```powershell
python -m pip install pyyaml
```

### Python cannot import requests

Install Requests:

```powershell
python -m pip install requests
```

## Phase I Exit Criteria

Local Ollama setup is considered successful when:

- Ollama is installed on the labadmin VM or selected local host.
- At least one approved model is available locally.
- The Ollama API responds at `http://localhost:11434`.
- The Daedalus runner can send a prompt to Ollama.
- Daedalus can save a generated Markdown engineering package.
- The generated package is reviewed against the Phase I validation checklist.

## Design Rationale

Using Ollama supports the Daedalus local-first design goal. It allows the project to demonstrate AI-assisted engineering without requiring an external API dependency for Phase I.

This reinforces the core Daedalus story:

```text
Daedalus is a local-first, Git-first, Markdown-first infrastructure engineering copilot.
It generates engineering artifacts for human review before any infrastructure execution is allowed.
```
