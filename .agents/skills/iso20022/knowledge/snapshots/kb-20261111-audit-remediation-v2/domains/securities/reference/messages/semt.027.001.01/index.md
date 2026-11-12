---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "semt.027.001.01"
message_family: "semt.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01"
source_ids: ["src-000233", "src-000310", "src-000375"]
source_editions: ["August 2026", "march-2026"]
message_name: "SecuritiesSettlementTransactionQueryResponseV01"
business_area: "semt"
message_version: "01"
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [2473, 2561], "heading": "72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01"}, {"source_id": "src-000375", "file_pages": [77, 165], "heading": "4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01"}]
---

# semt.027.001.01 — SecuritiesSettlementTransactionQueryResponseV01

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesSettlementTransactionQueryResponseV01`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | semt.027.001.01 | [src-000310](../../../../../raw-input/target2securities_t2s/semt.027.001.01.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:semt.027.001.01 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S SecuritiesAndPenaltyReporting | raw-input/target2securities_t2s/semt.027.001.01.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/index.md)
- [Source extraction coverage](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/coverage.md)
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
