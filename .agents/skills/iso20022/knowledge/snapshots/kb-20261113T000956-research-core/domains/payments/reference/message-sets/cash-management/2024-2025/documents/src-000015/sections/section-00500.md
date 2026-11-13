---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07", "26.4 Message Building Blocks", "26.4.4 SupplementaryData <SplmtryData>"]
file_pages: [662]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26.4.4 SupplementaryData <SplmtryData>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 662 to 662.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 662

```text
Definition: New reservation values.
NewReservationValueSet <NewRsvatnValSet> contains the following elements (see "Reservation4"
on page 841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDateTime <StartDtTm> [0..1] ± 841
   Amount <Amt> [1..1] ± 841
26.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 662 February 2025
```

