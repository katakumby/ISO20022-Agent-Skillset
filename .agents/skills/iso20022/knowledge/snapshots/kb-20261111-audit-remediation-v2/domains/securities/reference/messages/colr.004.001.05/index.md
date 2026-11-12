---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "colr.004.001.05"
message_family: "colr.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05"
source_ids: ["src-000066"]
source_editions: []
message_name: "MarginCallResponseV05"
business_area: "colr"
message_version: "05"
message_sets: ["collateral-management"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
---

# colr.004.001.05 — MarginCallResponseV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `MarginCallResponseV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | colr.004.001.05 | [src-000066](../../../../../raw-input/collateral_management_collateral_management/colr.004.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:colr.004.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Collateral Management | raw-input/collateral_management_collateral_management/colr.004.001.05.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/collateral-management/edition-unknown-src-000065/index.md)
- [Source extraction coverage](../../message-sets/collateral-management/edition-unknown-src-000065/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
