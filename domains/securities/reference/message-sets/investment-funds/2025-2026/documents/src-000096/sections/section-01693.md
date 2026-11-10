---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.26 TransactionOverhead <TxOvrhd>", "46.4.5.10.26.5 IndividualFee <IndvFee>"]
file_pages: [2380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.26.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2380 to 2380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2380

```text
46.4.5.10.26.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2380
{Or     Code <Cd> [1..1] CodeSet 2381
Or}     Proprietary <Prtry> [1..1] ± 2382
   Basis <Bsis> [0..1]  2382
{Or     Code <Cd> [1..1] CodeSet 2382
Or}     Proprietary <Prtry> [1..1] ± 2383
   StandardAmount <StdAmt> [0..1] Amount C3, C10 2383
   StandardRate <StdRate> [0..1] Rate 2383
   DiscountDetails <DscntDtls> [0..1]  C17 2384
     Amount <Amt> [0..1] Amount C3, C10 2384
     Rate <Rate> [0..1] Rate 2385
     Basis <Bsis> [0..1]  2385
{Or       Code <Cd> [1..1] CodeSet 2385
Or}       Proprietary <Prtry> [1..1] ± 2385
   AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2386
   AppliedRate <ApldRate> [0..1] Rate 2386
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 2386
   RecipientIdentification <RcptId> [0..1] ± 2386
   InformativeIndicator <InftvInd> [1..1] Indicator 2387
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
46.4.5.10.26.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2380 May 2026
```

