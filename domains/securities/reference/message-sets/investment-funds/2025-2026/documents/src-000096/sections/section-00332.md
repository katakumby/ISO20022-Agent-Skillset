---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.12 UnitsDetails <UnitsDtls>", "24.4.6.12.8 TransactionOverhead <TxOvrhd>", "24.4.6.12.8.5 IndividualFee <IndvFee>"]
file_pages: [466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.12.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 466 to 466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 466

```text
24.4.6.12.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  466
{Or     Code <Cd> [1..1] CodeSet 467
Or}     Proprietary <Prtry> [1..1] ± 468
   Basis <Bsis> [0..1]  468
{Or     Code <Cd> [1..1] CodeSet 468
Or}     Proprietary <Prtry> [1..1] ± 469
   StandardAmount <StdAmt> [0..1] Amount C1, C10 469
   StandardRate <StdRate> [0..1] Rate 469
   DiscountDetails <DscntDtls> [0..1]  C15 470
     Amount <Amt> [0..1] Amount C1, C10 470
     Rate <Rate> [0..1] Rate 471
     Basis <Bsis> [0..1]  471
{Or       Code <Cd> [1..1] CodeSet 471
Or}       Proprietary <Prtry> [1..1] ± 471
   AppliedAmount <ApldAmt> [0..1] Amount C1, C10 472
   AppliedRate <ApldRate> [0..1] Rate 472
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 472
   RecipientIdentification <RcptId> [0..1] ± 472
   InformativeIndicator <InftvInd> [1..1] Indicator 473
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
24.4.6.12.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 466 May 2026
```

