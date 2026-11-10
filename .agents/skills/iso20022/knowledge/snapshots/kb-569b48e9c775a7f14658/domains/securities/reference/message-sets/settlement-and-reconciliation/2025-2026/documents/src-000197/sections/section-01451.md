---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.38 MatchingStatus26Choice", "35.1.29.38.1 Matched <Mtchd>"]
file_pages: [1937]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.38.1 Matched <Mtchd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1937 to 1937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1937

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1937
Or   Unmatched <Umtchd> [1..1]  1937
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1937
Or}     Reason <Rsn> [1..*]  1938
       Code <Cd> [1..1] ± 1938
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1938
Or}   Proprietary <Prtry> [1..1] ± 1938
35.1.29.38.1  Matched <Mtchd>
Presence: [1..1]
Definition: Status is matched.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Matched <Mtchd> contains the following elements (see "ProprietaryReason4" on page 1899 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
35.1.29.38.2  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status is unmatched.
Unmatched <Umtchd> contains one of the following UnmatchedStatus18Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1937
Or}   Reason <Rsn> [1..*]  1938
     Code <Cd> [1..1] ± 1938
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1938
35.1.29.38.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1937 March 2026
```

