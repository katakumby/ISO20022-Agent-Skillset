---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.30 ProcessingStatus99Choice"]
file_pages: [301]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.30 ProcessingStatus99Choice

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 301 to 301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
Cancelled <Canc> contains one of the following elements (see "CancellationStatus15Choice" on
page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 276
Or}   Reason <Rsn> [1..*]  276
     Code <Cd> [1..1] ± 276
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 277
9.1.21.30  ProcessingStatus99Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 301
Or   Rejected <Rjctd> [1..1] ± 301
Or   Repair <Rpr> [1..1] ± 302
Or   Cancelled <Canc> [1..1] ± 302
Or}   Proprietary <Prtry> [1..1] ± 302
9.1.21.30.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus34Choice" on page 303 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 303
Or}   Reason <Rsn> [1..*] ± 303
9.1.21.30.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction or request has been rejected for further processing.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 301 September 2025
```

