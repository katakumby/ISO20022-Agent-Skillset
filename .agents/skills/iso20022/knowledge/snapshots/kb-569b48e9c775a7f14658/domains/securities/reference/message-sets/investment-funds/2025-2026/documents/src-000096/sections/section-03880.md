---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.2 ClosurePendingStatusReason1Choice", "66.1.45.2.2 Reason <Rsn>", "66.1.45.2.2.2 AdditionalInformation <AddtlInf>"]
file_pages: [5170]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.2.2.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5170 to 5170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5170

```text
66.1.45.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the closure pending status.
Datatype: "Max350Text" on page 5403
66.1.45.3  OtherAccountStatus1
Definition: Status of an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] ± 5170
   Reason <Rsn> [0..1] ± 5170
66.1.45.3.1  Status <Sts>
Presence: [1..1]
Definition: Status of the account.
Status <Sts> contains the following elements (see "GenericIdentification36" on page 4549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.3.2  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the status of the account.
Reason <Rsn> contains the following elements (see "GenericIdentification36" on page 4549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.4  DrawdownStatus1Choice
Definition: Choice of formats for a drawdown status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5171
Or}   Proprietary <Prtry> [1..1] ± 5171
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5170 May 2026
```

