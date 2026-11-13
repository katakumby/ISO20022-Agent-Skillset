---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.6 ProprietaryStatusAndReason6", "35.1.29.6.1 ProprietaryStatus <PrtrySts>"]
file_pages: [1878]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.6.1 ProprietaryStatus <PrtrySts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1878 to 1878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1878

```text
35.1.29.6.1  ProprietaryStatus <PrtrySts>
Presence: [1..1]
Definition: Proprietary identification of the status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "GenericIdentification30" on
page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.6.2  ProprietaryReason <PrtryRsn>
Presence: [0..*]
Definition: Proprietary identification of the reason related to a proprietary status.
Impacted by: C1 "AdditionalReasonInforrmationRule"
ProprietaryReason <PrtryRsn> contains the following elements (see "ProprietaryReason4" on
page 1899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
35.1.29.7  AffirmationStatus8Choice
Definition: Choice of format for the affirmation status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1878
Or}   Proprietary <Prtry> [1..1] ± 1879
35.1.29.7.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of the trade at confirmation level at the time the settlement instruction
was sent.
Datatype: "AffirmationStatus1Code" on page 2045
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1878 March 2026
```

