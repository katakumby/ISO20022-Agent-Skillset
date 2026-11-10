---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.12 PendingStatus39Choice"]
file_pages: [438]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.12 PendingStatus39Choice

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 438 to 438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus16Choice" on page 459 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  460
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 460
Or}     Reason <Rsn> [1..*] ± 460
Or   Failing <Flng> [1..1]  461
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 461
Or}     Reason <Rsn> [1..*] ± 461
Or}   Proprietary <Prtry> [1..1] ± 461
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
17.1.16.12  PendingStatus39Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 438
Or}   Reason <Rsn> [1..*]  438
     Code <Cd> [1..1] ± 439
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 439
17.1.16.12.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 485
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
17.1.16.12.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
438 March 2024
```

