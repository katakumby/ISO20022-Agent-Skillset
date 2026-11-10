---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.1 Units <Units>"]
file_pages: [725]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.1 Units <Units>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 725 to 725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 725

```text
30.4.7.16.1  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 725
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 725
30.4.7.16.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
30.4.7.16.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
30.4.7.16.2  OrderDate <OrdrDt>
Presence: [0..1]
Definition: Date the investor or its agent placed the original order.
Datatype: "ISODate" on page 5388
30.4.7.16.3  AcquisitionDate <AcqstnDt>
Presence: [0..1]
Definition: Date the investor purchased the financial instrument.
Datatype: "ISODate" on page 5388
30.4.7.16.4  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Certificate representing the security that is delivered.
Datatype: "Max35Text" on page 5403
30.4.7.16.5  Group1Or2Units <Grp1Or2Units>
Presence: [0..1]
Definition: Tax group to which the purchased investment fund units belong. The investor indicates to the
intermediary operating pooled nominees, which type of unit is to be sold.
Datatype: "UKTaxGroupUnit1Code" on page 5387
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 725 May 2026
```

