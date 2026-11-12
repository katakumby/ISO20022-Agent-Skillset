---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.4 Message Building Blocks", "8.4.8 UnderlyingIntraBalance <UndrlygIntraBal>", "8.4.8.7 InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8.4.8.7 InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
8.4.8.7  InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which can not be included within the
structured fields of the message.
Datatype: "Max350Text" on page 3328
8.4.9 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C15 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 132 August 2026
```

