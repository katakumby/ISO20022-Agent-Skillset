---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.15 SupplementaryData <SplmtryData>"]
file_pages: [718]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.15 SupplementaryData <SplmtryData>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 718 to 718.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 718

```text
InformationAgent <InfAgt> contains one of the following elements (see "PartyIdentification120Choice"
on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
11.4.15 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C14 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 718 February 2026
```

