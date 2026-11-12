---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.49 GeneratedReason5", "35.1.29.49.1 Code <Cd>"]
file_pages: [1954]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.49.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1954 to 1954.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1954

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1954
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1954
35.1.29.49.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the transaction was generated.
Code <Cd> contains one of the following elements (see "GeneratedReasons5Choice" on page 1970 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1970
Or}   Proprietary <Prtry> [1..1] ± 1970
35.1.29.49.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.50  MatchingStatus25Choice
Definition: Choice of format for the matching status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1954
Or   Unmatched <Umtchd> [1..1]  1955
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1955
Or}     Reason <Rsn> [1..*]  1955
       Code <Cd> [1..1] ± 1956
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1956
Or}   Proprietary <Prtry> [1..1] ± 1956
35.1.29.50.1  Matched <Mtchd>
Presence: [1..1]
Definition: Status is matched.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1954 March 2026
```

