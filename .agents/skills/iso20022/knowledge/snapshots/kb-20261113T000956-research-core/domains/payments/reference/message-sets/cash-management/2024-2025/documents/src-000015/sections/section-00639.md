---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.6 SupplementaryData1", "37.1.11.6.1 PlaceAndName <PlcAndNm>"]
file_pages: [816]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.6.1 PlaceAndName <PlcAndNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 816 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 816

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
37.1.11.6.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 889
37.1.11.6.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
37.1.11.7  ErrorHandling3
Definition: Specifies the error resulting from the processing of a request.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  816
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   Description <Desc> [0..1] Text 817
37.1.11.7.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 816 February 2025
```

