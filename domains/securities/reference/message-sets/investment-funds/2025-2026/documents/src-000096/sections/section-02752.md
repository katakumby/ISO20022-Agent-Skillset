---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.18 TransactionOverhead <TxOvrhd>", "55.4.5.19.18.5 IndividualFee <IndvFee>"]
file_pages: [3882]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.18.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3882 to 3882.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3882

```text
55.4.5.19.18.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C5 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  3882
{Or     Code <Cd> [1..1] CodeSet 3883
Or}     Proprietary <Prtry> [1..1] ± 3884
   Basis <Bsis> [0..1]  3884
{Or     Code <Cd> [1..1] CodeSet 3884
Or}     Proprietary <Prtry> [1..1] ± 3885
   StandardAmount <StdAmt> [0..1] Amount C2, C8 3885
   StandardRate <StdRate> [0..1] Rate 3885
   DiscountDetails <DscntDtls> [0..1]  C15 3886
     Amount <Amt> [0..1] Amount C2, C8 3886
     Rate <Rate> [0..1] Rate 3887
     Basis <Bsis> [0..1]  3887
{Or       Code <Cd> [1..1] CodeSet 3887
Or}       Proprietary <Prtry> [1..1] ± 3887
   AppliedAmount <ApldAmt> [0..1] Amount C2, C8 3888
   AppliedRate <ApldRate> [0..1] Rate 3888
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 3888
   RecipientIdentification <RcptId> [0..1] ± 3888
   InformativeIndicator <InftvInd> [1..1] Indicator 3889
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
55.4.5.19.18.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3882 May 2026
```

