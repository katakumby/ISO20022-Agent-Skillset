---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.50 PendingReason34", "82.1.30.50.1 Code <Cd>", "82.1.30.50.1.2 Proprietary <Prtry>"]
file_pages: [3198]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.50.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3198 to 3198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3198

```text
82.1.30.50.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.50.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.51  SettlementStatus34Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  3198
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3199
Or   Failing <Flng> [1..1]  3199
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3199
Or}     Reason <Rsn> [1..*] ± 3200
Or}   Proprietary <Prtry> [1..1] ± 3200
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
82.1.30.51.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3198 August 2026
```

