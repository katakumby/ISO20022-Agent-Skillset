---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.2 SettlementStatus26Choice"]
file_pages: [269]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.2 SettlementStatus26Choice

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 269 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus34Choice" on page 308 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  308
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 308
Or}     Reason <Rsn> [1..*] ± 308
Or   Failing <Flng> [1..1]  309
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 309
Or}     Reason <Rsn> [1..*] ± 309
Or}   Proprietary <Prtry> [1..1] ± 309
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
9.1.21.2  SettlementStatus26Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 269
Or}   Proprietary <Prtry> [1..1] ± 269
9.1.21.2.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of settlement of an instruction/financial instrument movement.
Datatype: "SecuritiesSettlementStatus1Code" on page 339
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
9.1.21.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of settlement of an instruction/financial instrument movement.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 269 September 2025
```

