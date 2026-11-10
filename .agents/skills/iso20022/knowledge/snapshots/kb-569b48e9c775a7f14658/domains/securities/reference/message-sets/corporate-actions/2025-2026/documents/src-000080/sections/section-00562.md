---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.4 Message Building Blocks", "12.4.5 CorporateActionInstruction <CorpActnInstr>", "12.4.5.1 OptionNumber <OptnNb>"]
file_pages: [730]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.4.5.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 730 to 730.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 730

```text
CorporateActionInstruction <CorpActnInstr> contains the following CorporateActionOption200
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 730
   OptionType <OptnTp> [1..1] ± 730
   InstructedQuantity <InstdQty> [1..1] ± 730
Constraints
• OptionNumber1Rule
For differentiation between options, the OptionNumber must be used (preferred rather than the
OptionType for example in the case where two or more offers can be described by the same
corporate action option code). Therefore, the OptionNumber value must be different for each option.
• OptionNumber2Rule
When the CorporateActionInstruction is unsolicited, that is, the instruction has not been preceded by
an Corporate ActionNotification, then OptionNumber/code must be UNSO (unsolicited).
12.4.5.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
OptionNumber <OptnNb> contains one of the following elements (see "OptionNumber1Choice" on
page 970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Text 970
Or}   Code <Cd> [1..1] CodeSet 970
12.4.5.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption40Choice"
on page 892 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 892
Or}   Proprietary <Prtry> [1..1] ± 894
12.4.5.3  InstructedQuantity <InstdQty>
Presence: [1..1]
Definition: Quantity of securities to which this instruction applies.
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 730 February 2026
```

