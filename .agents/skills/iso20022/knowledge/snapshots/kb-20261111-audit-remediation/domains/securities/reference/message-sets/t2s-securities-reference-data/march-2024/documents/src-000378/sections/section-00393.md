---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.7 SupplementaryData1"]
file_pages: [486]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.7 SupplementaryData1

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 486 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 486

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.10.7  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 486
   Envelope <Envlp> [1..1] (External Schema) 486
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
13.1.10.7.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 534
13.1.10.7.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
13.1.10.8  RateAndAmountFormat1Choice
Definition: Choice of format between rate, amount and not specified.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 487
Or   Amount <Amt> [1..1] Amount C1, C5 487
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1]  487
{Or     Code <Cd> [1..1] CodeSet 487
Or}     Proprietary <Prtry> [1..1] ± 488
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 486 March 2024
```

