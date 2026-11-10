---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.15 TransactionOverhead <TxOvrhd>", "41.4.4.8.15.1 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [1748]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.15.1 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1748 to 1748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1748

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax,
DigitalNetworkFee) must be present.
41.4.4.8.15.1  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
41.4.4.8.15.2  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C18 "FeeElementRule", C36 "StandardFeeAmountCalculation", C37
"StandardFeeRateCalculation"
IndividualFee <IndvFee> contains the following Fee9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1749
{Or     Code <Cd> [1..1] CodeSet 1749
Or}     Proprietary <Prtry> [1..1] ± 1750
   Basis <Bsis> [0..1]  1750
{Or     Code <Cd> [1..1] CodeSet 1751
Or}     Proprietary <Prtry> [1..1] ± 1751
   StandardAmount <StdAmt> [0..1] Amount C3, C10 1751
   StandardRate <StdRate> [0..1] Rate 1752
   DiscountDetails <DscntDtls> [0..1]  C16 1752
     Amount <Amt> [0..1] Amount C3, C10 1752
     Rate <Rate> [0..1] Rate 1753
     Basis <Bsis> [0..1]  1753
{Or       Code <Cd> [1..1] CodeSet 1753
Or}       Proprietary <Prtry> [1..1] ± 1754
   RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 1754
   RequestedRate <ReqdRate> [0..1] Rate 1754
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1755
   RecipientIdentification <RcptId> [0..1] ± 1755
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1748 May 2026
```

