---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.049.001.07"
message_family: "camt.049"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.049.001.07"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "27 camt.049.001.07 DeleteReservationV07", "file_pages": [663, 667]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.049.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 27 camt.049.001.07 DeleteReservationV07

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp663–667; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 27 camt.049.001.07 DeleteReservationV07, Functionality, file p663.**

Scope
The DeleteReservation message is used to request the deletion of one particular reservation by the
member and managed by the transaction administrator.
Usage
The deletion of a reservation in the system, will not only reset the reserved liquidity to zero, but also
delete the reservation itself from the system: only the default reservation for the current business day
remains in the system.
Outline
The DeleteReservationV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CurrentReservation
Identifies the current reservation to delete.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.049.001.07 DeleteReservationV07
Cash Management - Maintenance 2024 - 2025 663 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [27 camt.049.001.07 DeleteReservationV07](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00501.md) | 663–663 |
| [27 camt.049.001.07 DeleteReservationV07 / 27.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00502.md) | 664–664 |
| [27 camt.049.001.07 DeleteReservationV07 / 27.4 Message Building Blocks / 27.4.2 CurrentReservation &lt;CurRsvatn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00503.md) | 665–665 |
| [27 camt.049.001.07 DeleteReservationV07 / 27.4 Message Building Blocks / 27.4.2 CurrentReservation &lt;CurRsvatn&gt; / 27.4.2.3 Type &lt;Tp&gt; / 27.4.2.3.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00504.md) | 666–666 |
| [27 camt.049.001.07 DeleteReservationV07 / 27.4 Message Building Blocks / 27.4.2 CurrentReservation &lt;CurRsvatn&gt; / 27.4.2.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00505.md) | 667–667 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Delete Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p255-delete-reservation-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
