---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.085.001.02"
message_family: "camt.085"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.085.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "file_pages": [549, 577]}, {"source_id": "src-000360", "heading": "16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "file_pages": [358, 386]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.085.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 23 camt.085.001.02 IntraBalanceMovementPendingReportV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp549–577; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 23 camt.085.001.02 IntraBalanceMovementPendingReportV02, Functionality, file p549.**

This IntraBalanceMovementPendingReport message is sent from a settlement infrastructure to an
account owner/request to report the intra-balance movement instructions, previously sent by the
account owner, that have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- - re-send to a third party a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementPendingReportV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. CashAccount
Account to or from which a cash entry is made.
E. CashAccountOwner
Party that owns the account.
F. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
G. Movements
Further details on the intrabalance movement transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 549 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00432.md) | 549–549 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00433.md) | 550–551 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00434.md) | 552–553 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00435.md) | 554–554 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.1 Identification &lt;Id&gt; / 23.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00436.md) | 555–555 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00437.md) | 556–556 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 23.4.3.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00438.md) | 557–557 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 23.4.3.7 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00439.md) | 558–558 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.5 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00440.md) | 559–559 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00441.md) | 560–561 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00442.md) | 562–562 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00443.md) | 563–564 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00444.md) | 565–565 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.2 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00445.md) | 566–566 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 23.4.7.2.8.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00446.md) | 567–567 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 23.4.7.2.8.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00447.md) | 568–568 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 23.4.7.2.8.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 23.4.7.2.8.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00448.md) | 569–569 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.9 BalanceTo &lt;BalTo&gt; / 23.4.7.2.9.1 Type &lt;Tp&gt; / 23.4.7.2.9.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00449.md) | 570–570 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.9 BalanceTo &lt;BalTo&gt; / 23.4.7.2.9.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 23.4.7.2.9.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00450.md) | 571–571 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.10 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00451.md) | 572–572 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.14 Linkages &lt;Lnkgs&gt; / 23.4.7.2.14.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00452.md) | 573–573 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.14 Linkages &lt;Lnkgs&gt; / 23.4.7.2.14.3 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00453.md) | 574–574 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.14 Linkages &lt;Lnkgs&gt; / 23.4.7.2.14.3 Reference &lt;Ref&gt; / 23.4.7.2.14.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00454.md) | 575–575 |
| [23 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 23.4 Message Building Blocks / 23.4.7 Movements &lt;Mvmnts&gt; / 23.4.7.2 Movement &lt;Mvmnt&gt; / 23.4.7.2.15 Priority &lt;Prty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00455.md) | 576–577 |

## src-000360 — 16 camt.085.001.02 IntraBalanceMovementPendingReportV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp358–386; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 16 camt.085.001.02 IntraBalanceMovementPendingReportV02, Functionality, file p358.**

This IntraBalanceMovementPendingReport message is sent from a settlement infrastructure to an
account owner/request to report the intra-balance movement instructions, previously sent by the
account owner, that have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- - re-send to a third party a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementPendingReportV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. CashAccount
Account to or from which a cash entry is made.
E. CashAccountOwner
Party that owns the account.
F. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
G. Movements
Further details on the intrabalance movement transactions.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
358 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00297.md) | 358–358 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00298.md) | 359–360 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00299.md) | 361–362 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00300.md) | 363–363 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.1 Identification &lt;Id&gt; / 16.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00301.md) | 364–364 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00302.md) | 365–365 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 16.4.3.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00303.md) | 366–366 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 16.4.3.7 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00304.md) | 367–367 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.5 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00305.md) | 368–368 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00306.md) | 369–370 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00307.md) | 371–371 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00308.md) | 372–373 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00309.md) | 374–374 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.2 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00310.md) | 375–375 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 16.4.7.2.8.1 Type &lt;Tp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00311.md) | 376–376 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 16.4.7.2.8.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00312.md) | 377–377 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.8 BalanceFrom &lt;BalFr&gt; / 16.4.7.2.8.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 16.4.7.2.8.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00313.md) | 378–378 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.9 BalanceTo &lt;BalTo&gt; / 16.4.7.2.9.1 Type &lt;Tp&gt; / 16.4.7.2.9.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00314.md) | 379–379 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.9 BalanceTo &lt;BalTo&gt; / 16.4.7.2.9.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 16.4.7.2.9.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00315.md) | 380–380 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.10 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00316.md) | 381–381 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.14 Linkages &lt;Lnkgs&gt; / 16.4.7.2.14.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00317.md) | 382–382 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.14 Linkages &lt;Lnkgs&gt; / 16.4.7.2.14.3 Reference &lt;Ref&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00318.md) | 383–383 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.14 Linkages &lt;Lnkgs&gt; / 16.4.7.2.14.3 Reference &lt;Ref&gt; / 16.4.7.2.14.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00319.md) | 384–384 |
| [16 camt.085.001.02 IntraBalanceMovementPendingReportV02 / 16.4 Message Building Blocks / 16.4.7 Movements &lt;Mvmnts&gt; / 16.4.7.2 Movement &lt;Mvmnt&gt; / 16.4.7.2.15 Priority &lt;Prty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00320.md) | 385–386 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000359-central-counterparty.md) | participant | src-000359 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories-csd.md) | participant | src-000359 |
| [Central Securities Depositories](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories.md) | participant | src-000359 |
| [Central Securities Depository](../../../../../shared/reference/participants/participant-src-000359-central-securities-depository.md) | participant | src-000359 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | participant | src-000359 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | participant | src-000359 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000359-national-central-bank-ncb.md) | participant | src-000359 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000359-national-central-bank.md) | participant | src-000359 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000359-payment-bank.md) | participant | src-000359 |
| [Servicing/Executing Party Instructing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | participant | src-000359 |
| [Servicing/Executing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | participant | src-000359 |
| [Settlement Infrastructure Direct Participant](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure-direct-participant.md) | participant | src-000359 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md) | participant | src-000359 |
| [Stock Exchange](../../../../../shared/reference/participants/participant-src-000359-stock-exchange.md) | participant | src-000359 |
| [System Member](../../../../../shared/reference/participants/participant-src-000359-system-member.md) | participant | src-000359 |
| [System Transaction Administrator](../../../../../shared/reference/participants/participant-src-000359-system-transaction-administrator.md) | participant | src-000359 |
| [T2S operator](../../../../../shared/reference/participants/participant-src-000359-t2s-operator.md) | participant | src-000359 |
| [Third Party](../../../../../shared/reference/participants/participant-src-000359-third-party.md) | participant | src-000359 |
| [Movement Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p158-movement-process.md) | business-flow | src-000359 |
| [Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p159-status-advice-process.md) | business-flow | src-000359 |
| [Confirmation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p160-confirmation-process.md) | business-flow | src-000359 |
| [Modification Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p161-modification-process.md) | business-flow | src-000359 |
| [Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p162-cancellation-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p164-modification-cancellation-status-advice-process.md) | business-flow | src-000359 |
| [Movement Querying Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p165-movement-querying-process.md) | business-flow | src-000359 |
| [Movement Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p166-movement-reporting-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Query and Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p169-modification-cancellation-query-and-report-process.md) | business-flow | src-000359 |
| [Pending Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p170-pending-reporting-process.md) | business-flow | src-000359 |
| [Posting Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p171-posting-reporting-process.md) | business-flow | src-000359 |
| [External Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) | business-flow | src-000359 |
| [Internal Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) | business-flow | src-000359 |
| [Intra-Balance Movement Modification/Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p197-intra-balance-movement-modification-cancellation-process.md) | business-flow | src-000359 |
| [Push Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) | business-flow | src-000359 |
| [Pull Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) | business-flow | src-000359 |
| [Intra-Balance Movement Pending/Posting Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p208-intra-balance-movement-pending-posting-report-process.md) | business-flow | src-000359 |
| [Intra-Balance Movement Query/Response Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p211-intra-balance-movement-query-response-process.md) | business-flow | src-000359 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
