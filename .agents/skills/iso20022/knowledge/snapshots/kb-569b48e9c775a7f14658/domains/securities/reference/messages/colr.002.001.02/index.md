---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "colr.002.001.02"
message_family: "colr.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.002.001.02"
source_ids: ["src-000233", "src-000260", "src-000357"]
source_editions: ["August 2026", "march-2024"]
message_name: "CollateralValueReportV02"
business_area: "colr"
message_version: "02"
message_sets: ["t2s", "t2s-collateral-reporting"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [590, 613], "heading": "25 colr.002.001.02 CollateralValueReportV02"}, {"source_id": "src-000357", "file_pages": [16, 39], "heading": "3 colr.002.001.02 CollateralValueReportV02"}]
---

# colr.002.001.02 — CollateralValueReportV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `CollateralValueReportV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | colr.002.001.02 | [src-000260](../../../../../raw-input/target2securities_t2s/colr.002.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:colr.002.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S CollateralReporting | raw-input/target2securities_t2s/colr.002.001.02.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-collateral-reporting/march-2024/index.md)
- [Source extraction coverage](../../message-sets/t2s-collateral-reporting/march-2024/coverage.md)
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
