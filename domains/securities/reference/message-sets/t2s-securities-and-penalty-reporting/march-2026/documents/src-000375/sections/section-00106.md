---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.20 SettlementSystemMethod <SttlmSysMtd>"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.20 SettlementSystemMethod <SttlmSysMtd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
4.4.3.4.18.5.20  SettlementSystemMethod <SttlmSysMtd>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
SettlementSystemMethod <SttlmSysMtd> contains one of the following elements (see
"SettlementSystemMethod4Choice" on page 362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 362
Or}   Proprietary <Prtry> [1..1] ± 362
4.4.3.4.18.5.21  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 374 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 375
Or}   Proprietary <Prtry> [1..1] ± 375
4.4.3.4.18.5.22  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 352 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
4.4.3.4.18.5.23  Tracking <Trckg>
Presence: [0..1]
Definition: Specifies whether the loan and/or collateral is tracked.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 149 March 2026
```

