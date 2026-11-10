---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.28 RejectionOrRepairStatus40Choice", "9.1.21.28.2 Reason <Rsn>", "9.1.21.28.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.28.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.28.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.29  ProcessingStatus69Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 298
Or   Rejected <Rjctd> [1..1] ± 299
Or   Repair <Rpr> [1..1] ± 299
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 299
Or   Proprietary <Prtry> [1..1] ± 300
Or   Denied <Dnd> [1..1] ± 300
Or}   Cancelled <Canc> [1..1] ± 300
9.1.21.29.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation is pending processing.
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingStatus39Choice" on page 293 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 293
Or}   Reason <Rsn> [1..*]  293
     Code <Cd> [1..1] ± 293
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 294
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 298 September 2025
```

