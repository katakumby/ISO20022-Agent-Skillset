---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.50 MatchingStatus25Choice", "35.1.29.50.2 Unmatched <Umtchd>"]
file_pages: [1955]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.50.2 Unmatched <Umtchd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1955 to 1955.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1955

```text
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
35.1.29.50.2  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status is unmatched.
Unmatched <Umtchd> contains one of the following UnmatchedStatus17Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1955
Or}   Reason <Rsn> [1..*]  1955
     Code <Cd> [1..1] ± 1956
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1956
35.1.29.50.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.50.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the unmatched status.
Reason <Rsn> contains the following UnmatchedReason16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1956
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1956
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1955 March 2026
```

