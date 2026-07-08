# Workflow Prompt: Security Review

Use this workflow when reviewing a proposed architecture, deployment, service, or change for security risk.

## Input

Target system or change:

```text
{{TARGET}}
```

Known environment context:

```text
{{ENVIRONMENT_CONTEXT}}
```

## Required Output

# Security Review: {{TARGET}}

## 1. Scope

Define what is being reviewed.

## 2. Assets

List important systems, data, credentials, services, and dependencies.

## 3. Trust Boundaries

Identify user, service, network, identity, secret, and management boundaries.

## 4. Threats

Identify likely threats and abuse paths.

## 5. Risks

List risks with impact and likelihood.

## 6. Existing Controls

List controls already present or assumed.

## 7. Recommended Controls

Recommend hardening and monitoring improvements.

## 8. Validation Checklist

Provide checks that confirm security controls are working.

## 9. Residual Risk

Explain what risk remains after controls are applied.

## 10. Approval Notes

Identify anything that requires human decision before implementation.
