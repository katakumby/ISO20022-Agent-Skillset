---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.8 TransactionOverhead <TxOvrhd>", "53.4.5.17.8.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [3635]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.8.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3635 to 3635.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3635

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
53.4.5.17.8.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
53.4.5.17.8.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C16 "FeeElementRule", C36 "StandardFeeAmountCalculation", C37
"StandardFeeRateCalculation"
IndividualFee <IndvFee> contains the following Fee9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  3636
{Or     Code <Cd> [1..1] CodeSet 3636
Or}     Proprietary <Prtry> [1..1] ± 3637
   Basis <Bsis> [0..1]  3637
{Or     Code <Cd> [1..1] CodeSet 3638
Or}     Proprietary <Prtry> [1..1] ± 3638
   StandardAmount <StdAmt> [0..1] Amount C2, C7 3638
   StandardRate <StdRate> [0..1] Rate 3639
   DiscountDetails <DscntDtls> [0..1]  C14 3639
     Amount <Amt> [0..1] Amount C2, C7 3639
     Rate <Rate> [0..1] Rate 3640
     Basis <Bsis> [0..1]  3640
{Or       Code <Cd> [1..1] CodeSet 3640
Or}       Proprietary <Prtry> [1..1] ± 3641
   RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3641
   RequestedRate <ReqdRate> [0..1] Rate 3641
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 3642
   RecipientIdentification <RcptId> [0..1] ± 3642
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3635 May 2026
```

