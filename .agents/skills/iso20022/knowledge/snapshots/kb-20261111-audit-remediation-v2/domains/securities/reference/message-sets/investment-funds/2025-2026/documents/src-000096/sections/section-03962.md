---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.3 CancelledCompleteReason1"]
file_pages: [5259]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.3 CancelledCompleteReason1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5259 to 5259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5259

```text
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.3  CancelledCompleteReason1
Definition: Reason for a cancelled completed status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5259
{Or     Code <Cd> [1..1] CodeSet 5259
Or}     Proprietary <Prtry> [1..1] ± 5259
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5260
66.1.50.3.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the cancelled complete status.
Reason <Rsn> contains one of the following CancellationCompleteReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5259
Or}   Proprietary <Prtry> [1..1] ± 5259
66.1.50.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Cancelled complete reason expressed as a code.
Datatype: "CancelledStatusReason1Code" on page 5280
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Transaction is cancelled by the agent.
66.1.50.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cancelled complete reason expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5259 May 2026
```

