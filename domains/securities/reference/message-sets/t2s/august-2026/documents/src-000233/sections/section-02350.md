---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.7 PendingStatusAndReason2", "82.1.30.7.1 ProcessingStatus <PrcgSts>"]
file_pages: [3137]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.7.1 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3137 to 3137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3137

```text
82.1.30.7.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus66Choice" on page 3162 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3162
Or   Repair <Rpr> [1..1] ± 3162
Or   Cancelled <Canc> [1..1] ± 3163
Or}   Proprietary <Prtry> [1..1] ± 3163
82.1.30.7.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C14 "PendingToFailingRule"
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
82.1.30.8  ProcessingStatus67Choice
Definition: Choice of format for the processing status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3137 August 2026
```

