---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "semt.001.001.03"
message_family: "semt.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.001.001.03"
source_ids: ["src-000096", "src-000113"]
source_editions: ["2025-2026", "May 2026"]
message_name: "SecuritiesMessageRejectionV03"
business_area: "semt"
message_version: "03"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [371, 374], "heading": "17 semt.001.001.03 SecuritiesMessageRejectionV03"}]
---

# semt.001.001.03 — SecuritiesMessageRejectionV03

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesMessageRejectionV03`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | semt.001.001.03 | [src-000113](../../../../../raw-input/investment_funds/semt.001.001.03.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:semt.001.001.03 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/semt.001.001.03.xsd |

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









<!-- FUNDS-FLOW-0082-START -->
[Redemption cancellation request rejected for invalid reference](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p581-status-request-rejected.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0082-END -->

<!-- FUNDS-FLOW-0106-START -->
[Transfer status request rejected for an unknown reference](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p752-message-rejection.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0106-END -->

<!-- FUNDS-FLOW-0112-START -->
[Portfolio transfer cancellation rejected for invalid reference](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p794-rejected-cancellation-invalid-reference.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0112-END -->

<!-- FUNDS-FLOW-0124-START -->
[Transfer instruction status query rejected](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0124-END -->

<!-- FUNDS-EARLY-FLOW-251 -->
[Account Management / Account Opening / Rejection - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p251-rejection-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-251 -->

<!-- FUNDS-EARLY-FLOW-256 -->
[Account Management / Account Opening / Rejection - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p256-rejection-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-256 -->

<!-- FUNDS-EARLY-FLOW-269 -->
[Account Management / Account Modification / Rejection - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p269-rejection-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-269 -->

<!-- FUNDS-EARLY-FLOW-274 -->
[Account Management / Account Modification / Rejection - Intermediary](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p274-rejection-intermediary.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-274 -->

<!-- FUNDS-EARLY-FLOW-302 -->
[Account Management / Request for Account Management Status Rejection - Direct](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p302-request-for-account-management-status-rejection-direct.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-302 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
