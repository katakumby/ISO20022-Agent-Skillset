---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.016.001.05"
message_family: "setr.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.016.001.05"
source_ids: ["src-000096", "src-000152"]
source_editions: ["2025-2026", "May 2026"]
message_name: "OrderInstructionStatusReportV05"
business_area: "setr"
message_version: "05"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [4109, 4204], "heading": "56 setr.016.001.05 OrderInstructionStatusReportV05"}]
---

# setr.016.001.05 — OrderInstructionStatusReportV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `OrderInstructionStatusReportV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.016.001.05 | [src-000152](../../../../../raw-input/investment_funds/setr.016.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.016.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/setr.016.001.05.xsd |

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






















<!-- FUNDS-FLOW-0080-START -->
[Subscription cancellation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p569-request-status-of-subscription.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0080-END -->

<!-- FUNDS-FLOW-0081-START -->
[Redemption cancellation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p575-request-status-of-redemption.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0081-END -->

<!-- FUNDS-FLOW-0082-START -->
[Redemption cancellation request rejected for invalid reference](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p581-status-request-rejected.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0082-END -->

<!-- FUNDS-FLOW-0083-START -->
[Switch cancellation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p586-request-status-of-switch.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0083-END -->

<!-- FUNDS-EARLY-FLOW-425 -->
[Order Instruction Status Reporting / Subscription / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p425-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-425 -->

<!-- FUNDS-EARLY-FLOW-445 -->
[Order Instruction Status Reporting / Redemption / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p445-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-445 -->

<!-- FUNDS-EARLY-FLOW-465 -->
[Order Instruction Status Reporting / Switch / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-465 -->

<!-- FUNDS-EARLY-FLOW-429 -->
[Order Instruction Status Reporting / Subscription / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p429-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-429 -->

<!-- FUNDS-EARLY-FLOW-449 -->
[Order Instruction Status Reporting / Redemption / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p449-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-449 -->

<!-- FUNDS-EARLY-FLOW-469 -->
[Order Instruction Status Reporting / Switch / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-469 -->

<!-- FUNDS-EARLY-FLOW-436 -->
[Order Instruction Status Reporting / Subscription / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-436 -->

<!-- FUNDS-EARLY-FLOW-456 -->
[Order Instruction Status Reporting / Redemption / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-456 -->

<!-- FUNDS-EARLY-FLOW-476 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Subscription ](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p476-request-status-of-subscription.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-476 -->

<!-- FUNDS-EARLY-FLOW-481 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Redemption ](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p481-request-status-of-redemption.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-481 -->

<!-- FUNDS-EARLY-FLOW-486 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Switch](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-486 -->

<!-- FUNDS-EARLY-FLOW-491 -->
[Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-491 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
