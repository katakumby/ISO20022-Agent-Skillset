---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.046.001.08"
message_family: "camt.046"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.046.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "24 camt.046.001.08 GetReservationV08", "file_pages": [624, 635]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.046.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 24 camt.046.001.08 GetReservationV08

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp624–635; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 24 camt.046.001.08 GetReservationV08, Functionality, file p624.**

Scope
The GetReservation message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more reservation facilities set by the member
and managed by the transaction administrator.
Usage
The member can request reservations information based on the following elements:
- identification of the system;
- identification of the account;
- status of the reservation (default and/or current);
- type of reservation.
This message will be replied to by a ReturnReservation message.
Outline
The GetReservationV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReservationQueryDefinition
Definition of the reservation query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 624 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [24 camt.046.001.08 GetReservationV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00464.md) | 624–624 |
| [24 camt.046.001.08 GetReservationV08 / 24.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00465.md) | 625–625 |
| [24 camt.046.001.08 GetReservationV08 / 24.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00466.md) | 626–626 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00467.md) | 627–627 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00468.md) | 628–628 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00469.md) | 629–629 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00470.md) | 630–630 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00471.md) | 631–631 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.2.1 DateTime &lt;DtTm&gt; / 24.4.2.2.2.2.1.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00472.md) | 632–632 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.2.3 DefaultReservationType &lt;DfltRsvatnTp&gt; / 24.4.2.2.2.2.3.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00473.md) | 633–633 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.2.6 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00474.md) | 634–634 |
| [24 camt.046.001.08 GetReservationV08 / 24.4 Message Building Blocks / 24.4.2 ReservationQueryDefinition &lt;RsvatnQryDef&gt; / 24.4.2.2 ReservationCriteria &lt;RsvatnCrit&gt; / 24.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 24.4.2.2.2.3.2 StatusIndicator &lt;StsInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00475.md) | 635–635 |

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

- [Get/Return Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p236-get-return-reservation-scenario.md)
- [Get/Return Reservation Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p241-get-return-reservation-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
