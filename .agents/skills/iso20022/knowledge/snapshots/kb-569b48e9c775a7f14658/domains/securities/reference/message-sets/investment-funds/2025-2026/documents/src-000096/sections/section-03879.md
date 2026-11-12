---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.2 ClosurePendingStatusReason1Choice", "66.1.45.2.2 Reason <Rsn>"]
file_pages: [5169]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.2.2 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5169 to 5169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5169

```text
66.1.45.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the closure pending status.
Reason <Rsn> contains the following ClosurePendingStatusReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  5169
{Or     Code <Cd> [1..1] CodeSet 5169
Or}     Proprietary <Prtry> [1..1] ± 5169
   AdditionalInformation <AddtlInf> [0..1] Text 5170
66.1.45.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the closure pending status.
Code <Cd> contains one of the following ClosurePendingStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5169
Or}   Proprietary <Prtry> [1..1] ± 5169
66.1.45.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the closure pending status expressed as a code.
Datatype: "ClosurePendingStatusReason1Code" on page 5284
CodeName Name Definition
CLOS AccountClosingInProcess Account closing is in process.
PEND PendingConditions Account will be closed when conditions
are met.
66.1.45.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the closure pending status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5169 May 2026
```

