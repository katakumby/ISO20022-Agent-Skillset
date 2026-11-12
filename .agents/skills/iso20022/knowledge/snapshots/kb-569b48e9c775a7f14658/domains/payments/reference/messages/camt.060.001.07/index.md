---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "camt.060.001.07"
message_family: "camt.060"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.060.001.07"
source_ids: ["src-000005", "src-000010"]
source_editions: ["2025-2026", "March 2026"]
message_name: "AccountReportingRequestV07"
business_area: "camt"
message_version: "07"
message_sets: ["bank-to-customer-cash-management"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000005", "file_pages": [781, 795], "heading": "5 camt.060.001.07 AccountReportingRequestV07"}]
---

# camt.060.001.07 — AccountReportingRequestV07

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `AccountReportingRequestV07`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.060.001.07 | [src-000010](../../../../../raw-input/banktocustomer_cash_management/camt.060.001.07.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.060.001.07 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Bank-to-Customer Cash Management | raw-input/banktocustomer_cash_management/camt.060.001.07.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/bank-to-customer-cash-management/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/bank-to-customer-cash-management/2025-2026/coverage.md)
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
