---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.5 Equalisation4"]
file_pages: [4729]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.5 Equalisation4

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4729 to 4729.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4729

```text
66.1.26.5  Equalisation4
Definition: Part of an investor's subscription amount that is held by the fund in order to pay incentive /
performance fees at the end of the fiscal year.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C1, C13 4729
   Rate <Rate> [0..1] Rate 4730
   EqualisationMethodologyType <EqulstnMthdlgyTp> [0..1] CodeSet 4730
   ContingentLiquidationPerUnit <CntngntLqdtnPerUnit> [0..1] Amount C2, C10 4730
   DepreciationDepositPerUnit <DprctnDpstPerUnit> [0..1] Amount C2, C10 4731
   EqualisationCreditPerUnit <EqulstnCdtPerUnit> [0..1] Amount C2, C10 4731
   HighWatermark <HghWtrmrk> [0..1] Amount C2, C10 4732
   GrossAssetValue <GrssAsstVal> [0..1] Amount C2, C10 4732
Constraints
• ContingentLiquidationMethodologyTypeRule
Contingent Liquidation per Unit can only be used with Contingent Liquidation Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'ContingentLiquidation'
Following Must be True
    /DepreciationDepositPerUnit Must be absent
 And    /EqualisationCreditPerUnit Must be absent
• DepreciationDepositMethodologyTypeRule
Depreciation Deposit per Unit can only be used with Depreciation Deposit Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'DepreciationDeposit'
Following Must be True
    /ContingentLiquidationPerUnit Must be absent
 And    /EqualisationCreditPerUnit Must be absent
• EqualisationCreditMethodologyTypeRule
Equalisation Credit per Unit can only be used with Equalisation Credit Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'EqualisationCredit'
Following Must be True
    /ContingentLiquidationPerUnit Must be absent
 And    /DepreciationDepositPerUnit Must be absent
66.1.26.5.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the equalisation.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4729 May 2026
```

