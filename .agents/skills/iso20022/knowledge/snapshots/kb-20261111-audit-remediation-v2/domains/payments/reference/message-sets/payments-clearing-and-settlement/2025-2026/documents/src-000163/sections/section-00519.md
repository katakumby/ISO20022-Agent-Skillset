---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.4 SupplementaryData <SplmtryData>"]
file_pages: [701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.4 SupplementaryData <SplmtryData>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 701 to 701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 701

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1191
   Envelope <Envlp> [1..1] (External Schema) 1191
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
5.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C35 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1191
   Envelope <Envlp> [1..1] (External Schema) 1191
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
701 March 2026
```

