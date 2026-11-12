---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.29 CancellationStatus5Code"]
file_pages: [5280]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.29 CancellationStatus5Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5280 to 5280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5280

```text
CodeName Name Definition
NOWA WaiverAgreement Investor is not entitled to cancellation
rights under compliance rules as the
investor has agreed to waive those
rights.
NOIN Institutional Investor is not entitled to cancellation
rights under compliance rules as the
investor is a financial institution.
66.2.2.29  CancellationStatus5Code
Definition: Specifies the cancellation status.
Type: CodeSet
CodeName Name Definition
RECE Received Cancellation instruction/request has
been received, that is, technical
validation of the message is ok, and the
message is now at the receiving side.
PACK Accepted Cancellation instruction / request has
been received and has been
acknowledged / accepted for further
processing.
STNP SentToNextParty Cancellation instruction/request has
been sent to the next party, that is, the
next intermediary.
66.2.2.30  CancelledStatusReason1Code
Definition: Specifies the underlying reason for cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Transaction is cancelled by the agent.
66.2.2.31  CancelledStatusReason2Code
Definition: Specifies the underlying reason for cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANH CancelledByHub Transaction is cancelled by the hub.
CANP CancelledByInstructingParty Transaction is cancelled by the
instructing party.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5280 May 2026
```

