---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.21 ProcessingStatus71Choice", "17.1.16.21.5 Denied <Dnd>"]
file_pages: [452]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.21.5 Denied <Dnd>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 452 to 452.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 452

```text
17.1.16.21.5  Denied <Dnd>
Presence: [1..1]
Definition: Modification request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 434 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 435
Or}   Reason <Rsn> [1..*]  435
     Code <Cd> [1..1] ± 435
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 435
17.1.16.21.6  Completed <Cmpltd>
Presence: [1..1]
Definition: Modification request was completed.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Completed <Cmpltd> contains the following elements (see "ProprietaryReason4" on page 436 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 436
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 437
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
17.1.16.21.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 470
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 471
   ProprietaryReason <PrtryRsn> [0..*] ± C5 471
17.1.16.22  ProcessingStatus69Choice
Definition: Choice of format for the processing status.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
452 March 2024
```

