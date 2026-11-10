---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.013.001.05"
message_family: "setr.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.013.001.05"
source_ids: ["src-000096", "src-000149"]
source_editions: ["2025-2026", "May 2026"]
message_name: "SwitchOrderV05"
business_area: "setr"
message_version: "05"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [3487, 3796], "heading": "53 setr.013.001.05 SwitchOrderV05"}]
---

# setr.013.001.05 — SwitchOrderV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SwitchOrderV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.013.001.05 | [src-000149](../../../../../raw-input/investment_funds/setr.013.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.013.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/setr.013.001.05.xsd |

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





































<!-- FUNDS-FLOW-0078-START -->
[Switch cancellation — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p554-request-and-status-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0078-END -->

<!-- FUNDS-FLOW-0079-START -->
[Switch cancellation — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p558-request-and-status-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0079-END -->

<!-- FUNDS-FLOW-0083-START -->
[Switch cancellation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p586-request-status-of-switch.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0083-END -->

<!-- FUNDS-FLOW-0086-START -->
[Switch confirmation rejected by instructing party](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p607-switch.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0086-END -->

<!-- FUNDS-FLOW-0093-START -->
[Switch confirmation amendment — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p659-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0093-END -->

<!-- FUNDS-FLOW-0094-START -->
[Switch confirmation amendment — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p664-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0094-END -->

<!-- FUNDS-FLOW-0101-START -->
[Switch confirmation cancellation — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p716-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0101-END -->

<!-- FUNDS-FLOW-0102-START -->
[Switch confirmation cancellation — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p720-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0102-END -->

<!-- FUNDS-FLOW-0105-START -->
[Switch amended-confirmation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p745-switch.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0105-END -->

<!-- FUNDS-EARLY-FLOW-407 -->
[Order and Confirmation / Switch  / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p407-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-407 -->

<!-- FUNDS-EARLY-FLOW-411 -->
[Order and Confirmation / Switch  / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p411-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-411 -->

<!-- FUNDS-EARLY-FLOW-465 -->
[Order Instruction Status Reporting / Switch / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-465 -->

<!-- FUNDS-EARLY-FLOW-469 -->
[Order Instruction Status Reporting / Switch / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-469 -->

<!-- FUNDS-EARLY-FLOW-486 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Switch](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-486 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
