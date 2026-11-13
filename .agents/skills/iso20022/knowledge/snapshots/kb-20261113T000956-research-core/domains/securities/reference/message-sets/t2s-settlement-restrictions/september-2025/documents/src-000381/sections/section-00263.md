---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.36 SettlementStatus34Choice", "9.1.21.36.2 Failing <Flng>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.36.2 Failing <Flng>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
Reason <Rsn> contains the following elements (see "PendingReason34" on page 306 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  306
{Or     Code <Cd> [1..1] CodeSet 307
Or}     Proprietary <Prtry> [1..1] ± 307
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 307
9.1.21.36.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following FailingStatus17Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 309
Or}   Reason <Rsn> [1..*] ± 309
9.1.21.36.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.36.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following elements (see "FailingReason15" on page 310 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  310
{Or     Code <Cd> [1..1] CodeSet 310
Or}     Proprietary <Prtry> [1..1] ± 311
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 311
9.1.21.36.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 309 September 2025
```

