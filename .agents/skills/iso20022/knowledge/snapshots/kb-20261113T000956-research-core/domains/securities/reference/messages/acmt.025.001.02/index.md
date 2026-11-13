---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.025.001.02"
message_family: "acmt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02"
source_ids: ["src-000235", "src-000351"]
source_editions: ["august-2026"]
message_name: "AccountQueryListV02"
business_area: "acmt"
message_version: "02"
message_sets: ["t2s-cash-account-query-and-report"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000351", "file_pages": [4, 47], "heading": "2 acmt.025.001.02 AccountQueryListV02"}]
---

# acmt.025.001.02 — AccountQueryListV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `AccountQueryListV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | acmt.025.001.02 | [src-000235](../../../../../raw-input/target2securities_t2s/acmt.025.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S CashAccountQueryAndReport | raw-input/target2securities_t2s/acmt.025.001.02.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-cash-account-query-and-report/august-2026/index.md)
- [Source extraction coverage](../../message-sets/t2s-cash-account-query-and-report/august-2026/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.


<!-- MDR-NAV-START -->
## Supplied business evidence

[Purpose, usage, actors and detailed MDR evidence](mdr-evidence.md)
<!-- MDR-NAV-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
