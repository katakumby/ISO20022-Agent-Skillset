---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.048.001.07"
message_family: "camt.048"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.048.001.07"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "26 camt.048.001.07 ModifyReservationV07", "file_pages": [654, 662]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.048.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 26 camt.048.001.07 ModifyReservationV07

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp654–662; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 26 camt.048.001.07 ModifyReservationV07, Functionality, file p654.**

Scope
The ModifyReservation message is used to request modifications in the details of one particular
reservation set by the member and managed by the transaction administrator.
Usage
After the receipt of a ModifyReservation message the transaction administrator checks whether the
amount of liquidity on the member account is sufficient to set the reservation.
If there is enough liquidity available, the requested amount will be reserved. In case the requested
amount exceeds the available liquidity, only the available liquidity will be reserved. The difference will
not be blocked at a later point, even if the account balance of the member reaches the level of the initial
reservation request.
The reservation can be effected directly by the member, who has the possibility to:
- reset the reserved liquidity to zero
- change the reservation amount during the day with immediate effect
- input a default reservation amount for the following day(s); valid until a new reservation amount is
requested
After the receipt of a ModifyReservation message the transaction administrator checks whether the
amount of liquidity on the member account is sufficient to set the reservation.
Outline
The ModifyReservationV07 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationIdentification
Identification of the default reservation.
C. NewReservationValueSet
New reservation values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 654 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [26 camt.048.001.07 ModifyReservationV07](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00492.md) | 654–654 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00493.md) | 655–655 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00494.md) | 656–656 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.2 ReservationIdentification &lt;RsvatnId&gt; / 26.4.2.1 Current &lt;Cur&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00495.md) | 657–657 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.2 ReservationIdentification &lt;RsvatnId&gt; / 26.4.2.1 Current &lt;Cur&gt; / 26.4.2.1.1 ReservationIdentification &lt;RsvatnId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00496.md) | 658–658 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.2 ReservationIdentification &lt;RsvatnId&gt; / 26.4.2.1 Current &lt;Cur&gt; / 26.4.2.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00497.md) | 659–659 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.2 ReservationIdentification &lt;RsvatnId&gt; / 26.4.2.2 Default &lt;Dflt&gt; / 26.4.2.2.1 ReservationIdentification &lt;RsvatnId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00498.md) | 660–660 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.2 ReservationIdentification &lt;RsvatnId&gt; / 26.4.2.2 Default &lt;Dflt&gt; / 26.4.2.2.3 Type &lt;Tp&gt; / 26.4.2.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00499.md) | 661–661 |
| [26 camt.048.001.07 ModifyReservationV07 / 26.4 Message Building Blocks / 26.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00500.md) | 662–662 |

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

- [Modify Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p251-modify-reservation-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
