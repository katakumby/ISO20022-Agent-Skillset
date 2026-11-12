---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.30 ProprietaryStatusAndReason6", "17.1.16.30.1 ProprietaryStatus <PrtrySts>"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.30.1 ProprietaryStatus <PrtrySts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 471
   ProprietaryReason <PrtryRsn> [0..*] ± C5 471
17.1.16.30.1  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary identification of the status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "GenericIdentification30" on
page 409 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.30.2  ProprietaryReason <PrtryRsn>
Presence: [0..*]
Definition: Proprietary identification of the reason related to a proprietary status.
Impacted by: C5 "AdditionalReasonInforrmationRule"
ProprietaryReason <PrtryRsn> contains the following elements (see "ProprietaryReason4" on
page 436 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 436
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 437
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
17.1.16.31  AcknowledgementReason9
Definition: Specifies additional information about the processed instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 472
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 472
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
471 March 2024
```

