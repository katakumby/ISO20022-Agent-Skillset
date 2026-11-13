---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 MatchingStatus24Choice", "7.1.28.11.2 Unmatched <Umtchd>", "7.1.28.11.2.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11.2.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
Unmatched <Umtchd> contains one of the following UnmatchedStatus16Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 478
Or}   Reason <Rsn> [1..*]  478
     Code <Cd> [1..1]  478
{Or       Code <Cd> [1..1] CodeSet 479
Or}       Proprietary <Prtry> [1..1] ± 481
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 481
7.1.28.11.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.11.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the unmatched status.
Reason <Rsn> contains the following UnmatchedReason15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  478
{Or     Code <Cd> [1..1] CodeSet 479
Or}     Proprietary <Prtry> [1..1] ± 481
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 481
7.1.28.11.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Code <Cd> contains one of the following UnmatchedReason21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 479
Or}   Proprietary <Prtry> [1..1] ± 481
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 478 March 2026
```

