---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.3 PendingProcessing2Choice", "7.1.28.3.2 Reason <Rsn>"]
file_pages: [587]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.3.2 Reason <Rsn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 587 to 587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 587

```text
7.1.28.3.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the Pending Processing Status.
Reason <Rsn> contains the following AwaitingAffirmationReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  587
{Or     Code <Cd> [1..1] CodeSet 587
Or}     Proprietary <Prtry> [1..1] ± 587
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 588
7.1.28.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the trade is wainting the affirmation.
Code <Cd> contains one of the following AwaitingAffirmationReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 587
Or}   Proprietary <Prtry> [1..1] ± 587
7.1.28.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has been alleged.
Datatype: "AwaitingAffirmationReason1Code" on page 615
CodeName Name Definition
WAFF AwaitingAffirmation Affirmation has not been received yet.
7.1.28.3.2.1.2  Proprietary <Prtry>
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 587 February 2025
```

