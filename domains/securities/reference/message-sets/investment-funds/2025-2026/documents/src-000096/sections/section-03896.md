---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.15 AcceptedStatusReason1Choice", "66.1.45.15.2 Proprietary <Prtry>"]
file_pages: [5187]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.15.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5187 to 5187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5187

```text
CodeName Name Definition
SECT SectorNotAllowed Status of the account modification
instruction is accepted but modification
of the account data will not be carried
out for the sector code.
66.1.45.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.16  TransferCancellationStatus3
Definition: Transfer cancellation status is accepted or sent to next party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 5187
   Reason <Rsn> [0..1] Text 5187
66.1.45.16.1  Status <Sts>
Presence: [1..1]
Definition: Status of the transfer cancellation is accepted or sent to next party.
Datatype: "CancellationStatus5Code" on page 5280
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
66.1.45.16.2  Reason <Rsn>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5187 May 2026
```

