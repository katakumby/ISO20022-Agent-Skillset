---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.33 AcknowledgementReason22", "9.1.21.33.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.33.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
9.1.21.33.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.34  ProcessingStatus100Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 305
Or   Repair <Rpr> [1..1] ± 305
Or   Cancelled <Canc> [1..1] ± 306
Or}   Proprietary <Prtry> [1..1] ± 306
9.1.21.34.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus34Choice" on page 303 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 303
Or}   Reason <Rsn> [1..*] ± 303
9.1.21.34.2  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 277
Or}   Reason <Rsn> [1..*]  277
     Code <Cd> [0..*]  278
{Or       Code <Cd> [1..1] CodeSet 278
Or}       Proprietary <Prtry> [1..1] ± 279
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 279
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 305 September 2025
```

