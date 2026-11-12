---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "reda.029.001.01"
message_family: "reda.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.029.001.01"
source_ids: ["src-000233", "src-000284", "src-000378"]
source_editions: ["August 2026", "March 2024", "june-2021"]
message_name: "SecurityMaintenanceStatusAdviceV01"
business_area: "reda"
message_version: "01"
message_sets: ["t2s", "t2s-securities-reference-data"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [2203, 2207], "heading": "49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01"}, {"source_id": "src-000378", "file_pages": [119, 123], "heading": "9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01"}]
---

# reda.029.001.01 — SecurityMaintenanceStatusAdviceV01

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecurityMaintenanceStatusAdviceV01`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | reda.029.001.01 | [src-000284](../../../../../raw-input/target2securities_t2s/reda.029.001.01.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:reda.029.001.01 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S SecuritiesReferenceData | raw-input/target2securities_t2s/reda.029.001.01.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-securities-reference-data/june-2021/index.md)
- [Source extraction coverage](../../message-sets/t2s-securities-reference-data/june-2021/coverage.md)
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








<!-- SECREF-FIG-8-START -->
[Security modification activity](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p156-modification-process.md) — June2021 business evidence; March2024 companion definition is a separate publication.
<!-- SECREF-FIG-8-END -->

<!-- SECREF-FIG-14-START -->
[Security maintenance — confirmation](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p211-confirmation-scenario.md) — June2021 business evidence; March2024 companion definition is a separate publication.
<!-- SECREF-FIG-14-END -->

<!-- SECREF-FIG-15-START -->
[Security maintenance — rejection](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p231-rejection-scenario.md) — June2021 business evidence; March2024 companion definition is a separate publication.
<!-- SECREF-FIG-15-END -->

<!-- SECREF-EXAMPLES-START -->
[June2021 business examples: exact identifiers, source conditions and literal XML checks](../../message-sets/t2s-securities-reference-data/june-2021/business-examples.md)
<!-- SECREF-EXAMPLES-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
