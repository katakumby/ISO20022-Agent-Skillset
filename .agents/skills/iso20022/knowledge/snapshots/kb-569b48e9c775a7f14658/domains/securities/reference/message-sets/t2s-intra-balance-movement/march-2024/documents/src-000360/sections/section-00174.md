---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.5 Movement <Mvmnt>", "10.4.4.1.5.4 StatusAndReason <StsAndRsn>", "10.4.4.1.5.4.2 SettlementStatus <SttlmSts>"]
file_pages: [214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.5.4.2 SettlementStatus <SttlmSts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 214 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 214

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus67Choice" on page 456 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rejected <Rjctd> [1..1] ± 456
Or   Repair <Rpr> [1..1] ± 457
Or   Cancelled <Canc> [1..1] ± 457
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 457
Or}   Proprietary <Prtry> [1..1] ± 457
10.4.4.1.5.4.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C17 "PendingToFailingRule"
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
10.4.4.1.5.4.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
214 March 2024
```

