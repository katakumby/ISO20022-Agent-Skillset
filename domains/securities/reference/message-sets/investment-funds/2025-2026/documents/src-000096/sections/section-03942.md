---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.3 TaxReference1", "66.1.47.3.1 TaxType <TaxTp>"]
file_pages: [5235]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.3.1 TaxType <TaxTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5235 to 5235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5235

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxType <TaxTp> [0..1]  5235
{Or     Code <Cd> [1..1] CodeSet 5235
Or}     Proprietary <Prtry> [1..1] ± 5235
   Reference <Ref> [1..1] Text 5236
   HolderType <HldrTp> [0..1]  5236
{Or     Code <Cd> [1..1] CodeSet 5236
Or}     Proprietary <Prtry> [1..1] ± 5236
66.1.47.3.1  TaxType <TaxTp>
Presence: [0..1]
Definition: Type of tax reference.
TaxType <TaxTp> contains one of the following TaxReferenceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5235
Or}   Proprietary <Prtry> [1..1] ± 5235
66.1.47.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax reference expressed as a code.
Datatype: "PersonIdentificationType7Code" on page 5341
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
GTIN GenericTaxIdentificationNumber Generic tax identification number.
ITIN IndividualTaxpayerIdentificationNumber Tax processing number.
66.1.47.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax reference expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5235 May 2026
```

