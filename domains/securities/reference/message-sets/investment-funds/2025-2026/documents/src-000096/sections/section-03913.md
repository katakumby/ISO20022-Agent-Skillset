---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.27 TransferInstructionStatus5"]
file_pages: [5205]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.27 TransferInstructionStatus5

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5205 to 5205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5205

```text
Definition: Status of the plan expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.45.27  TransferInstructionStatus5
Definition: Instruction status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 5205
   Reason <Rsn> [0..1] Text 5205
66.1.45.27.1  Status <Sts>
Presence: [1..1]
Definition: Status code.
Datatype: "TransferStatus6Code" on page 5380
CodeName Name Definition
PACK Accepted Transfer or settlement instruction has
been acknowledged / accepted for
further processing.
COSE AlreadyExecuted Transfer or settlement instruction is fully
executed and the confirmation is sent.
COMP Complete Portfolio transfer is complete.
DELY Delayed Transfer or settlement instruction is
delayed.
MACH Matched Transfer or settlement instruction is
matched.
RECE Received Instruction has been received, that is,
technical validation of the message is ok,
and the message is now at the receiving
side.
STNP SentToNextParty Transfer or settlement instruction has
been sent to the next party, that is, the
next intermediary.
SETT Settled Transfer or settlement instruction is
settled.
66.1.45.27.2  Reason <Rsn>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5205 May 2026
```

