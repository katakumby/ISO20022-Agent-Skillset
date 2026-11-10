---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.6 OptionCancelledInstructionBalance <OptnCancInstrBal>"]
file_pages: [788]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.6 OptionCancelledInstructionBalance <OptnCancInstrBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 788 to 788.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 788

```text
14.4.3.5.3.3.7.6  OptionCancelledInstructionBalance <OptnCancInstrBal>
Presence: [0..1]
Definition: Daily total of cancelled instructions for a given option.
OptionCancelledInstructionBalance <OptnCancInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.7.7  OptionPendingInstructionBalance <OptnPdgInstrBal>
Presence: [0..1]
Definition: Daily total of pending instructions in pending status for a given option. It includes cancel
pending instructions.
OptionPendingInstructionBalance <OptnPdgInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.7.8  OptionRejectedInstructionBalance <OptnRjctdInstrBal>
Presence: [0..1]
Definition: Daily total of rejected instructions for a given option.
OptionRejectedInstructionBalance <OptnRjctdInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.7.9  OptionReturnedInstructedBalance <OptnRtrdInstdBal>
Presence: [0..1]
Definition: Daily total of returned instructions received for a given option.
OptionReturnedInstructedBalance <OptnRtrdInstdBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 788 February 2026
```

