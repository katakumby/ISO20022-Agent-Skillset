---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.033.001.01"
message_family: "semt.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.033.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "file_pages": [2700, 2723]}, {"source_id": "src-000381", "heading": "7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "file_pages": [145, 168]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.033.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2700–2723; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01, Functionality, file p2700.**

The SecuritiesTransactionCancellationRequestReport message is sent from a settlement infrastructure
to an account owner/requestor to provide full details or current status values of settlement or the intra-
position movement cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The SecuritiesTransactionCancellationRequestReportV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Cancellations
Report on the transaction cancellation requests.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2700 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01980.md) | 2700–2700 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01981.md) | 2701–2701 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01982.md); [Constraints continuation C14–C23 (file p2704)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01983.md#file-page-2704) | 2702–2703 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01983.md) | 2704–2704 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01984.md) | 2705–2705 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 78.4.2.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01985.md) | 2706–2706 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 78.4.2.7 Frequency &lt;Frqcy&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01986.md) | 2707–2708 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01987.md) | 2709–2709 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01988.md) | 2710–2711 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01989.md) | 2712–2712 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.4 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01990.md) | 2713–2713 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.6 TransactionIdentification &lt;TxId&gt; / 78.4.3.4.6.2 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01991.md) | 2714–2714 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01992.md) | 2715–2715 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 78.4.3.4.7.1.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01993.md) | 2716–2716 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 78.4.3.4.7.1.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01994.md) | 2717–2717 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 78.4.3.4.7.1.5 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01995.md) | 2718–2718 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 78.4.3.4.7.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01996.md) | 2719–2719 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 78.4.3.4.7.2.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01997.md) | 2720–2720 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 78.4.3.4.7.2.4 TradeDate &lt;TradDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01998.md) | 2721–2721 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.3 Cancellations &lt;Cxls&gt; / 78.4.3.4 Cancellation &lt;Cxl&gt; / 78.4.3.4.7 Underlying &lt;Undrlyg&gt; / 78.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 78.4.3.4.7.2.7 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01999.md) | 2722–2722 |
| [78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 78.4 Message Building Blocks / 78.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02000.md) | 2723–2723 |

## src-000381 — 7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01

[src-000381](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp145–168; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01, Functionality, file p145.**

The SecuritiesTransactionCancellationRequestReport message is sent from a settlement infrastructure
to an account owner/requestor to provide full details or current status values of settlement or the intra-
position movement cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The SecuritiesTransactionCancellationRequestReportV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Cancellations
Report on the transaction cancellation requests.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 145 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00116.md) | 145–145 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00117.md) | 146–146 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00118.md); [Constraints continuation C14–C23 (file p149)](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00119.md#file-page-149) | 147–148 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00119.md) | 149–149 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00120.md) | 150–150 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 7.4.2.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00121.md) | 151–151 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 7.4.2.7 Frequency &lt;Frqcy&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00122.md) | 152–153 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00123.md) | 154–154 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00124.md) | 155–156 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00125.md) | 157–157 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.4 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00126.md) | 158–158 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.6 TransactionIdentification &lt;TxId&gt; / 7.4.3.4.6.2 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00127.md) | 159–159 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00128.md) | 160–160 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.3.4.7.1.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00129.md) | 161–161 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.3.4.7.1.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00130.md) | 162–162 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.3.4.7.1.5 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00131.md) | 163–163 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 7.4.3.4.7.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00132.md) | 164–164 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 7.4.3.4.7.2.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00133.md) | 165–165 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 7.4.3.4.7.2.4 TradeDate &lt;TradDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00134.md) | 166–166 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.3 Cancellations &lt;Cxls&gt; / 7.4.3.4 Cancellation &lt;Cxl&gt; / 7.4.3.4.7 Underlying &lt;Undrlyg&gt; / 7.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 7.4.3.4.7.2.7 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00135.md) | 167–167 |
| [7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01 / 7.4 Message Building Blocks / 7.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00136.md) | 168–168 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000380-central-counterparty.md) | participant | src-000380 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md) | participant | src-000380 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md) | participant | src-000380 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | participant | src-000380 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | participant | src-000380 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md) | participant | src-000380 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000380-t2s-operator.md) | participant | src-000380 |
| [Query Report Process](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p253-query-report-process.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) | business-flow | src-000380 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
