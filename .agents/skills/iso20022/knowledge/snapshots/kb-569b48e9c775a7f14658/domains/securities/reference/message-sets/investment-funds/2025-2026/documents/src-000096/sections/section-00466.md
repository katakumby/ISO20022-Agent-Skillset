---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.12 UnitsDetails <UnitsDtls>", "28.4.7.12.8 TransactionOverhead <TxOvrhd>", "28.4.7.12.8.5 IndividualFee <IndvFee>"]
file_pages: [642]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.12.8.5 IndividualFee <IndvFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 642 to 642.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 642

```text
28.4.7.12.8.5  IndividualFee <IndvFee>
Presence: [0..*]
Definition: Individual fee (charge/commission).
Impacted by: C6 "AppliedAmountRule"
IndividualFee <IndvFee> contains the following Fee11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  642
{Or     Code <Cd> [1..1] CodeSet 643
Or}     Proprietary <Prtry> [1..1] ± 644
   Basis <Bsis> [0..1]  644
{Or     Code <Cd> [1..1] CodeSet 644
Or}     Proprietary <Prtry> [1..1] ± 645
   StandardAmount <StdAmt> [0..1] Amount C1, C10 645
   StandardRate <StdRate> [0..1] Rate 645
   DiscountDetails <DscntDtls> [0..1]  C15 646
     Amount <Amt> [0..1] Amount C1, C10 646
     Rate <Rate> [0..1] Rate 647
     Basis <Bsis> [0..1]  647
{Or       Code <Cd> [1..1] CodeSet 647
Or}       Proprietary <Prtry> [1..1] ± 647
   AppliedAmount <ApldAmt> [0..1] Amount C1, C10 648
   AppliedRate <ApldRate> [0..1] Rate 648
   NonStandardSLAReference <NonStdSLARef> [0..1] Text 648
   RecipientIdentification <RcptId> [0..1] ± 648
   InformativeIndicator <InftvInd> [1..1] Indicator 649
Constraints
• AppliedAmountRule
If InformativeIndicator is "false" or "0" (No), then AppliedAmount must be present.
On Condition
    /InformativeIndicator is equal to value 'false'
 Or    /InformativeIndicator is equal to value '0'
Following Must be True
    /AppliedAmount Must be present
28.4.7.12.8.5.1  Type <Tp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 642 May 2026
```

