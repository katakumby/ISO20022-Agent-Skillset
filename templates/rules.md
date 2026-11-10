---
template: true
document_kind: rules
review_status: template
domain: "{{domain}}"
message_ids: []
message_set: "{{message_set_or_null}}"
source_ids: []
source_editions: []
---

# {{message_or_message_set}} — Rules

> TEMPLATE ONLY: preserve all source-backed rules, conditions, and exceptions. Do not invent business rules from schema structure.

## Business rules

| Rule ID / source label | Rule and exact condition | Applies to | Exceptions / qualifications | Source ID and precise locator |
| --- | --- | --- | --- | --- |

## Cross-field and process constraints

| Constraint / source label | Fields, roles, or events involved | Condition and expected behavior | Source ID and precise locator |
| --- | --- | --- | --- |

## Schema-enforced constraints

| Constraint | Schema location | Complete type / structure reference | Difference from business rule, if applicable |
| --- | --- | --- | --- |

Keep XSD validation distinct from MDR requirements and narrative recommendations. Preserve source wording where a paraphrase could weaken a condition.

## Conflicts and interpretation

{{Separate source facts from derived explanation. Record conflicting versions or ambiguous requirements with both source locators and issue links.}}

## Navigation and review

- Message / message-set index: {{index_link}}
- Structure reference: {{structure_link_or_inapplicable}}
- Coverage: {{coverage_link}}
- Source register / originals: {{source_links}}
- Review evidence: {{actual_checks_and_date}}
- Open issues: {{issue_links_or_reviewed_none}}

[Template guide](README.md)
