---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.3 PendingProcessing2Choice", "7.1.28.3.2 Reason <Rsn>", "7.1.28.3.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [588]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.3.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 588 to 588.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 588

```text
7.1.28.3.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Datatype: "Max210Text" on page 668
7.1.28.4  ProprietaryStatusAndReason6
Definition: Provides the proprietary status and reason of an instruction or an instruction cancellation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 588
   ProprietaryReason <PrtryRsn> [0..*] ± C4 588
7.1.28.4.1  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary identification of the status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "GenericIdentification30" on
page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.4.2  ProprietaryReason <PrtryRsn>
Presence: [0..*]
Definition: Proprietary identification of the reason related to a proprietary status.
Impacted by: C4 "AdditionalReasonInforrmationRule"
ProprietaryReason <PrtryRsn> contains the following elements (see "ProprietaryReason4" on
page 589 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 588 February 2025
```

