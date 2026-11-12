---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.11 MatchingStatus24Choice", "7.1.28.11.1 Matched <Mtchd>"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.11.1 Matched <Mtchd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C6 477
Or   Unmatched <Umtchd> [1..1]  477
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 478
Or}     Reason <Rsn> [1..*]  478
       Code <Cd> [1..1]  478
{Or         Code <Cd> [1..1] CodeSet 479
Or}         Proprietary <Prtry> [1..1] ± 481
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 481
Or}   Proprietary <Prtry> [1..1] ± 481
7.1.28.11.1  Matched <Mtchd>
Presence: [1..1]
Definition: Status is matched.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Matched <Mtchd> contains the following elements (see "ProprietaryReason4" on page 470 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 470
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
7.1.28.11.2  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status is unmatched.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 477 March 2026
```

