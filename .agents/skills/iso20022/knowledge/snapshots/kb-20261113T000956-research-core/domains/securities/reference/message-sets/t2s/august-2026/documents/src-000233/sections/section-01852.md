---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.5 SettlementParameters <SttlmParams>", "72.4.3.4.18.5.20 SettlementSystemMethod <SttlmSysMtd>"]
file_pages: [2545]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.5.20 SettlementSystemMethod <SttlmSysMtd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2545 to 2545.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2545

```text
72.4.3.4.18.5.20  SettlementSystemMethod <SttlmSysMtd>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
SettlementSystemMethod <SttlmSysMtd> contains one of the following elements (see
"SettlementSystemMethod4Choice" on page 2977 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2977
Or}   Proprietary <Prtry> [1..1] ± 2977
72.4.3.4.18.5.21  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 3010 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3011
Or}   Proprietary <Prtry> [1..1] ± 3011
72.4.3.4.18.5.22  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
72.4.3.4.18.5.23  Tracking <Trckg>
Presence: [0..1]
Definition: Specifies whether the loan and/or collateral is tracked.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2545 August 2026
```

