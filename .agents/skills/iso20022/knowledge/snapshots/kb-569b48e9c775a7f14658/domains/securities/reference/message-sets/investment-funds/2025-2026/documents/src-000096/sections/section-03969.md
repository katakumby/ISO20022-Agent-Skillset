---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.10 RejectionReason33", "66.1.50.10.1 Reason <Rsn>"]
file_pages: [5267]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.10.1 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5267 to 5267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5267

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5267
{Or     Code <Cd> [1..1] CodeSet 5267
Or}     Proprietary <Prtry> [1..1] ± 5267
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5267
66.1.50.10.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason17Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5267
Or}   Proprietary <Prtry> [1..1] ± 5267
66.1.50.10.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "CancellationRejectedReason1Code" on page 5279
CodeName Name Definition
CUTO CutOffTime Instruction has been received after the
cut-off time.
COSE AlreadyExecuted Order or transfer has already been
executed and confirmation has been
sent.
66.1.50.10.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rejected reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.50.10.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5267 May 2026
```

