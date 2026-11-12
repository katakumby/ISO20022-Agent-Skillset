---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.56 MatchingStatus24Choice", "35.1.29.56.2 Unmatched <Umtchd>", "35.1.29.56.2.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1965]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.56.2.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1965 to 1965.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1965

```text
Unmatched <Umtchd> contains one of the following UnmatchedStatus16Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}   Reason <Rsn> [1..*]  1965
     Code <Cd> [1..1]  1965
{Or       Code <Cd> [1..1] CodeSet 1966
Or}       Proprietary <Prtry> [1..1] ± 1968
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
35.1.29.56.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.56.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the unmatched status.
Reason <Rsn> contains the following UnmatchedReason15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1965
{Or     Code <Cd> [1..1] CodeSet 1966
Or}     Proprietary <Prtry> [1..1] ± 1968
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
35.1.29.56.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Code <Cd> contains one of the following UnmatchedReason21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1966
Or}   Proprietary <Prtry> [1..1] ± 1968
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1965 March 2026
```

