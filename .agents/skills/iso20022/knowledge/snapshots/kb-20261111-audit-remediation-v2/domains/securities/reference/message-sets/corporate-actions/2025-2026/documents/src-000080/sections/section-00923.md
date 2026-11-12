---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.2 ProprietaryStatusAndReason6", "16.1.26.2.1 ProprietaryStatus <PrtrySts>"]
file_pages: [1141]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.2.1 ProprietaryStatus <PrtrySts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1141 to 1141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1141

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1141
   ProprietaryReason <PrtryRsn> [0..*] ± C2 1141
16.1.26.2.1  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary identification of the status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "GenericIdentification30" on
page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.26.2.2  ProprietaryReason <PrtryRsn>
Presence: [0..*]
Definition: Proprietary identification of the reason related to a proprietary status.
Impacted by: C2 "AdditionalReasonInforrmationRule"
ProprietaryReason <PrtryRsn> contains the following elements (see "ProprietaryReason4" on
page 1143 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1144
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1144
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.1.26.3  AcceptedStatus8Choice
Definition: Choice between a reason or no reason for the corporate action instruction processing
accepted status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1141 February 2026
```

