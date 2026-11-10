---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.8 TransactionOverhead <TxOvrhd>", "30.4.7.16.8.5 IndividualFee <IndvFee>"]
file_pages: [730]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 730 to 730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 730

```text
30.4.7.16.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  730
{Or     Code <Cd> [1..1] CodeSet 731
Or}     Proprietary <Prtry> [1..1] ± 732
   Basis <Bsis> [0..1]  732
{Or     Code <Cd> [1..1] CodeSet 732
Or}     Proprietary <Prtry> [1..1] ± 733
   StandardAmount <StdAmt> [0..1] Amount C1, C10 733
   StandardRate <StdRate> [0..1] Rate 733
   DiscountDetails <DscntDtls> [0..1]  C15 734
     Amount <Amt> [0..1] Amount C1, C10 734
     Rate <Rate> [0..1] Rate 735
     Basis <Bsis> [0..1]  735
{Or       Code <Cd> [1..1] CodeSet 735
Or}       Proprietary <Prtry> [1..1] ± 735
   AppliedAmount <ApldAmt> [0..1] Amount C1, C10 736
   AppliedRate <ApldRate> [0..1] Rate 736
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 736
   RecipientIdentification <RcptId> [0..1] ± 736
   InformativeIndicator <InftvInd> [1..1] Indicator 737
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
30.4.7.16.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 730 May 2026
```

