---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.26 TransactionOverhead <TxOvrhd>", "43.4.5.9.26.5 IndividualFee <IndvFee>"]
file_pages: [1960]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.26.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1960 to 1960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1960

```text
43.4.5.9.26.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1960
{Or     Code <Cd> [1..1] CodeSet 1961
Or}     Proprietary <Prtry> [1..1] ± 1962
   Basis <Bsis> [0..1]  1962
{Or     Code <Cd> [1..1] CodeSet 1962
Or}     Proprietary <Prtry> [1..1] ± 1963
   StandardAmount <StdAmt> [0..1] Amount C3, C10 1963
   StandardRate <StdRate> [0..1] Rate 1963
   DiscountDetails <DscntDtls> [0..1]  C17 1964
     Amount <Amt> [0..1] Amount C3, C10 1964
     Rate <Rate> [0..1] Rate 1965
     Basis <Bsis> [0..1]  1965
{Or       Code <Cd> [1..1] CodeSet 1965
Or}       Proprietary <Prtry> [1..1] ± 1965
   AppliedAmount <ApldAmt> [0..1] Amount C3, C10 1966
   AppliedRate <ApldRate> [0..1] Rate 1966
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 1966
   RecipientIdentification <RcptId> [0..1] ± 1966
   InformativeIndicator <InftvInd> [1..1] Indicator 1967
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
43.4.5.9.26.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1960 May 2026
```

