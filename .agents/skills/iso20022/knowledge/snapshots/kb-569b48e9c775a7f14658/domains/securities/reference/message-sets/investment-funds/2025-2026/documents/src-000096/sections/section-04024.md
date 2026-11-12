---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.147 OrderCancellationStatus2Code"]
file_pages: [5332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.147 OrderCancellationStatus2Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5332 to 5332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5332

```text
CodeName Name Definition
ENAB Enabled Enabled.
SPEC SpecialCircumstances Special circumstances.
66.2.2.147  OrderCancellationStatus2Code
Definition: Specifies the current status of the order cancellation request.
Type: CodeSet
CodeName Name Definition
STNP SentToNextParty Order cancellation request has been
sent to the next party, eg, the next
intermediary.
RECE Received Status of the order cancellation request
is received, that is, technical validation of
the message is ok, and the message is
now at the receiving side.
CANP CancellationPending Order cancellation request is pending,
The order cancellation request has been
received but this does not indicate the
order has been cancelled.
CAND CancellationCompleted Status of the order cancellation request
is completed. The cancellation request
has been accepted and processed; the
order has been cancelled.
66.2.2.148  OrderConfirmationStatus1Code
Definition: Specifies the current status of an order confirmation or of an order confirmation amendment.
Type: CodeSet
CodeName Name Definition
STNP SentToNextParty Order confirmation or order confirmation
cancellation instruction or order
confirmation amendment has been sent
to the next party, eg, the next
intermediary.
CPNP CommunicationProblemNextParty Communication problems with the next
party.
COAC ConfirmationAccepted Order confirmation or order confirmation
amendment is accepted.
CREC ConfirmationReceived Order confirmation or order confirmation
amendment is received, ie, technical
validation of the message is ok, and the
message is now at the receiving side.
66.2.2.149  OrderOriginatorEligibility1Code
Definition: Specifies the type of the counterparties eligibility as defined by article 24 of the EU MiFID
Directive applicable to transactions executed by investment firms for eligible counterparties.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5332 May 2026
```

