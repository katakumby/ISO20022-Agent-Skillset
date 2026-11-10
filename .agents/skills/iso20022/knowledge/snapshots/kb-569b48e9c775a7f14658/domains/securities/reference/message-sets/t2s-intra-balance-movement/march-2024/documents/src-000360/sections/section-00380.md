---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.16 RejectionOrRepairStatus38Choice", "17.1.16.16.2 Reason <Rsn>", "17.1.16.16.2.1 Code <Cd>", "17.1.16.16.2.1.2 Proprietary <Prtry>"]
file_pages: [446]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.16.2.1.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 446 to 446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
CodeName Name Definition
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
OTHR Other Other. See Narrative.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
17.1.16.16.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.16.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 497
17.1.16.17  CancellationReason21Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 446
Or}   Proprietary <Prtry> [1..1] ± 447
17.1.16.17.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
446 March 2024
```

