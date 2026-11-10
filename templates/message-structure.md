---
template: true
document_kind: message-structure
review_status: template
domain: "{{domain}}"
business_area: "{{business_area}}"
message_id: "{{full_message_id}}"
source_ids: []
source_editions: []
namespace: "{{target_namespace}}"
---

# {{full_message_id}} — Schema structure

> TEMPLATE ONLY: populate from supplied XSDs. This page is not a complete schema reference until the declaration/type inventory and dependencies are reconciled.

## Schema identity and roots

| Item | Value | Source ID and schema locator |
| --- | --- | --- |
| Target namespace | {{target_namespace}} | {{locator}} |
| Schema language/version cues | {{schema_version_evidence}} | {{locator}} |
| Declared document root(s) | {{declared_roots}} | {{locator}} |
| Payload element and type | {{payload_declaration}} | {{locator}} |
| Element / attribute form defaults | {{form_defaults}} | {{locator}} |

## Supplied schema dependencies

| Source ID | Import / include / other relationship | Namespace and schema location | Resolution | Issue / canonical reference |
| --- | --- | --- | --- | --- |

{{Explain unresolved dependencies. Never imply that an external schema or code list was supplied when it was not.}}

## Structural overview

{{Describe roots, major blocks, and their ordering. Link an XSD-derived structure diagram if created.}}

## Global declarations and type index

| Stable local ID | Kind | Exact QName or anonymous schema path | Definition page | Source ID and schema locator |
| --- | --- | --- | --- | --- |

Include supplied global elements, attributes, types, reusable groups, and relevant identity constraints. Anonymous types must be identifiable by their enclosing schema location. Reuse links for recursive references.

## Root fields and compositors

| XML path / declaration | Kind / order | Type or reference | Member cardinality / attribute use | Enclosing sequence/all/choice and cardinality | Other constraints | Source locator / detail page |
| --- | --- | --- | --- | --- | --- | --- |

{{Retain group structure and alternatives. State effective XSD defaults explicitly when attributes were omitted. Link full component/type definitions instead of recursively flattening the whole schema.}}

## Namespace and reference notes

{{Record namespace-qualified identity, prefix mappings where useful, reusable groups, extension/restriction relationships, and recursion.}}

## Constraints and external code sets

{{Link complete type restrictions and schema enumerations. Keep external code-list publications separately versioned. Link business rules as distinct from XSD validation.}}

## Coverage and review evidence

- Owning coverage inventory: {{coverage_link}}
- Declaration/type reconciliation: {{result_and_evidence}}
- Dependency review: {{result_and_evidence}}
- Choice/cardinality/restriction review: {{result_and_evidence}}
- Open issues: {{issue_links_or_reviewed_none}}
- Source register / originals: {{source_links}}

[Template guide](README.md)
