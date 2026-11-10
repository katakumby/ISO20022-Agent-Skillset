---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.2 IndividualCancellationStatusReport <IndvCxlStsRpt>", "57.4.3.2.6 CancellationStatus <CxlSts>", "57.4.3.2.6.2 Rejected <Rjctd>"]
file_pages: [4220]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.2.6.2 Rejected <Rjctd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4220 to 4220.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4220

```text
CodeName Name Definition
the message is ok, and the message is
now at the receiving side.
CANP CancellationPending Order cancellation request is pending,
The order cancellation request has been
received but this does not indicate the
order has been cancelled.
CAND CancellationCompleted Status of the order cancellation request
is completed. The cancellation request
has been accepted and processed; the
order has been cancelled.
57.4.3.2.6.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Status of the order cancellation request is rejected.
Impacted by: C8 "ReasonElementRule"
Rejected <Rjctd> contains the following RejectedStatus13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  4220
{Or     Code <Cd> [1..1] CodeSet 4220
Or}     Proprietary <Prtry> [1..1] ± 4221
   AdditionalInformation <AddtlInf> [0..1] Text 4221
Constraints
• ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
57.4.3.2.6.2.1  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the rejected status.
Reason <Rsn> contains one of the following RejectedReason66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4220
Or}   Proprietary <Prtry> [1..1] ± 4221
57.4.3.2.6.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Rejected reason expressed as a code.
Datatype: "RejectedStatusReason14Code" on page 5354
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4220 May 2026
```

