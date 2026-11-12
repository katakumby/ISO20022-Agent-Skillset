---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.1 SettlementStatus32Choice", "7.1.28.1.1 Pending <Pdg>", "7.1.28.1.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [459]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.1.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 459 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 459

```text
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following PendingStatus73Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 459
Or}   Reason <Rsn> [1..*]  459
     Code <Cd> [1..1]  459
{Or       Code <Cd> [1..1] CodeSet 460
Or}       Proprietary <Prtry> [1..1] ± 463
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 463
7.1.28.1.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.1.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  459
{Or     Code <Cd> [1..1] CodeSet 460
Or}     Proprietary <Prtry> [1..1] ± 463
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 463
7.1.28.1.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following PendingReason69Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 460
Or}   Proprietary <Prtry> [1..1] ± 463
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 459 March 2026
```

