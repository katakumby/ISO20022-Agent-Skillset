---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "reda.010.001.01"
message_family: "reda.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01"
source_ids: ["src-000233", "src-000266", "src-000378"]
source_editions: ["August 2026", "March 2024", "june-2021"]
message_name: "SecurityQueryV01"
business_area: "reda"
message_version: "01"
message_sets: ["t2s", "t2s-securities-reference-data"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [1764, 1783], "heading": "31 reda.010.001.01 SecurityQueryV01"}, {"source_id": "src-000378", "file_pages": [77, 93], "heading": "6 reda.010.001.01 SecurityQueryV01"}]
---

# reda.010.001.01 — SecurityQueryV01

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecurityQueryV01`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | reda.010.001.01 | [src-000266](../../../../../raw-input/target2securities_t2s/reda.010.001.01.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:reda.010.001.01 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S SecuritiesReferenceData | raw-input/target2securities_t2s/reda.010.001.01.xsd |

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






<!-- SECREF-FIG-10-START -->
[Security query and audit-trail query activity](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p162-query-query-response-process.md) — June2021 business evidence; March2024 companion definition is a separate publication.
<!-- SECREF-FIG-10-END -->

<!-- SECREF-FIG-18-START -->
[Security query and report exchange](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p294-security-query-security-report-scenario.md) — June2021 business evidence; March2024 companion definition is a separate publication.
<!-- SECREF-FIG-18-END -->

<!-- SECREF-EXAMPLES-START -->
[June2021 business examples: exact identifiers, source conditions and literal XML checks](../../message-sets/t2s-securities-reference-data/june-2021/business-examples.md)
<!-- SECREF-EXAMPLES-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
