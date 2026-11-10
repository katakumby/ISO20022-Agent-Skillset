---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.22 ProcessingStatus69Choice", "17.1.16.22.4 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.22.4 AcknowledgedAccepted <AckdAccptd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
page 442 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 442
Or}   Reason <Rsn> [1..*]  443
     Code <Cd> [1..1]  443
{Or       Code <Cd> [1..1] CodeSet 443
Or}       Proprietary <Prtry> [1..1] ± 443
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 444
17.1.16.22.4  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus24Choice" on page 427 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 428
Or}   Reason <Rsn> [1..*]  428
     Code <Cd> [1..1] ± 428
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 428
17.1.16.22.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 470
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 471
   ProprietaryReason <PrtryRsn> [0..*] ± C5 471
17.1.16.22.6  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
454 March 2024
```

