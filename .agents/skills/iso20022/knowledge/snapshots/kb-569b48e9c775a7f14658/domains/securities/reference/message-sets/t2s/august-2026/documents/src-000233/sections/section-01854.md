---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.5 SettlementParameters <SttlmParams>", "72.4.3.4.18.5.28 EligibleForCollateral <ElgblForColl>"]
file_pages: [2547]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.5.28 EligibleForCollateral <ElgblForColl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2547 to 2547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2547

```text
ModificationCancellationAllowed <ModCxlAllwd> contains one of the following elements (see
"ModificationCancellationAllowed4Choice" on page 3023 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 3023
Or}   Proprietary <Prtry> [1..1] ± 3023
72.4.3.4.18.5.28  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
72.4.3.4.18.5.29  SecuritiesSubBalanceType <SctiesSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
SecuritiesSubBalanceType <SctiesSubBalTp> contains the following elements (see
"GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
72.4.3.4.18.5.30  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the cash sub balance type indicator (example restriction type for a market
infrastructure).
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
72.4.3.4.18.6  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2547 August 2026
```

