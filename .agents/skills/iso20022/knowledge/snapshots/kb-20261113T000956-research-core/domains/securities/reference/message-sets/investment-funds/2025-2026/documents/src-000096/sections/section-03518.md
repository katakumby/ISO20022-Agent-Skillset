---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.19 Equalisation3", "66.1.26.19.1 Amount <Amt>"]
file_pages: [4768]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.19.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4768 to 4768.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4768

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C1, C13 4768
   Rate <Rate> [0..1] Rate 4769
   EqualisationMethodologyType <EqulstnMthdlgyTp> [0..2]  4769
     EqualisationMethodologyTypeCode
<EqulstnMthdlgyTpCd>
[1..1] CodeSet 4769
     RelatedSubscription <RltdSbcpt> [0..*]  4770
       Reference <Ref> [1..1] ± 4770
       RelatedQuantity <RltdQty> [0..1] Quantity 4771
       RelatedAmount <RltdAmt> [0..1] Amount C2, C10 4771
       ContingentLiquidationPerUnit <CntngntLqdtnPerUnit> [0..1] Amount C2, C10 4771
       DepreciationDepositPerUnit <DprctnDpstPerUnit> [0..1] Amount C2, C10 4771
       EqualisationCreditPerUnit <EqulstnCdtPerUnit> [0..1] Amount C2, C10 4772
   HighWatermark <HghWtrmrk> [0..1] Amount C2, C10 4772
   GrossAssetValue <GrssAsstVal> [0..1] Amount C2, C10 4773
Constraints
• RedemptionEqualisationMethodologyTypes1Rule
Contingent Liquidation and Depreciation Deposit are mutually exclusive.
On Condition
    /EqualisationMethodologyType[*]/EqualisationMethodologyTypeCode is equal to 
value 'ContingentLiquidation'
Following Must be True
    /EqualisationMethodologyType[*]/RelatedSubscription[*]/
DepreciationDepositPerUnit Must be absent
• RedemptionEqualisationMethodologyTypes2Rule
Contingent Liquidation and Depreciation Deposit are mutually exclusive.
On Condition
    /EqualisationMethodologyType[*]/EqualisationMethodologyTypeCode is equal to 
value 'DepreciationDeposit'
Following Must be True
    /EqualisationMethodologyType[*]/RelatedSubscription[*]/
ContingentLiquidationPerUnit Must be absent
66.1.26.19.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of money resulting from the calculation of the equalisation.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4768 May 2026
```

