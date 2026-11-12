---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.103.001.03"
message_family: "camt.103"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.103.001.03"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "35 camt.103.001.03 CreateReservationV03", "file_pages": [767, 772]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.103.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 35 camt.103.001.03 CreateReservationV03

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp767–772; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 35 camt.103.001.03 CreateReservationV03, Functionality, file p767.**

Scope
The CreateReservation message is used to request for the creation of one particular reservation by the
member and managed by the transaction administrator.
Usage
Based on the criteria defined in the CreateReservation message, the transaction administrator will
execute or reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateReservationV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationIdentification
Identification of the default reservation.
C. ValueSet
New reservation values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.103.001.03 CreateReservationV03
Cash Management - Maintenance 2024 - 2025 767 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [35 camt.103.001.03 CreateReservationV03](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00591.md) | 767–767 |
| [35 camt.103.001.03 CreateReservationV03 / 35.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00592.md) | 768–768 |
| [35 camt.103.001.03 CreateReservationV03 / 35.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00593.md) | 769–769 |
| [35 camt.103.001.03 CreateReservationV03 / 35.4 Message Building Blocks / 35.4.2 ReservationIdentification &lt;RsvatnId&gt; / 35.4.2.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00594.md) | 770–770 |
| [35 camt.103.001.03 CreateReservationV03 / 35.4 Message Building Blocks / 35.4.2 ReservationIdentification &lt;RsvatnId&gt; / 35.4.2.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00595.md) | 771–771 |
| [35 camt.103.001.03 CreateReservationV03 / 35.4 Message Building Blocks / 35.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00596.md) | 772–772 |

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

- [Create Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p247-create-reservation-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
