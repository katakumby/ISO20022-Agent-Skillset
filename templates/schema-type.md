---
template: true
document_kind: schema-type
review_status: template
domain: "{{domain}}"
message_id: "{{full_message_id}}"
type_id: "{{type_id}}"
type_kind: "{{simple_complex_or_anonymous}}"
qname_or_schema_path: "{{exact_qname_or_anonymous_path}}"
namespace: "{{namespace}}"
source_ids: []
source_editions: []
---

# {{exact_type_name_or_anonymous_location}}

> TEMPLATE ONLY: document one complete type or reusable schema component. Remove inapplicable sections only with a clear statement of why they do not apply.

## Identity and provenance

| Item | Value |
| --- | --- |
| Stable local ID | {{type_id}} |
| Exact QName or anonymous type location | {{qname_or_schema_path}} |
| Source ID and schema locator | {{source_and_locator}} |
| Definition / source annotation | {{source_backed_definition}} |
| Base type and derivation | {{base_type_extension_or_restriction}} |
| Referenced by | {{relative_links_to_users}} |

## Compositor structure

{{Preserve nesting and order of sequence, all, and choice groups, including each group's min/max occurrences. Identify alternatives and reused groups.}}

## Elements and attributes

| XML name / QName or ref | Kind / order | Type / definition link | minOccurs..maxOccurs or attribute use | Enclosing group / alternatives | Nillable / default / fixed | Source locator |
| --- | --- | --- | --- | --- | --- | --- |

Record every member. For attributes, distinguish required, optional, and prohibited use. For elements, preserve ordering, wildcard behavior, and namespace qualification. Explain effective defaults separately from attributes present in the source.

## Restrictions and facets

| Facet / constraint | Exact value or expression | Applies to | Inherited or declared | Source locator |
| --- | --- | --- | --- | --- |

Cover patterns, lengths, bounds, total/fraction digits, whitespace, lists/unions, and other supplied facets as applicable. Preserve lexical expressions exactly.

## Schema enumeration values

| Exact code value | Source annotation / meaning | Source locator |
| --- | --- | --- |

Do not fill this table with guessed external code values. If the type uses an external list, cite its independently versioned publication.

## Other schema semantics

{{Record applicable content model, mixed/simple content, group references, wildcards/processContents, abstract/substitution behavior, identity constraints, and namespace rules. Link any unsupported construct to an issue.}}

## Recursion and reuse

{{Link recursive or shared types without infinite expansion. Distinguish same local names in different namespaces.}}

## Business meaning versus schema behavior

{{Keep MDR descriptions and business restrictions explicitly attributed and separate from what the XSD enforces.}}

## Coverage and review

- Structure index: {{structure_link}}
- Coverage item: {{coverage_link_and_item_id}}
- Review evidence: {{actual_checks_and_date}}
- Open issues: {{issue_links_or_reviewed_none}}
- Sources: {{source_links}}

[Template guide](README.md)
