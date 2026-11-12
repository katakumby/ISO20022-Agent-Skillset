---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.5 PersonIdentification10", "22.1.10.5.4 Other <Othr>", "22.1.10.5.4.2 SchemeName <SchmeNm>", "22.1.10.5.4.2.1 Code <Cd>"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.5.4.2.1 Code <Cd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
SchemeName <SchmeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 349
Or}   Proprietary <Prtry> [1..1] Text 349
22.1.10.5.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalPersonIdentification1Code" on page 437
22.1.10.5.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 456
22.1.10.5.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 456
22.1.11 Price
22.1.11.1  SecuritiesTransactionPrice22Choice
Definition: Choice element capturing strike price related descriptive information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Price <Pric> [1..1] ± 349
Or   DigitalTokenPrice <DgtlTknPric> [1..1] ± 350
Or}   NoPrice <NoPric> [1..1] ± 350
22.1.11.1.1  Price <Pric>
Presence: [1..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
349 July 2025
```

