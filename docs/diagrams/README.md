# Daedalus Diagrams

## Purpose

This directory contains Mermaid diagrams that explain the Daedalus platform, repository structure, workflow model, human approval gates, and relationship to the Zero Trust lab.

These diagrams are intended to render directly in GitHub Markdown.

## Diagrams

| Diagram | Purpose |
|---|---|
| `daedalus-workflow.mmd` | Shows the end-to-end Daedalus engineering workflow |
| `repository-architecture.mmd` | Shows how the repository is organized |
| `human-in-the-loop-model.mmd` | Shows where human approval is required |
| `zero-trust-lab-relationship.mmd` | Shows the relationship between the lab and Daedalus |

## How to View

GitHub can render Mermaid diagrams inside Markdown files and Mermaid code blocks.

You can also copy the contents of a `.mmd` file into the Mermaid Live Editor or a local Markdown preview tool that supports Mermaid.

## Design Notes

Daedalus diagrams should emphasize:

- Proposed work versus approved work
- Human approval gates
- Security review
- Validation and rollback
- Project memory
- Architecture decision tracking
- The lab as the environment
- Daedalus as the engineering copilot

## Diagram Index

### End-to-End Workflow

```mermaid
flowchart TD
    A[Human Request] --> B[Engineering Request]
    B --> C[Readiness Review]
    C --> D{Ready?}
    D -- No --> E[Clarify Scope]
    E --> B
    D -- Yes --> F[Engineering Package]
    F --> G[Security Review]
    G --> H[Validation Checklist]
    H --> I[Rollback Plan]
    I --> J{Major Decision?}
    J -- Yes --> K[ADR]
    J -- No --> L[Human Review]
    K --> L
    L --> M{Approved?}
    M -- No --> N[Revise or Reject]
    N --> B
    M -- Yes --> O[Manual Implementation]
    O --> P[Validation Evidence]
    P --> Q[Memory Update]
```

### Repository Architecture

```mermaid
flowchart LR
    R[Daedalus Repository] --> D[docs]
    R --> M[memory]
    R --> P[prompts]
    R --> T[templates]
    R --> S[schemas]
    R --> E[examples]
    R --> G[.github]

    D --> DW[workflow docs]
    D --> OM[operating manual]
    D --> DI[diagrams]

    M --> MA[architecture]
    M --> MD[decisions]
    M --> MO[outputs]
    M --> MR[rollback]
    M --> MT[threat models]
    M --> MV[validation]

    P --> PW[workflow prompts]
    P --> PO[output contracts]
    P --> PS[system rules]

    T --> TE[engineering templates]
    T --> TI[IaC skeletons]

    S --> SJ[JSON schemas]

    E --> EE[end-to-end examples]

    G --> GI[issue templates]
    G --> GA[validation workflow]
```
