---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.3 StatusAndReason <StsAndRsn>", "3.4.3.3.2 SettlementStatus <SttlmSts>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.3.2 SettlementStatus <SttlmSts>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus99Choice" on page 301 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 301
Or   Rejected <Rjctd> [1..1] ± 301
Or   Repair <Rpr> [1..1] ± 302
Or   Cancelled <Canc> [1..1] ± 302
Or}   Proprietary <Prtry> [1..1] ± 302
3.4.3.3.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C16 "PendingToFailingRule"
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
3.4.3.3.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 68 September 2025
```

