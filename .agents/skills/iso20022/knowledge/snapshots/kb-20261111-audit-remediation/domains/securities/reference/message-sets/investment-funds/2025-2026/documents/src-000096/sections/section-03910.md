---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.24 RejectionReason31", "66.1.45.24.1 Reason <Rsn>"]
file_pages: [5202]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.24.1 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5202 to 5202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5202

```text
66.1.45.24.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason16Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5202
Or}   Proprietary <Prtry> [1..1] ± 5202
66.1.45.24.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "RejectedStatusReason6Code" on page 5357
CodeName Name Definition
SAFE InvestmentAccount Investment account identification is not
recognised or is invalid.
NSLA NotCompliantWithSLA Instruction is not compliant with the
service level agreement.
66.1.45.24.1.2  Proprietary <Prtry>
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
66.1.45.24.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the rejected status reason.
Datatype: "Max350Text" on page 5403
66.1.45.25  EnabledStatusReason1Choice
Definition: Choice of formats for an enabled status reason.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5202 May 2026
```

