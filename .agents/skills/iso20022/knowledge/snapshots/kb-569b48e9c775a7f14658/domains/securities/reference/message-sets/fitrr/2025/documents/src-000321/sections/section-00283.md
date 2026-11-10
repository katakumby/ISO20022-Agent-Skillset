---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.7 Identification Information"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.7 Identification Information

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
Index <Indx> contains the following elements (see "FinancialInstrument58" on page 328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 328
   Name <Nm> [1..1] ± 328
22.1.7 Identification Information
22.1.7.1  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] Text 333
22.1.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 436
22.1.7.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: "Max35Text" on page 456
22.1.8 Market
22.1.8.1  TradingVenueIdentification2
Definition: Trading venue related fields.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 333
   Type <Tp> [1..1] CodeSet 334
22.1.8.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification field of the submitting entity.
Datatype: "Max50Text" on page 456
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
333 July 2025
```

