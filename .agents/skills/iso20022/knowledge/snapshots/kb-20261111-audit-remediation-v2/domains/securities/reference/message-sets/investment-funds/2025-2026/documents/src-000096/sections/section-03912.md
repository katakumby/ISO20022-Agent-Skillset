---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.25 EnabledStatusReason1Choice", "66.1.45.25.2 Reason <Rsn>", "66.1.45.25.2.1 Code <Cd>", "66.1.45.25.2.1.2 Proprietary <Prtry>"]
file_pages: [5204]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.25.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5204 to 5204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5204

```text
Definition: Reason for the enabled account status expressed as a code.
Datatype: "EnabledStatusReason1Code" on page 5296
CodeName Name Definition
MODI Modified Modification to the account data is in
process.
66.1.45.25.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the enabled account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.25.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the enabled account status.
Datatype: "Max350Text" on page 5403
66.1.45.26  PlanStatus2Choice
Definition: Choice of formats for the status of a plan.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5204
Or}   Proprietary <Prtry> [1..1] ± 5204
66.1.45.26.1  Code <Cd>
Presence: [1..1]
Definition: Status of the plan expressed as a code.
Datatype: "PlanStatus1Code" on page 5341
CodeName Name Definition
ACTV Active Plan is active.
CLOS Closed Plan is closed.
SUSP Suspended Plan is suspended.
66.1.45.26.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5204 May 2026
```

