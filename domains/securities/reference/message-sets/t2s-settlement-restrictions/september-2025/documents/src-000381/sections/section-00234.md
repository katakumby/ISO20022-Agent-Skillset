---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.12 ProcessingStatus71Choice", "9.1.21.12.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.12.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 280
Or   Pending <Pdg> [1..1] ± 280
Or   Rejected <Rjctd> [1..1] ± 280
Or   Repair <Rpr> [1..1] ± 281
Or   Denied <Dnd> [1..1] ± 281
Or   Completed <Cmpltd> [1..1] ± C5 282
Or}   Proprietary <Prtry> [1..1] ± 282
9.1.21.12.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Request has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 291 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 291
Or}   Reason <Rsn> [1..*] ± 291
9.1.21.12.2  Pending <Pdg>
Presence: [1..1]
Definition: Modification is pending. It is not known at this time whether modification can be affected.
Pending <Pdg> contains one of the following elements (see "PendingStatus38Choice" on page 282 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 282
Or}   Reason <Rsn> [1..*]  283
     Code <Cd> [1..1] ± 283
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 283
9.1.21.12.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Modification request has been rejected for further processing.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 280 September 2025
```

