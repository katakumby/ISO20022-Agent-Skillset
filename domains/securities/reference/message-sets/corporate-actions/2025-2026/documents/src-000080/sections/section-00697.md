---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.1 RateAndAmountFormat56Choice", "16.1.15.1.4 RateTypeAndRate <RateTpAndRate>", "16.1.15.1.4.1 RateType <RateTp>", "16.1.15.1.4.1.2 Proprietary <Prtry>"]
file_pages: [888]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.1.4.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 888 to 888.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 888

```text
CodeName Name Definition
NRAT NRATax Withholding tax related to income
subject to NRA (Non Resident Alien).
16.1.15.1.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of withholding tax rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.1.4.2  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.15.2  ClassificationType32Choice
Definition: Choice of format for the classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 888
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 888
16.1.15.2.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: ISO 10962 Classification of Financial Instrument (CFI).
Datatype: "CFIOct2015Identifier" on page 1244
16.1.15.2.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Proprietary classification of financial instrument.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 888 February 2026
```

