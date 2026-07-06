# Pull Request

## Summary

Briefly describe the change.

## Change Type

Select all that apply:

- [ ] Documentation
- [ ] Workflow
- [ ] Prompt
- [ ] Template
- [ ] Schema
- [ ] Example
- [ ] Script/tooling
- [ ] GitHub Action
- [ ] Project memory
- [ ] Other

## Related Issue or Request

Link the related issue, engineering request, ADR, or memory record.

```text
Closes #
Related:
```

## Affected Paths

List major files or directories changed.

```text
path/to/file
```

## Risk Level

Select one:

- [ ] Low — documentation or formatting only
- [ ] Medium — workflow/template/schema change
- [ ] High — affects generated engineering output, IaC, validation, rollback, or security review
- [ ] Critical — affects human approval gates, identity, access, secrets, backup, or public exposure guidance

## Human Approval Gate

Does this PR change human approval requirements?

- [ ] No
- [ ] Yes
- [ ] Unsure

If yes or unsure, explain.

## Security Impact

Select all that apply:

- [ ] No security impact
- [ ] Affects security review process
- [ ] Affects trust boundaries
- [ ] Affects identity or access control guidance
- [ ] Affects secrets handling
- [ ] Affects public exposure guidance
- [ ] Affects backup or recovery guidance
- [ ] Affects IaC safety guardrails

## Validation

Describe how this PR was validated.

- [ ] Repository validation script passes
- [ ] Markdown renders correctly
- [ ] JSON schemas are valid
- [ ] Links and paths are accurate
- [ ] Examples still align with workflows
- [ ] Not applicable

Validation notes:

```text

```

## Rollback

Describe how this change can be reverted if needed.

```text
Revert this PR or restore the previous version of affected files.
```

## Checklist

- [ ] Change is scoped and understandable
- [ ] Human approval model is preserved
- [ ] No plaintext secrets are included
- [ ] Validation guidance is preserved where applicable
- [ ] Rollback guidance is preserved where applicable
- [ ] Security implications are documented where applicable
- [ ] ADR impact was considered
- [ ] Project index was updated if needed
- [ ] Roadmap was updated if needed
- [ ] Repository validation passes

## Additional Notes

Add anything else reviewers should know.
