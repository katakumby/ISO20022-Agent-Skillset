---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.5 ProformaStatusReason1Choice", "66.1.45.5.2 Reason <Rsn>", "66.1.45.5.2.2 AdditionalInformation <AddtlInf>"]
file_pages: [5173]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.5.2.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5173 to 5173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5173

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.5.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the proforma account status.
Datatype: "Max350Text" on page 5403
66.1.45.6  Status25Choice
Definition: Choice of formats for the specification of the status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 5173
Or}   Rejected <Rjctd> [1..10] ± 5173
66.1.45.6.1  Status <Sts>
Presence: [1..1]
Definition: Status code.
Datatype: "AccountManagementStatus1Code" on page 5271
CodeName Name Definition
RECE Received The account management instruction
has been received and is acknowledged.
ACCP Accepted The account management instruction
has been validated and accepted.
EXEC ProcessingOngoing The account management instruction is
being processed and the confirmation
will follow.
STNP SentToNextParty The account management instruction
has been sent to the next party, for
example, the next intermediary.
66.1.45.6.2  Rejected <Rjctd>
Presence: [1..10]
Definition: Status of the account management instruction is rejected.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5173 May 2026
```

