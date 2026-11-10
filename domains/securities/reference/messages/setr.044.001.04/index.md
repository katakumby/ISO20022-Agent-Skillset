---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.044.001.04"
message_family: "setr.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"
source_ids: ["src-000181", "src-000187"]
source_editions: ["2024-2025", "February 2025"]
message_name: "SecuritiesTradeConfirmationStatusAdviceV04"
business_area: "setr"
message_version: "04"
message_sets: ["post-trade-matching"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000181", "file_pages": [162, 221], "heading": "6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
---

# setr.044.001.04 — SecuritiesTradeConfirmationStatusAdviceV04

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesTradeConfirmationStatusAdviceV04`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.044.001.04 | [src-000187](../../../../../raw-input/post_trade_matching/setr.044.001.04.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.044.001.04 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Post-Trade Matching | raw-input/post_trade_matching/setr.044.001.04.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/post-trade-matching/2024-2025/index.md)
- [Source extraction coverage](../../message-sets/post-trade-matching/2024-2025/coverage.md)
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
