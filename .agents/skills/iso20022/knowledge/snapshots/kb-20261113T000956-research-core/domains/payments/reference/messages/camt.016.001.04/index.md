---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "payments"
message_id: "camt.016.001.04"
message_family: "camt.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"
source_ids: ["src-000015", "src-000030"]
source_editions: ["2024-2025", "February 2025"]
message_name: "GetCurrencyExchangeRateV04"
business_area: "camt"
message_version: "04"
message_sets: ["cash-management"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000015", "file_pages": [505, 510], "heading": "15 camt.016.001.04 GetCurrencyExchangeRateV04"}]
---

# camt.016.001.04 — GetCurrencyExchangeRateV04

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `GetCurrencyExchangeRateV04`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.016.001.04 | [src-000030](../../../../../raw-input/cash_management/camt.016.001.04.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.016.001.04 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Cash Management | raw-input/cash_management/camt.016.001.04.xsd |

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
