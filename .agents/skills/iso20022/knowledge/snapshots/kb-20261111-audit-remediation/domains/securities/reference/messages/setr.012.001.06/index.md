---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.012.001.06"
message_family: "setr.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.012.001.06"
source_ids: ["src-000096", "src-000148"]
source_editions: ["2025-2026", "May 2026"]
message_name: "SubscriptionOrderConfirmationV06"
business_area: "setr"
message_version: "06"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [3248, 3486], "heading": "52 setr.012.001.06 SubscriptionOrderConfirmationV06"}]
---

# setr.012.001.06 — SubscriptionOrderConfirmationV06

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SubscriptionOrderConfirmationV06`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.012.001.06 | [src-000148](../../../../../raw-input/investment_funds/setr.012.001.06.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.012.001.06 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/setr.012.001.06.xsd |

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




























<!-- FUNDS-FLOW-0084-START -->
[Subscription confirmation rejected by instructing party](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p597-subscription.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0084-END -->

<!-- FUNDS-FLOW-0087-START -->
[Subscription confirmation amendment — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p619-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0087-END -->

<!-- FUNDS-FLOW-0088-START -->
[Subscription confirmation amendment — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p624-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0088-END -->

<!-- FUNDS-FLOW-0089-START -->
[Subscription confirmation amendment — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0089-END -->

<!-- FUNDS-FLOW-0095-START -->
[Subscription confirmation cancellation — direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p677-direct.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0095-END -->

<!-- FUNDS-FLOW-0096-START -->
[Subscription confirmation cancellation — intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p682-intermediary.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0096-END -->

<!-- FUNDS-FLOW-0097-START -->
[Subscription confirmation cancellation — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0097-END -->

<!-- FUNDS-FLOW-0103-START -->
[Subscription amended-confirmation status query](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p731-subscription.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0103-END -->

<!-- FUNDS-EARLY-FLOW-368 -->
[Order and Confirmation / Subscription  / Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p368-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-368 -->

<!-- FUNDS-EARLY-FLOW-374 -->
[Order and Confirmation / Subscription  / Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p374-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-374 -->

<!-- FUNDS-EARLY-FLOW-381 -->
[Order and Confirmation / Subscription  / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-381 -->

<!-- FUNDS-EARLY-FLOW-491 -->
[Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-491 -->

<!-- FUNDS-EARLY-FLOW-524 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Bulk ](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-524 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
