---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.007.001.10"
message_family: "sese.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.007.001.10"
source_ids: ["src-000096", "src-000126"]
source_editions: ["2025-2026", "May 2026"]
message_name: "TransferInConfirmationV10"
business_area: "sese"
message_version: "10"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [695, 777], "heading": "30 sese.007.001.10 TransferInConfirmationV10"}]
---

# sese.007.001.10 — TransferInConfirmationV10

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `TransferInConfirmationV10`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.007.001.10 | [src-000126](../../../../../raw-input/investment_funds/sese.007.001.10.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.007.001.10 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/sese.007.001.10.xsd |

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







<!-- FUNDS-FLOW-0115-START -->
[Two-owner asset transfer — direct double leg](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p816-two-account-owners-direct-double-leg.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0115-END -->

<!-- FUNDS-FLOW-0116-START -->
[Two-owner asset transfer — direct single leg](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p822-two-account-owners-direct-single-leg.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0116-END -->

<!-- FUNDS-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0117-END -->

<!-- FUNDS-FLOW-0118-START -->
[Two-owner asset transfer — intermediary double leg](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p837-two-account-owners-intermediary-double-leg.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0118-END -->

<!-- FUNDS-FLOW-0120-START -->
[Transfer-in confirmation reversal](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p848-transfer-in-reversal.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0120-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
