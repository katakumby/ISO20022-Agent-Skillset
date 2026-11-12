---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.011.001.10"
message_family: "sese.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.011.001.10"
source_ids: ["src-000096", "src-000130"]
source_editions: ["2025-2026", "May 2026"]
message_name: "TransferInstructionStatusReportV10"
business_area: "sese"
message_version: "10"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [816, 942], "heading": "34 sese.011.001.10 TransferInstructionStatusReportV10"}]
---

# sese.011.001.10 — TransferInstructionStatusReportV10

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `TransferInstructionStatusReportV10`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.011.001.10 | [src-000130](../../../../../raw-input/investment_funds/sese.011.001.10.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.011.001.10 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/sese.011.001.10.xsd |

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
















<!-- FUNDS-FLOW-0107-START -->
[Portfolio transfer discovery](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p764-discovery.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0107-END -->

<!-- FUNDS-FLOW-0108-START -->
[Portfolio transfer instruction and completion](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p768-portfolio-transfer-instruction.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0108-END -->

<!-- FUNDS-FLOW-0109-START -->
[Portfolio transfer instruction rejected](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p779-rejected.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0109-END -->

<!-- FUNDS-FLOW-0110-START -->
[Portfolio transfer status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p783-request-status.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0110-END -->

<!-- FUNDS-FLOW-0111-START -->
[Portfolio transfer cancellation accepted](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p789-cancellation.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0111-END -->

<!-- FUNDS-FLOW-0112-START -->
[Portfolio transfer cancellation rejected for invalid reference](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p794-rejected-cancellation-invalid-reference.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0112-END -->

<!-- FUNDS-FLOW-0113-START -->
[Portfolio transfer cancellation rejected after execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p799-rejected-cancellation-already-executed.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0113-END -->

<!-- FUNDS-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0117-END -->

<!-- FUNDS-FLOW-0123-START -->
[Transfer instruction status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p867-request-for-status.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0123-END -->

<!-- FUNDS-FLOW-0124-START -->
[Transfer instruction status query rejected](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0124-END -->

<!-- FUNDS-FLOW-0125-START -->
[Unsolicited transfer instruction status — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p876-status-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0125-END -->

<!-- FUNDS-FLOW-0126-START -->
[Unsolicited transfer instruction status — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p881-status-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0126-END -->

<!-- FUNDS-FLOW-0127-START -->
[Transfer cancellation status query — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p886-cancellation-status-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0127-END -->

<!-- FUNDS-FLOW-0128-START -->
[Transfer cancellation status query — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p893-transfer-cancellation-status-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0128-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
