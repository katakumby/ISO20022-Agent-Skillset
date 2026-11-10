---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.081.001.02"
message_family: "camt.081"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.081.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "file_pages": [436, 476]}, {"source_id": "src-000360", "heading": "12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "file_pages": [245, 285]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.081.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 19 camt.081.001.02 IntraBalanceMovementModificationReportV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp436–476; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 19 camt.081.001.02 IntraBalanceMovementModificationReportV02, Functionality, file p436.**

The IntraBalanceMovementModificationReport message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or current status values of the intra-balance movement
modification request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The IntraBalanceMovementModificationReportV02 MessageDefinition is composed of 5
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
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 436 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00339.md) | 436–436 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00340.md) | 437–439 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00341.md) | 440–441 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00342.md) | 442–442 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.1 Identification &lt;Id&gt; / 19.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00343.md) | 443–443 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00344.md) | 444–444 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 19.4.3.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00345.md) | 445–445 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 19.4.3.6 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00346.md) | 446–446 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00347.md) | 447–449 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00348.md) | 450–452 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00349.md) | 453–453 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00350.md) | 454–454 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00351.md) | 455–456 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00352.md) | 457–457 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00353.md) | 458–458 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.4 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00354.md) | 459–459 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.6 StatusDate &lt;StsDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00355.md) | 460–461 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.1 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00356.md) | 462–462 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.1 Reference &lt;Ref&gt; / 19.4.4.1.5.7.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00357.md) | 463–463 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.6 ClearingChannel &lt;ClrChanl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00358.md) | 464–464 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 19.4.4.1.5.7.7.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00359.md) | 465–465 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 19.4.4.1.5.7.7.3 Reference &lt;Ref&gt; / 19.4.4.1.5.7.7.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00360.md) | 466–466 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 19.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 19.4.4.1.5.7.7.3 Reference &lt;Ref&gt; / 19.4.4.1.5.7.7.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00361.md) | 467–468 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00362.md) | 469–469 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 19.4.4.1.5.8.3.1 Type &lt;Tp&gt; / 19.4.4.1.5.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00363.md) | 470–470 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 19.4.4.1.5.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 19.4.4.1.5.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00364.md) | 471–471 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00365.md) | 472–472 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 19.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00366.md) | 473–473 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 19.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 19.4.4.1.5.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00367.md) | 474–474 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.1 Modifications &lt;Mods&gt; / 19.4.4.1.5 Modification &lt;Mod&gt; / 19.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 19.4.4.1.5.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00368.md) | 475–475 |
| [19 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 19.4 Message Building Blocks / 19.4.4 ReportOrError &lt;RptOrErr&gt; / 19.4.4.2 OperationalError &lt;OprlErr&gt; / 19.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00369.md) | 476–476 |

## src-000360 — 12 camt.081.001.02 IntraBalanceMovementModificationReportV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp245–285; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 12 camt.081.001.02 IntraBalanceMovementModificationReportV02, Functionality, file p245.**

The IntraBalanceMovementModificationReport message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or current status values of the intra-balance movement
modification request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The IntraBalanceMovementModificationReportV02 MessageDefinition is composed of 5
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
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
245 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00204.md) | 245–245 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00205.md) | 246–248 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00206.md) | 249–250 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00207.md) | 251–251 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.1 Identification &lt;Id&gt; / 12.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00208.md) | 252–252 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00209.md) | 253–253 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 12.4.3.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00210.md) | 254–254 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 12.4.3.6 QueryType &lt;QryTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00211.md) | 255–255 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00212.md) | 256–258 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00213.md) | 259–261 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00214.md) | 262–262 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00215.md) | 263–263 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00216.md) | 264–265 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00217.md) | 266–266 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00218.md) | 267–267 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.4 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00219.md) | 268–268 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.6 StatusDate &lt;StsDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00220.md) | 269–270 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.1 Reference &lt;Ref&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00221.md) | 271–271 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.1 Reference &lt;Ref&gt; / 12.4.4.1.5.7.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00222.md) | 272–272 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.6 ClearingChannel &lt;ClrChanl&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00223.md) | 273–273 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 12.4.4.1.5.7.7.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00224.md) | 274–274 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 12.4.4.1.5.7.7.3 Reference &lt;Ref&gt; / 12.4.4.1.5.7.7.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00225.md) | 275–275 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.7 RequestDetails &lt;ReqDtls&gt; / 12.4.4.1.5.7.7 Linkages &lt;Lnkgs&gt; / 12.4.4.1.5.7.7.3 Reference &lt;Ref&gt; / 12.4.4.1.5.7.7.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00226.md) | 276–277 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00227.md) | 278–278 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 12.4.4.1.5.8.3.1 Type &lt;Tp&gt; / 12.4.4.1.5.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00228.md) | 279–279 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.3 BalanceFrom &lt;BalFr&gt; / 12.4.4.1.5.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 12.4.4.1.5.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00229.md) | 280–280 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00230.md) | 281–281 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 12.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00231.md) | 282–282 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.4 BalanceTo &lt;BalTo&gt; / 12.4.4.1.5.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 12.4.4.1.5.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00232.md) | 283–283 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.1 Modifications &lt;Mods&gt; / 12.4.4.1.5 Modification &lt;Mod&gt; / 12.4.4.1.5.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.4.1.5.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00233.md) | 284–284 |
| [12 camt.081.001.02 IntraBalanceMovementModificationReportV02 / 12.4 Message Building Blocks / 12.4.4 ReportOrError &lt;RptOrErr&gt; / 12.4.4.2 OperationalError &lt;OprlErr&gt; / 12.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00234.md) | 285–285 |

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
