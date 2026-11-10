---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.26 SettlementStatus16Choice", "17.1.16.26.2 Failing <Flng>"]
file_pages: [461]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.26.2 Failing <Flng>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 461 to 461.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 461

```text
Reason <Rsn> contains the following elements (see "PendingReason14" on page 466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  466
{Or     Code <Cd> [1..1] CodeSet 466
Or}     Proprietary <Prtry> [1..1] ± 469
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
17.1.16.26.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus9Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 461
Or}   Reason <Rsn> [1..*] ± 461
17.1.16.26.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 485
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
17.1.16.26.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following elements (see "FailingReason7" on page 462 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  462
{Or     Code <Cd> [1..1] CodeSet 462
Or}     Proprietary <Prtry> [1..1] ± 465
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 466
17.1.16.26.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
461 March 2024
```

