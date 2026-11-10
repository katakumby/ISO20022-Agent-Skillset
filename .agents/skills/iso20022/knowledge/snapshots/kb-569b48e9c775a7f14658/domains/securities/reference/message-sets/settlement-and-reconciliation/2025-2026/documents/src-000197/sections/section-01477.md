---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.56 MatchingStatus24Choice", "35.1.29.56.2 Unmatched <Umtchd>", "35.1.29.56.2.2 Reason <Rsn>", "35.1.29.56.2.2.1 Code <Cd>", "35.1.29.56.2.2.1.2 Proprietary <Prtry>"]
file_pages: [1968]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.56.2.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1968 to 1968.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1968

```text
35.1.29.56.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.56.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.56.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
35.1.29.57  AcknowledgedAcceptedStatus21Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
35.1.29.57.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1968 March 2026
```

