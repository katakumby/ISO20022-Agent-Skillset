---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.28 AccountStatusUpdateInstruction1", "66.1.45.28.2 UpdateInstructionReason <UpdInstrRsn>", "66.1.45.28.2.2 Reason <Rsn>", "66.1.45.28.2.2.1 Code <Cd>"]
file_pages: [5208]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.28.2.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5208 to 5208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5208

```text
Reason <Rsn> contains the following AccountStatusUpdateInstructionReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1]  5208
{Or     Code <Cd> [1..1] CodeSet 5208
Or}     Proprietary <Prtry> [1..1] ± 5208
   AdditionalInformation <AddtlInf> [0..1] Text 5209
Constraints
• ReasonElementRule
Either Code or AdditionalInformation must be present. Both may be present.
66.1.45.28.2.2.1  Code <Cd>
Presence: [0..1]
Definition: Reason for the instruction to change the account status.
Code <Cd> contains one of the following AccountStatusUpdateInstructionReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5208
Or}   Proprietary <Prtry> [1..1] ± 5208
66.1.45.28.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the instruction to change the account status expressed as a code.
Datatype: "AccountStatusUpdateRequestReason1Code" on page 5275
CodeName Name Definition
CLOE AccountClosureInstructionError Previous account closure instruction was
sent in error.
66.1.45.28.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the instruction to change the account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5208 May 2026
```

