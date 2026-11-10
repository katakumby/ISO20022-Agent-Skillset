---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.5 CancellationStatus24Choice"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.5 CancellationStatus24Choice

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
7.1.28.5  CancellationStatus24Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 471
Or}   Reason <Rsn> [1..*]  471
     Code <Cd> [1..1]  471
{Or       Code <Cd> [1..1] CodeSet 472
Or}       Proprietary <Prtry> [1..1] ± 472
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 472
7.1.28.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.1.28.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the cancellation status.
Reason <Rsn> contains the following CancellationReason22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  471
{Or     Code <Cd> [1..1] CodeSet 472
Or}     Proprietary <Prtry> [1..1] ± 472
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 472
7.1.28.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction is cancelled.
Code <Cd> contains one of the following CancellationReason36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 472
Or}   Proprietary <Prtry> [1..1] ± 472
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 471 March 2026
```

