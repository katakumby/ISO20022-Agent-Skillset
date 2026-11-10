---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "secl.005.001.02"
message_family: "secl.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"
source_ids: ["src-000053", "src-000059"]
source_editions: ["2025-2026", "March 2026; Standards MX November 2026 release"]
message_name: "MarginReportV02"
business_area: "secl"
message_version: "02"
message_sets: ["ccp-clearing"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000053", "file_pages": [232, 245], "heading": "6 MX secl.005.001.02 MarginReportV02"}]
---

# secl.005.001.02 — MarginReportV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `MarginReportV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | secl.005.001.02 | [src-000059](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.005.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:secl.005.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | CCP Clearing | raw-input/central_counterparty_clearing_ccp_clearing/secl.005.001.02.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/ccp-clearing/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/ccp-clearing/2025-2026/coverage.md)
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
