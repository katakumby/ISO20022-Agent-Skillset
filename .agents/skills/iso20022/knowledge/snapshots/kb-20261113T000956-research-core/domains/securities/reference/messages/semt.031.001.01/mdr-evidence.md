---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.031.001.01"
message_family: "semt.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.031.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "file_pages": [2652, 2688]}, {"source_id": "src-000381", "heading": "5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "file_pages": [97, 133]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.031.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2652–2688; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01, Functionality, file p2652.**

The SecuritiesSettlementConditionsModificationRequestReport message is sent from a settlement
infrastructure to an account owner/requestor to provide full details or current status values of the
settlement or intra-position movement modification request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The SecuritiesSettlementConditionsModificationRequestReportV01 MessageDefinition is composed of
4 MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Modifications
Report on the condition modifications requests.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2652 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01940.md) | 2652–2652 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01941.md) | 2653–2654 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01942.md); [Constraints continuation C27–C29 (file p2658)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01943.md#file-page-2658) | 2655–2657 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01943.md) | 2658–2658 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 76.4.2.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01944.md) | 2659–2659 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 76.4.2.3 ReportIdentification &lt;RptId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01945.md) | 2660–2660 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 76.4.2.8 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01946.md) | 2661–2663 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01947.md) | 2664–2664 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01948.md) | 2665–2667 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01949.md) | 2668–2668 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.4 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01950.md) | 2669–2670 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.1 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01951.md) | 2671–2671 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.1 Reference &lt;Ref&gt; / 76.4.3.4.6.1.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01952.md) | 2672–2672 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.1 Reference &lt;Ref&gt; / 76.4.3.4.6.1.7 CommonIdentification &lt;CmonId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01953.md) | 2673–2673 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.6 Priority &lt;Prty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01954.md) | 2674–2674 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.9 SecuritiesRTGS &lt;SctiesRTGS&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01955.md) | 2675–2675 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.13 Linkages &lt;Lnkgs&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01956.md) | 2676–2676 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 76.4.3.4.6.13.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01957.md) | 2677–2677 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 76.4.3.4.6.13.3 Reference &lt;Ref&gt; / 76.4.3.4.6.13.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01958.md) | 2678–2678 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 76.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 76.4.3.4.6.13.3 Reference &lt;Ref&gt; / 76.4.3.4.6.13.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01959.md) | 2679–2679 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01960.md) | 2680–2680 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 76.4.3.4.7.1.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01961.md) | 2681–2681 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 76.4.3.4.7.1.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01962.md) | 2682–2682 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 76.4.3.4.7.1.5 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01963.md) | 2683–2683 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 76.4.3.4.7.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01964.md) | 2684–2684 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 76.4.3.4.7.2.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01965.md) | 2685–2685 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 76.4.3.4.7.2.4 TradeDate &lt;TradDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01966.md) | 2686–2686 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.3 Modifications &lt;Mods&gt; / 76.4.3.4 Modification &lt;Mod&gt; / 76.4.3.4.7 Underlying &lt;Undrlyg&gt; / 76.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 76.4.3.4.7.2.7 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01967.md) | 2687–2687 |
| [76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 76.4 Message Building Blocks / 76.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01968.md) | 2688–2688 |

## src-000381 — 5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01

[src-000381](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp97–133; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01, Functionality, file p97.**

The SecuritiesSettlementConditionsModificationRequestReport message is sent from a settlement
infrastructure to an account owner/requestor to provide full details or current status values of the
settlement or intra-position movement modification request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The SecuritiesSettlementConditionsModificationRequestReportV01 MessageDefinition is composed of
4 MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Modifications
Report on the condition modifications requests.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 97 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00076.md) | 97–97 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00077.md) | 98–99 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00078.md); [Constraints continuation C27–C29 (file p103)](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00079.md#file-page-103) | 100–102 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00079.md) | 103–103 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 5.4.2.1 ReportNumber &lt;RptNb&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00080.md) | 104–104 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 5.4.2.3 ReportIdentification &lt;RptId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00081.md) | 105–105 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 5.4.2.8 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00082.md) | 106–108 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00083.md) | 109–109 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00084.md) | 110–112 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00085.md) | 113–113 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.4 RequestReference &lt;ReqRef&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00086.md) | 114–115 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.1 Reference &lt;Ref&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00087.md) | 116–116 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.1 Reference &lt;Ref&gt; / 5.4.3.4.6.1.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00088.md) | 117–117 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.1 Reference &lt;Ref&gt; / 5.4.3.4.6.1.7 CommonIdentification &lt;CmonId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00089.md) | 118–118 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.6 Priority &lt;Prty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00090.md) | 119–119 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.9 SecuritiesRTGS &lt;SctiesRTGS&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00091.md) | 120–120 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.13 Linkages &lt;Lnkgs&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00092.md) | 121–121 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 5.4.3.4.6.13.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00093.md) | 122–122 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 5.4.3.4.6.13.3 Reference &lt;Ref&gt; / 5.4.3.4.6.13.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00094.md) | 123–123 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.6 RequestDetails &lt;ReqDtls&gt; / 5.4.3.4.6.13 Linkages &lt;Lnkgs&gt; / 5.4.3.4.6.13.3 Reference &lt;Ref&gt; / 5.4.3.4.6.13.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00095.md) | 124–124 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00096.md) | 125–125 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 5.4.3.4.7.1.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00097.md) | 126–126 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 5.4.3.4.7.1.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00098.md) | 127–127 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.1 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 5.4.3.4.7.1.5 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00099.md) | 128–128 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 5.4.3.4.7.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00100.md) | 129–129 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 5.4.3.4.7.2.2 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00101.md) | 130–130 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 5.4.3.4.7.2.4 TradeDate &lt;TradDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00102.md) | 131–131 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.3 Modifications &lt;Mods&gt; / 5.4.3.4 Modification &lt;Mod&gt; / 5.4.3.4.7 Underlying &lt;Undrlyg&gt; / 5.4.3.4.7.2 SettlementTransaction &lt;SttlmTx&gt; / 5.4.3.4.7.2.7 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00103.md) | 132–132 |
| [5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01 / 5.4 Message Building Blocks / 5.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00104.md) | 133–133 |

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
