---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "setr.007.001.05"
message_family: "setr.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.007.001.05"
source_ids: ["src-000096", "src-000143"]
source_editions: ["2025-2026", "May 2026"]
message_name: "SubscriptionBulkOrderV05"
business_area: "setr"
message_version: "05"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [2523, 2760], "heading": "47 setr.007.001.05 SubscriptionBulkOrderV05"}]
---

# setr.007.001.05 — SubscriptionBulkOrderV05

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SubscriptionBulkOrderV05`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | setr.007.001.05 | [src-000143](../../../../../raw-input/investment_funds/setr.007.001.05.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:setr.007.001.05 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/setr.007.001.05.xsd |

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








<!-- FUNDS-FLOW-0089-START -->
[Subscription confirmation amendment — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0089-END -->

<!-- FUNDS-FLOW-0097-START -->
[Subscription confirmation cancellation — bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0097-END -->

<!-- FUNDS-EARLY-FLOW-381 -->
[Order and Confirmation / Subscription  / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-381 -->

<!-- FUNDS-EARLY-FLOW-436 -->
[Order Instruction Status Reporting / Subscription / Bulk](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-436 -->

<!-- FUNDS-EARLY-FLOW-524 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Bulk ](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-524 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
