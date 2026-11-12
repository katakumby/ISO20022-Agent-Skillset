---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "camt.018.001.05"
message_family: "camt.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"
source_ids: ["src-000015", "src-000032"]
source_editions: ["2024-2025", "February 2025"]
message_name: "GetBusinessDayInformationV05"
business_area: "camt"
message_version: "05"
message_sets: ["cash-management"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000015", "file_pages": [522, 534], "heading": "17 camt.018.001.05 GetBusinessDayInformationV05"}]
---

# camt.018.001.05 — GetBusinessDayInformationV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `GetBusinessDayInformationV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.018.001.05 | [src-000032](../../../../../raw-input/cash_management/camt.018.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.018.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Cash Management | raw-input/cash_management/camt.018.001.05.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/cash-management/2024-2025/index.md)
- [Source extraction coverage](../../message-sets/cash-management/2024-2025/coverage.md)
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
