---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.14 RejectionOrRepairStatus39Choice", "9.1.21.14.2 Reason <Rsn>", "9.1.21.14.2.1 Code <Cd>", "9.1.21.14.2.1.2 Proprietary <Prtry>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.14.2.1.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
CodeName Name Definition
NRGN NotFoundRejection Instruction could not be found.
OTHR Other Other. See Narrative.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
9.1.21.14.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.14.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
9.1.21.15  CancellationReason21Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 285
Or}   Proprietary <Prtry> [1..1] ± 285
9.1.21.15.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Datatype: "CancelledStatusReason5Code" on page 317
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
OTHR Other Other. See Narrative.
9.1.21.15.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 285 September 2025
```

