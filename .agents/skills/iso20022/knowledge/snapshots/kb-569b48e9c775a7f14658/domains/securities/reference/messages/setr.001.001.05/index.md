---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.001.001.05"
message_family: "setr.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.001.001.05"
source_ids: ["src-000096", "src-000137"]
source_editions: ["2025-2026", "May 2026"]
message_name: "RedemptionBulkOrderV05"
business_area: "setr"
message_version: "05"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [1685, 1886], "heading": "41 setr.001.001.05 RedemptionBulkOrderV05"}]
---

# setr.001.001.05 — RedemptionBulkOrderV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `RedemptionBulkOrderV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.001.001.05 | [src-000137](../../../../../raw-input/investment_funds/setr.001.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.001.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/setr.001.001.05.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/investment-funds/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/investment-funds/2025-2026/coverage.md)
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













<!-- FUNDS-FLOW-0077-START -->
[Redemption cancellation — bulk and reinstruction](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p544-request-and-status-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0077-END -->

<!-- FUNDS-FLOW-0092-START -->
[Redemption confirmation amendment — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p650-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0092-END -->

<!-- FUNDS-FLOW-0100-START -->
[Redemption confirmation cancellation — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p707-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0100-END -->

<!-- FUNDS-EARLY-FLOW-400 -->
[Order and Confirmation / Redemption / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p400-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-400 -->

<!-- FUNDS-EARLY-FLOW-456 -->
[Order Instruction Status Reporting / Redemption / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-456 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
