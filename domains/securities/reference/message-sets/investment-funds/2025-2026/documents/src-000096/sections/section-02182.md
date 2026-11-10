---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.16 TransactionOverhead <TxOvrhd>", "50.4.4.9.16.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [3073]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.16.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3073 to 3073.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3073

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
50.4.4.9.16.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
50.4.4.9.16.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C18 "FeeElementRule", C36 "StandardFeeAmountCalculation", C37
"StandardFeeRateCalculation"
IndividualFee <IndvFee> contains the following Fee9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  3074
{Or     Code <Cd> [1..1] CodeSet 3074
Or}     Proprietary <Prtry> [1..1] ± 3075
   Basis <Bsis> [0..1]  3075
{Or     Code <Cd> [1..1] CodeSet 3076
Or}     Proprietary <Prtry> [1..1] ± 3076
   StandardAmount <StdAmt> [0..1] Amount C3, C10 3076
   StandardRate <StdRate> [0..1] Rate 3077
   DiscountDetails <DscntDtls> [0..1]  C16 3077
     Amount <Amt> [0..1] Amount C3, C10 3077
     Rate <Rate> [0..1] Rate 3078
     Basis <Bsis> [0..1]  3078
{Or       Code <Cd> [1..1] CodeSet 3078
Or}       Proprietary <Prtry> [1..1] ± 3079
   RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 3079
   RequestedRate <ReqdRate> [0..1] Rate 3079
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 3080
   RecipientIdentification <RcptId> [0..1] ± 3080
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3073 May 2026
```

