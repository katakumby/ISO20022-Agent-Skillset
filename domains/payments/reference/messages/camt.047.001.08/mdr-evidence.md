---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.047.001.08"
message_family: "camt.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.047.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "25 camt.047.001.08 ReturnReservationV08", "file_pages": [636, 653]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.047.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 25 camt.047.001.08 ReturnReservationV08

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp636–653; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 25 camt.047.001.08 ReturnReservationV08, Functionality, file p636.**

Scope
The ReturnReservation message is sent by the transaction administrator to a member.
It is used to provide information on the details of one or more reservation facilities set by the member
and managed by the transaction administrator.
The ReturnReservation message can be sent as a response to a related Get Reservation message
(pull mode) or initiated by the transaction administrator (push mode). The push of information can take
place either at prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the reservations facilities that the transaction administrator
manages for the member.
The transaction administrator will send reservations information to the member based on the following
elements:
- identification of the system
- identification of the account
- status of the reservation (default and/or current )
- type of reservation.
Outline
The ReturnReservationV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on reservations.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 636 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [25 camt.047.001.08 ReturnReservationV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00476.md) | 636–636 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00477.md) | 637–637 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00478.md) | 638–638 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00479.md) | 639–640 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00480.md) | 641–642 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CurrentReservation &lt;CurRsvatn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00481.md) | 643–643 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CurrentReservation &lt;CurRsvatn&gt; / 25.4.2.1.1.1 ReservationIdentification &lt;RsvatnId&gt; / 25.4.2.1.1.1.1 ReservationIdentification &lt;RsvatnId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00482.md) | 644–644 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CurrentReservation &lt;CurRsvatn&gt; / 25.4.2.1.1.1 ReservationIdentification &lt;RsvatnId&gt; / 25.4.2.1.1.1.3 Type &lt;Tp&gt; / 25.4.2.1.1.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00483.md) | 645–645 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CurrentReservation &lt;CurRsvatn&gt; / 25.4.2.1.1.2 ReservationOrError &lt;RsvatnOrErr&gt; / 25.4.2.1.1.2.1 Reservation &lt;Rsvatn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00484.md) | 646–646 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CurrentReservation &lt;CurRsvatn&gt; / 25.4.2.1.1.2 ReservationOrError &lt;RsvatnOrErr&gt; / 25.4.2.1.1.2.2 BusinessError &lt;BizErr&gt; / 25.4.2.1.1.2.2.1 Error &lt;Err&gt; / 25.4.2.1.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00485.md) | 647–647 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 DefaultReservation &lt;DfltRsvatn&gt; / 25.4.2.1.2.1 ReservationIdentification &lt;RsvatnId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00486.md) | 648–648 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 DefaultReservation &lt;DfltRsvatn&gt; / 25.4.2.1.2.1 ReservationIdentification &lt;RsvatnId&gt; / 25.4.2.1.2.1.2 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00487.md) | 649–649 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 DefaultReservation &lt;DfltRsvatn&gt; / 25.4.2.1.2.1 ReservationIdentification &lt;RsvatnId&gt; / 25.4.2.1.2.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00488.md) | 650–650 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 DefaultReservation &lt;DfltRsvatn&gt; / 25.4.2.1.2.2 ReservationOrError &lt;RsvatnOrErr&gt; / 25.4.2.1.2.2.1 Reservation &lt;Rsvatn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00489.md) | 651–651 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 DefaultReservation &lt;DfltRsvatn&gt; / 25.4.2.1.2.2 ReservationOrError &lt;RsvatnOrErr&gt; / 25.4.2.1.2.2.2 BusinessError &lt;BizErr&gt; / 25.4.2.1.2.2.2.1 Error &lt;Err&gt; / 25.4.2.1.2.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00490.md) | 652–652 |
| [25 camt.047.001.08 ReturnReservationV08 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.2 OperationalError &lt;OprlErr&gt; / 25.4.2.2.1 Error &lt;Err&gt; / 25.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00491.md) | 653–653 |

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
