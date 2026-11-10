---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.16 TransactionOverhead <TxOvrhd>", "47.4.4.8.16.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [2593]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.16.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2593 to 2593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2593

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
47.4.4.8.16.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
47.4.4.8.16.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C18 "FeeElementRule", C36 "StandardFeeAmountCalculation", C37
"StandardFeeRateCalculation"
IndividualFee <IndvFee> contains the following Fee9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2594
{Or     Code <Cd> [1..1] CodeSet 2594
Or}     Proprietary <Prtry> [1..1] ± 2595
   Basis <Bsis> [0..1]  2595
{Or     Code <Cd> [1..1] CodeSet 2596
Or}     Proprietary <Prtry> [1..1] ± 2596
   StandardAmount <StdAmt> [0..1] Amount C3, C10 2596
   StandardRate <StdRate> [0..1] Rate 2597
   DiscountDetails <DscntDtls> [0..1]  C16 2597
     Amount <Amt> [0..1] Amount C3, C10 2597
     Rate <Rate> [0..1] Rate 2598
     Basis <Bsis> [0..1]  2598
{Or       Code <Cd> [1..1] CodeSet 2598
Or}       Proprietary <Prtry> [1..1] ± 2599
   RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2599
   RequestedRate <ReqdRate> [0..1] Rate 2599
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 2600
   RecipientIdentification <RcptId> [0..1] ± 2600
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2593 May 2026
```

