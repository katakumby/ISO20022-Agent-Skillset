---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.13 Miscellaneous", "17.1.13.8 SupplementaryData1", "17.1.13.8.1 PlaceAndName <PlcAndNm>"]
file_pages: [416]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.13.8.1 PlaceAndName <PlcAndNm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 416 to 416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 416
   Envelope <Envlp> [1..1] (External Schema) 416
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
17.1.13.8.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 497
17.1.13.8.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
17.1.13.9  NumberCount1Choice
Definition: Choice of number count type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 416
Or}   TotalNumber <TtlNb> [1..1]  C11, C7 417
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 417
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 417
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
17.1.13.9.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
416 March 2024
```

