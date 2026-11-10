---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.3 StatusAndReason <StsAndRsn>", "74.4.3.3.2 SettlementStatus <SttlmSts>"]
file_pages: [2623]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.3.2 SettlementStatus <SttlmSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2623 to 2623.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2623

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus99Choice" on page 3191 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3192
Or   Rejected <Rjctd> [1..1] ± 3192
Or   Repair <Rpr> [1..1] ± 3192
Or   Cancelled <Canc> [1..1] ± 3193
Or}   Proprietary <Prtry> [1..1] ± 3193
74.4.3.3.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C16 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus34Choice" on page 3198 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3198
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3199
Or   Failing <Flng> [1..1]  3199
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3200
Or}   Proprietary <Prtry> [1..1] ± 3200
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
74.4.3.3.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2623 August 2026
```

