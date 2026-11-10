---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.42 ProcessingStatus69Choice", "82.1.30.42.5 Proprietary <Prtry>"]
file_pages: [3187]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.42.5 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3187 to 3187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3187

```text
82.1.30.42.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 3130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 3130
   ProprietaryReason <PrtryRsn> [0..*] ± C6 3130
82.1.30.42.6  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 3160 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3160
Or}   Reason <Rsn> [1..*]  3161
     Code <Cd> [1..1] ± 3161
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3161
82.1.30.42.7  Cancelled <Canc>
Presence: [1..1]
Definition: Cancellation requested executed.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus15Choice" on
page 3146 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3146
Or}   Reason <Rsn> [1..*]  3146
     Code <Cd> [1..1] ± 3146
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3147
82.1.30.43  ProcessingStatus70Choice
Definition: Choice of format for the processing status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3187 August 2026
```

