---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.9 TransactionOverhead <TxOvrhd>", "53.4.5.16.9.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [3567]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.9.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3567 to 3567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3567

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
53.4.5.16.9.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
53.4.5.16.9.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C16 "FeeElementRule", C36 "StandardFeeAmountCalculation", C37
"StandardFeeRateCalculation"
IndividualFee <IndvFee> contains the following Fee9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  3568
{Or     Code <Cd> [1..1] CodeSet 3568
Or}     Proprietary <Prtry> [1..1] ± 3569
   Basis <Bsis> [0..1]  3569
{Or     Code <Cd> [1..1] CodeSet 3570
Or}     Proprietary <Prtry> [1..1] ± 3570
   StandardAmount <StdAmt> [0..1] Amount C2, C7 3570
   StandardRate <StdRate> [0..1] Rate 3571
   DiscountDetails <DscntDtls> [0..1]  C14 3571
     Amount <Amt> [0..1] Amount C2, C7 3571
     Rate <Rate> [0..1] Rate 3572
     Basis <Bsis> [0..1]  3572
{Or       Code <Cd> [1..1] CodeSet 3572
Or}       Proprietary <Prtry> [1..1] ± 3573
   RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3573
   RequestedRate <ReqdRate> [0..1] Rate 3573
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 3574
   RecipientIdentification <RcptId> [0..1] ± 3574
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3567 May 2026
```

