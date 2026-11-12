---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "seev.034.001.16"
message_family: "seev.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.034.001.16"
source_ids: ["src-000080", "src-000085"]
source_editions: ["2025-2026", "February 2026"]
message_name: "CorporateActionInstructionStatusAdviceV16"
business_area: "seev"
message_version: "16"
message_sets: ["corporate-actions"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000080", "file_pages": [320, 359], "heading": "6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"}]
---

# seev.034.001.16 — CorporateActionInstructionStatusAdviceV16

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `CorporateActionInstructionStatusAdviceV16`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | seev.034.001.16 | [src-000085](../../../../../raw-input/corporate_actions/seev.034.001.16.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:seev.034.001.16 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Corporate Actions | raw-input/corporate_actions/seev.034.001.16.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/corporate-actions/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/corporate-actions/2025-2026/coverage.md)
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
