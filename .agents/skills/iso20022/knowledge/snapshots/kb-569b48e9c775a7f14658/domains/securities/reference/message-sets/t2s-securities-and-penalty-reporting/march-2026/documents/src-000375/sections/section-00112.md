---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.14 PreviouslySettledQuantity <PrevslySttldQty>"]
file_pages: [155]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.14 PreviouslySettledQuantity <PrevslySttldQty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 155 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
4.4.3.4.18.14  PreviouslySettledQuantity <PrevslySttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument previously settled.
PreviouslySettledQuantity <PrevslySttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
4.4.3.4.18.15  RemainingToBeSettledQuantity <RmngToBeSttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument remaining to be settled.
RemainingToBeSettledQuantity <RmngToBeSttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
4.4.3.4.18.16  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C19 "NumberRule"
Datatype: "Max3Number" on page 554
Constraints
• NumberRule
If Number is negative, then Sign must be present.
4.4.3.4.18.17  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 155 March 2026
```

