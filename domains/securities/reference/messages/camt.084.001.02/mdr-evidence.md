---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.084.001.02"
message_family: "camt.084"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.084.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "file_pages": [522, 548]}, {"source_id": "src-000360", "heading": "15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "file_pages": [331, 357]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.084.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 22 camt.084.001.02 IntraBalanceMovementPostingReportV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp522–548; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 22 camt.084.001.02 IntraBalanceMovementPostingReportV02, Functionality, file p522.**

This IntraBalanceMovementPostingReport message is sent from a settlement infrastructure to an
account owner/requestor to report the intra-balance movement instructions, previously sent by the
account owner, that have a settled status.
The message may also be used to:
- - re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- - provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- - re-send to a third party a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementPostingReportV02 MessageDefinition is composed of 7
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
G. SubBalance
Identifies the transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 522 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00409.md) | 522–522 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00410.md) | 523–524 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00411.md) | 525–526 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00412.md) | 527–527 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.1 Identification &lt;Id&gt; / 22.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00413.md) | 528–528 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00414.md) | 529–529 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 22.4.3.3 ReportIdentification &lt;RptId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00415.md) | 530–530 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 22.4.3.8 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00416.md) | 531–531 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.5 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00417.md) | 532–533 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00418.md) | 534–534 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.1 BalanceFrom &lt;BalFr&gt; / 22.4.7.1.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00419.md) | 535–535 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.1 BalanceFrom &lt;BalFr&gt; / 22.4.7.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00420.md) | 536–536 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.1 BalanceFrom &lt;BalFr&gt; / 22.4.7.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 22.4.7.1.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00421.md) | 537–538 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00422.md) | 539–539 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00423.md) | 540–540 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.7 BalanceTo &lt;BalTo&gt; / 22.4.7.2.7.1 Type &lt;Tp&gt; / 22.4.7.2.7.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00424.md) | 541–541 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.7 BalanceTo &lt;BalTo&gt; / 22.4.7.2.7.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 22.4.7.2.7.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00425.md) | 542–542 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.9 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00426.md) | 543–543 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.13 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00427.md) | 544–544 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.14 Linkages &lt;Lnkgs&gt; / 22.4.7.2.14.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00428.md) | 545–545 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.14 Linkages &lt;Lnkgs&gt; / 22.4.7.2.14.3 Reference &lt;Ref&gt; / 22.4.7.2.14.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00429.md) | 546–546 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.14 Linkages &lt;Lnkgs&gt; / 22.4.7.2.14.3 Reference &lt;Ref&gt; / 22.4.7.2.14.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00430.md) | 547–547 |
| [22 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 22.4 Message Building Blocks / 22.4.7 SubBalance &lt;SubBal&gt; / 22.4.7.2 Movement &lt;Mvmnt&gt; / 22.4.7.2.17 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00431.md) | 548–548 |

## src-000360 — 15 camt.084.001.02 IntraBalanceMovementPostingReportV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp331–357; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 15 camt.084.001.02 IntraBalanceMovementPostingReportV02, Functionality, file p331.**

This IntraBalanceMovementPostingReport message is sent from a settlement infrastructure to an
account owner/requestor to report the intra-balance movement instructions, previously sent by the
account owner, that have a settled status.
The message may also be used to:
- - re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- - provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- - re-send to a third party a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementPostingReportV02 MessageDefinition is composed of 7
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
G. SubBalance
Identifies the transactions.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
331 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00274.md) | 331–331 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00275.md) | 332–333 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00276.md) | 334–335 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00277.md) | 336–336 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.1 Identification &lt;Id&gt; / 15.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00278.md) | 337–337 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00279.md) | 338–338 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 15.4.3.3 ReportIdentification &lt;RptId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00280.md) | 339–339 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 15.4.3.8 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00281.md) | 340–340 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.5 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00282.md) | 341–342 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00283.md) | 343–343 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.1 BalanceFrom &lt;BalFr&gt; / 15.4.7.1.1 Type &lt;Tp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00284.md) | 344–344 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.1 BalanceFrom &lt;BalFr&gt; / 15.4.7.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00285.md) | 345–345 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.1 BalanceFrom &lt;BalFr&gt; / 15.4.7.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 15.4.7.1.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00286.md) | 346–347 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00287.md) | 348–348 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00288.md) | 349–349 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.7 BalanceTo &lt;BalTo&gt; / 15.4.7.2.7.1 Type &lt;Tp&gt; / 15.4.7.2.7.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00289.md) | 350–350 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.7 BalanceTo &lt;BalTo&gt; / 15.4.7.2.7.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 15.4.7.2.7.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00290.md) | 351–351 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.9 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00291.md) | 352–352 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.13 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00292.md) | 353–353 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.14 Linkages &lt;Lnkgs&gt; / 15.4.7.2.14.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00293.md) | 354–354 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.14 Linkages &lt;Lnkgs&gt; / 15.4.7.2.14.3 Reference &lt;Ref&gt; / 15.4.7.2.14.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00294.md) | 355–355 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.14 Linkages &lt;Lnkgs&gt; / 15.4.7.2.14.3 Reference &lt;Ref&gt; / 15.4.7.2.14.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00295.md) | 356–356 |
| [15 camt.084.001.02 IntraBalanceMovementPostingReportV02 / 15.4 Message Building Blocks / 15.4.7 SubBalance &lt;SubBal&gt; / 15.4.7.2 Movement &lt;Mvmnt&gt; / 15.4.7.2.17 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00296.md) | 357–357 |

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
