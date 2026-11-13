---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.23 ProcessingStatus68Choice", "17.1.16.23.2 Proprietary <Prtry>"]
file_pages: [456]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.23.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 456 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 456

```text
CodeName Name Definition
REPR InRepair Instruction is accepted but in repair.
17.1.16.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.24  ProcessingStatus67Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rejected <Rjctd> [1..1] ± 456
Or   Repair <Rpr> [1..1] ± 457
Or   Cancelled <Canc> [1..1] ± 457
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 457
Or}   Proprietary <Prtry> [1..1] ± 457
17.1.16.24.1  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction or request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 444
Or}   Reason <Rsn> [1..*]  444
     Code <Cd> [0..*]  445
{Or       Code <Cd> [1..1] CodeSet 445
Or}       Proprietary <Prtry> [1..1] ± 446
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
456 March 2024
```

