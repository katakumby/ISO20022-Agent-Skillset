---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.16 UnitsDetails <UnitsDtls>", "26.4.6.16.8 TransactionOverhead <TxOvrhd>", "26.4.6.16.8.5 IndividualFee <IndvFee>"]
file_pages: [554]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.16.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 554 to 554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 554

```text
26.4.6.16.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  554
{Or     Code <Cd> [1..1] CodeSet 555
Or}     Proprietary <Prtry> [1..1] ± 556
   Basis <Bsis> [0..1]  556
{Or     Code <Cd> [1..1] CodeSet 556
Or}     Proprietary <Prtry> [1..1] ± 557
   StandardAmount <StdAmt> [0..1] Amount C1, C10 557
   StandardRate <StdRate> [0..1] Rate 557
   DiscountDetails <DscntDtls> [0..1]  C15 558
     Amount <Amt> [0..1] Amount C1, C10 558
     Rate <Rate> [0..1] Rate 559
     Basis <Bsis> [0..1]  559
{Or       Code <Cd> [1..1] CodeSet 559
Or}       Proprietary <Prtry> [1..1] ± 559
   AppliedAmount <ApldAmt> [0..1] Amount C1, C10 560
   AppliedRate <ApldRate> [0..1] Rate 560
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 560
   RecipientIdentification <RcptId> [0..1] ± 560
   InformativeIndicator <InftvInd> [1..1] Indicator 561
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
26.4.6.16.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 554 May 2026
```

