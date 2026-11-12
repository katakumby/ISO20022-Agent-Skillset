---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.19 Equalisation3", "66.1.26.19.2 Rate <Rate>"]
file_pages: [4769]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.19.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4769 to 4769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4769

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.19.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used for calculation of the equalisation.
Datatype: "PercentageRate" on page 5401
66.1.26.19.3  EqualisationMethodologyType <EqulstnMthdlgyTp>
Presence: [0..2]
Definition: Methodology used for the allocation of the performance fees.
EqualisationMethodologyType <EqulstnMthdlgyTp> contains the following
EqualisationMethodologyType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
66.1.26.19.3.1  EqualisationMethodologyTypeCode <EqulstnMthdlgyTpCd>
Presence: [1..1]
Definition: Methodology used for the allocation of the performance fees.
Datatype: "EqualisationMethodologyType1Code" on page 5296
CodeName Name Definition
COLI ContingentLiquidation Mandatory redemption of units
processed either at redemption or
crystallization, whose proceeds are due
to the asset manager as performance
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4769 May 2026
```

