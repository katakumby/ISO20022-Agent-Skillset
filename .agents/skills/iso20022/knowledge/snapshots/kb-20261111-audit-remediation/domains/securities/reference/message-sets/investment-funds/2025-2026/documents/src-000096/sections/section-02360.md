---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.26 TransactionOverhead <TxOvrhd>", "52.4.5.10.26.5 IndividualFee <IndvFee>"]
file_pages: [3323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.26.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3323 to 3323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3323

```text
52.4.5.10.26.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  3323
{Or     Code <Cd> [1..1] CodeSet 3324
Or}     Proprietary <Prtry> [1..1] ± 3325
   Basis <Bsis> [0..1]  3325
{Or     Code <Cd> [1..1] CodeSet 3325
Or}     Proprietary <Prtry> [1..1] ± 3326
   StandardAmount <StdAmt> [0..1] Amount C3, C11 3326
   StandardRate <StdRate> [0..1] Rate 3326
   DiscountDetails <DscntDtls> [0..1]  C19 3327
     Amount <Amt> [0..1] Amount C3, C11 3327
     Rate <Rate> [0..1] Rate 3328
     Basis <Bsis> [0..1]  3328
{Or       Code <Cd> [1..1] CodeSet 3328
Or}       Proprietary <Prtry> [1..1] ± 3328
   AppliedAmount <ApldAmt> [0..1] Amount C3, C11 3329
   AppliedRate <ApldRate> [0..1] Rate 3329
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 3329
   RecipientIdentification <RcptId> [0..1] ± 3329
   InformativeIndicator <InftvInd> [1..1] Indicator 3330
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
52.4.5.10.26.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3323 May 2026
```

