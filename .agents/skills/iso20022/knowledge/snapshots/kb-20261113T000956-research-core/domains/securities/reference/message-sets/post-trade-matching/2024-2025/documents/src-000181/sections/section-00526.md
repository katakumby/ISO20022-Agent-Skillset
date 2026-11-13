---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.15 CancellationReason39Choice", "7.1.28.15.2 Reason <Rsn>", "7.1.28.15.2.1 Code <Cd>"]
file_pages: [604]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.15.2.1 Code <Cd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 604 to 604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 604

```text
Reason <Rsn> contains the following AwaitingCancellationReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  604
{Or     Code <Cd> [1..1] CodeSet 604
Or}     Proprietary <Prtry> [1..1] ± 604
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 604
7.1.28.15.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the trade is wainting the cancellation.
Code <Cd> contains one of the following AwaitingCancellationReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 604
Or}   Proprietary <Prtry> [1..1] ± 604
7.1.28.15.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Datatype: "AwaitingCancellationReason1Code" on page 615
CodeName Name Definition
WCAN AwaitingCancellation Cancellation has not been received yet.
7.1.28.15.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.15.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 604 February 2025
```

