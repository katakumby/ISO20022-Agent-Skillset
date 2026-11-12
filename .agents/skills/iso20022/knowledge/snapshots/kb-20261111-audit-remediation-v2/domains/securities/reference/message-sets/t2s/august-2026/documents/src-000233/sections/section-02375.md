---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.26 MatchingDenied3Choice", "82.1.30.26.2 Proprietary <Prtry>"]
file_pages: [3162]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.26.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3162 to 3162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3162

```text
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
82.1.30.26.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.27  ProcessingStatus66Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3162
Or   Repair <Rpr> [1..1] ± 3162
Or   Cancelled <Canc> [1..1] ± 3163
Or}   Proprietary <Prtry> [1..1] ± 3163
82.1.30.27.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 3172 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3173
Or}   Reason <Rsn> [1..*] ± 3173
82.1.30.27.2  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3162 August 2026
```

