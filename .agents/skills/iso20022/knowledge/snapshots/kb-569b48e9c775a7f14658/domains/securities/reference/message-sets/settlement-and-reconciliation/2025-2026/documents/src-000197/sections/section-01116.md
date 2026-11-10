---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.27 RegistrationReason5", "35.1.16.27.1 Code <Cd>"]
file_pages: [1559]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.27.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1559 to 1559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1559

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1559
{Or     Code <Cd> [1..1] CodeSet 1559
Or}     Proprietary <Prtry> [1..1] ± 1559
   AdditionalInformation <AddtlInf> [0..1] Text 1560
35.1.16.27.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason of the holding status.
Code <Cd> contains one of the following Registration10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1559
Or}   Proprietary <Prtry> [1..1] ± 1559
35.1.16.27.1.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration2Code" on page 2114
CodeName Name Definition
PTYH PartyHold You or your party set the instruction in a
hold/frozen/preadvice mode.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
35.1.16.27.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Registration information expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1559 March 2026
```

