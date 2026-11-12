---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.083.001.02"
message_family: "camt.083"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.083.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "file_pages": [491, 521]}, {"source_id": "src-000360", "heading": "14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "file_pages": [300, 330]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.083.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 21 camt.083.001.02 IntraBalanceMovementCancellationReportV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp491–521; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 21 camt.083.001.02 IntraBalanceMovementCancellationReportV02, Functionality, file p491.**

The IntraBalanceMovementCancellationReport message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or current status values of the intra-balance movement
cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The IntraBalanceMovementCancellationReportV02 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. ReportOrError
Provides information on report or error resulting from the originating query message.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 491 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00384.md) | 491–491 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00385.md) | 492–493 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00386.md); [Constraints continuation C19–C22 (file p496)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00387.md#file-page-496) | 494–495 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00387.md) | 496–496 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.1 Identification &lt;Id&gt; / 21.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00388.md) | 497–497 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.1 Identification &lt;Id&gt; / 21.4.1.5 MessageRecipient &lt;MsgRcpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00389.md) | 498–498 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 21.4.3.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00390.md) | 499–499 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 21.4.3.5 ReportPeriod &lt;RptPrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00391.md) | 500–500 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 21.4.3.9 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00392.md) | 501–502 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00393.md) | 503–504 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00394.md) | 505–505 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00395.md) | 506–506 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.4 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00396.md) | 507–508 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00397.md) | 509–509 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.3 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00398.md) | 510–510 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.5 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00399.md) | 511–511 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.7 TransactionIdentification &lt;TxId&gt; / 21.4.4.1.5.7.2 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00400.md) | 512–513 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00401.md) | 514–514 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 21.4.4.1.5.8.3.1 Type &lt;Tp&gt; / 21.4.4.1.5.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00402.md) | 515–515 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 21.4.4.1.5.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 21.4.4.1.5.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00403.md) | 516–516 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00404.md) | 517–517 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 21.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00405.md) | 518–518 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 21.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 21.4.4.1.5.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00406.md) | 519–519 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.1 Cancellations &lt;Cxls&gt; / 21.4.4.1.5 Cancellation &lt;Cxl&gt; / 21.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 21.4.4.1.5.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00407.md) | 520–520 |
| [21 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 21.4 Message Building Blocks / 21.4.4 ReportOrError &lt;RptOrErr&gt; / 21.4.4.2 OperationalError &lt;OprlErr&gt; / 21.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00408.md) | 521–521 |

## src-000360 — 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp300–330; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02, Functionality, file p300.**

The IntraBalanceMovementCancellationReport message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or current status values of the intra-balance movement
cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The IntraBalanceMovementCancellationReportV02 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. ReportOrError
Provides information on report or error resulting from the originating query message.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
300 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00249.md) | 300–300 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00250.md) | 301–302 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00251.md); [Constraints continuation C19–C22 (file p305)](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00252.md#file-page-305) | 303–304 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00252.md) | 305–305 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.1 Identification &lt;Id&gt; / 14.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00253.md) | 306–306 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.1 Identification &lt;Id&gt; / 14.4.1.5 MessageRecipient &lt;MsgRcpt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00254.md) | 307–307 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 14.4.3.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00255.md) | 308–308 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 14.4.3.5 ReportPeriod &lt;RptPrd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00256.md) | 309–309 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 14.4.3.9 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00257.md) | 310–311 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00258.md) | 312–313 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00259.md) | 314–314 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00260.md) | 315–315 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.4 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00261.md) | 316–317 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00262.md) | 318–318 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.3 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00263.md) | 319–319 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.5 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00264.md) | 320–320 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.7 TransactionIdentification &lt;TxId&gt; / 14.4.4.1.5.7.2 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00265.md) | 321–322 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00266.md) | 323–323 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 14.4.4.1.5.8.3.1 Type &lt;Tp&gt; / 14.4.4.1.5.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00267.md) | 324–324 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 14.4.4.1.5.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 14.4.4.1.5.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00268.md) | 325–325 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00269.md) | 326–326 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 14.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00270.md) | 327–327 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 14.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 14.4.4.1.5.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00271.md) | 328–328 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.1 Cancellations &lt;Cxls&gt; / 14.4.4.1.5 Cancellation &lt;Cxl&gt; / 14.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 14.4.4.1.5.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00272.md) | 329–329 |
| [14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 / 14.4 Message Building Blocks / 14.4.4 ReportOrError &lt;RptOrErr&gt; / 14.4.4.2 OperationalError &lt;OprlErr&gt; / 14.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00273.md) | 330–330 |

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
