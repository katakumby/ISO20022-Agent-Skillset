---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.21 ProcessingStatus71Choice"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.21 ProcessingStatus71Choice

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.21  ProcessingStatus71Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or   Pending <Pdg> [1..1] ± 450
Or   Rejected <Rjctd> [1..1] ± 451
Or   Repair <Rpr> [1..1] ± 451
Or   Denied <Dnd> [1..1] ± 452
Or   Completed <Cmpltd> [1..1] ± C5 452
Or}   Proprietary <Prtry> [1..1] ± 452
17.1.16.21.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Request has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 472 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 472
Or}   Reason <Rsn> [1..*] ± 472
17.1.16.21.2  Pending <Pdg>
Presence: [1..1]
Definition: Modification is pending. It is not known at this time whether modification can be affected.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
450 March 2024
```

