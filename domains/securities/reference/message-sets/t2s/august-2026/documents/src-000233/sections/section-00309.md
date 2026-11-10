---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.4 StatusAndReason <StsAndRsn>", "17.4.4.1.5.4.2 SettlementStatus <SttlmSts>"]
file_pages: [405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.4.2 SettlementStatus <SttlmSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 405 to 405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 405

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus67Choice" on page 3137 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rejected <Rjctd> [1..1] ± 3138
Or   Repair <Rpr> [1..1] ± 3138
Or   Cancelled <Canc> [1..1] ± 3138
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3139
Or}   Proprietary <Prtry> [1..1] ± 3139
17.4.4.1.5.4.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C17 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus16Choice" on page 3140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3140
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3141
Or}     Reason <Rsn> [1..*] ± 3141
Or   Failing <Flng> [1..1]  3141
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3141
Or}     Reason <Rsn> [1..*] ± 3142
Or}   Proprietary <Prtry> [1..1] ± 3142
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
17.4.4.1.5.4.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 405 August 2026
```

