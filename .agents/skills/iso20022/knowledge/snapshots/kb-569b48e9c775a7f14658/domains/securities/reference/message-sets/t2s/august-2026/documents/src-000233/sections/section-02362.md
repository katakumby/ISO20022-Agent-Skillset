---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.16 RejectionOrRepairStatus38Choice", "82.1.30.16.2 Reason <Rsn>", "82.1.30.16.2.1 Code <Cd>", "82.1.30.16.2.1.2 Proprietary <Prtry>"]
file_pages: [3149]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.16.2.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3149 to 3149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3149

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
82.1.30.16.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.16.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.17  CancellationStatus24Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3150
Or}   Reason <Rsn> [1..*]  3150
     Code <Cd> [1..1]  3150
{Or       Code <Cd> [1..1] CodeSet 3150
Or}       Proprietary <Prtry> [1..1] ± 3151
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3151
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3149 August 2026
```

