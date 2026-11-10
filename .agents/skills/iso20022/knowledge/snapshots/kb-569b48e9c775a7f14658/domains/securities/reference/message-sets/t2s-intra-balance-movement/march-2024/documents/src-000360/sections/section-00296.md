---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.7 SubBalance <SubBal>", "15.4.7.2 Movement <Mvmnt>", "15.4.7.2.17 CreationDateTime <CreDtTm>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.7.2.17 CreationDateTime <CreDtTm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
15.4.7.2.17  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Specifies the date/time on which the trade was executed.
Datatype: "ISODateTime" on page 493
15.4.7.2.18  InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which can not be included within the
structured fields of the message.
Datatype: "Max350Text" on page 497
15.4.7.2.19  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C15 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 415 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 416
   Envelope <Envlp> [1..1] (External Schema) 416
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
357 March 2024
```

