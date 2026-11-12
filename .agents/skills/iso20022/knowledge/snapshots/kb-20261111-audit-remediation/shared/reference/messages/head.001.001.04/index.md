---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "shared"
message_id: "head.001.001.04"
message_family: "head.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
source_ids: ["src-000011", "src-000013"]
source_editions: ["Version 4 March 2024", "march-2024"]
message_name: "BusinessApplicationHeaderV04"
business_area: "head"
message_version: "04"
message_sets: ["business-application-header"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000011", "file_pages": [4, 25], "heading": "2 head.001.001.04 BusinessApplicationHeaderV04"}]
---

# head.001.001.04 — BusinessApplicationHeaderV04

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `BusinessApplicationHeaderV04`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | head.001.001.04 | [src-000013](../../../../raw-input/business_application_header/head.001.001.04.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:head.001.001.04 | /xs:schema/@targetNamespace |
| Root(s) | AppHdr | /xs:schema/xs:element |
| Collection | Business Application Header | raw-input/business_application_header/head.001.001.04.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/business-application-header/march-2024/index.md)
- [Source extraction coverage](../../message-sets/business-application-header/march-2024/coverage.md)
- [Shared participants](../../../../catalog/participants.md)
- [Business flows](../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.



## Curated business reference

[Purpose, participants, usage boundaries and complete source business rules](business.md).


<!-- MDR-NAV-START -->
## Supplied business evidence

[Purpose, usage, actors and detailed MDR evidence](mdr-evidence.md) · [Curated message context](business.md)
<!-- MDR-NAV-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
