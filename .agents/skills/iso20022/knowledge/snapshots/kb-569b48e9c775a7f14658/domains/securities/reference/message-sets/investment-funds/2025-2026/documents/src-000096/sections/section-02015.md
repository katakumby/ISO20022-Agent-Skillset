---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.26 TransactionOverhead <TxOvrhd>", "49.4.5.9.26.5 IndividualFee <IndvFee>"]
file_pages: [2838]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.26.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2838 to 2838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2838

```text
49.4.5.9.26.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2838
{Or     Code <Cd> [1..1] CodeSet 2839
Or}     Proprietary <Prtry> [1..1] ± 2840
   Basis <Bsis> [0..1]  2840
{Or     Code <Cd> [1..1] CodeSet 2840
Or}     Proprietary <Prtry> [1..1] ± 2841
   StandardAmount <StdAmt> [0..1] Amount C3, C10 2841
   StandardRate <StdRate> [0..1] Rate 2841
   DiscountDetails <DscntDtls> [0..1]  C17 2842
     Amount <Amt> [0..1] Amount C3, C10 2842
     Rate <Rate> [0..1] Rate 2843
     Basis <Bsis> [0..1]  2843
{Or       Code <Cd> [1..1] CodeSet 2843
Or}       Proprietary <Prtry> [1..1] ± 2843
   AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2844
   AppliedRate <ApldRate> [0..1] Rate 2844
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 2844
   RecipientIdentification <RcptId> [0..1] ± 2844
   InformativeIndicator <InftvInd> [1..1] Indicator 2845
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
49.4.5.9.26.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2838 May 2026
```

