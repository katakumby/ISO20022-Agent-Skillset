---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.1 Units <Units>"]
file_pages: [1399]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.1 Units <Units>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1399 to 1399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1399

```text
38.4.15.8.4.1  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1399
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1399
38.4.15.8.4.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
38.4.15.8.4.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
38.4.15.8.4.2  OrderDate <OrdrDt>
Presence: [0..1]
Definition: Date the investor or its agent placed the original order.
Datatype: "ISODate" on page 5388
38.4.15.8.4.3  AcquisitionDate <AcqstnDt>
Presence: [0..1]
Definition: Date the investor purchased the financial instrument.
Datatype: "ISODate" on page 5388
38.4.15.8.4.4  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Certificate representing the security that is delivered.
Datatype: "Max35Text" on page 5403
38.4.15.8.4.5  Group1Or2Units <Grp1Or2Units>
Presence: [0..1]
Definition: Tax group to which the purchased investment fund units belong. The investor indicates to the
intermediary operating pooled nominees, which type of unit is to be sold.
Datatype: "UKTaxGroupUnit1Code" on page 5387
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1399 May 2026
```

