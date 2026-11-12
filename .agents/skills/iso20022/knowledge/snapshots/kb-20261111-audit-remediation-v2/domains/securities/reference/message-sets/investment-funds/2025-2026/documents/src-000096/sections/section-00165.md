---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.4 FinancialInstrumentDetails <FinInstrmDtls>", "14.4.10.1.4.1 Identification <Id>", "14.4.10.1.4.1.9 Wertpapier <Wrtppr>"]
file_pages: [249]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.4.1.9 Wertpapier <Wrtppr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 249 to 249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
Definition: Identifier of a security assigned by the Japanese QUICK identification scheme for financial
instruments.
Datatype: "QUICKIdentifier" on page 5397
14.4.10.1.4.1.9  Wertpapier <Wrtppr>
Presence: [1..1]
Definition: Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The
Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are
different ranges of numbers representing different classes of securities.
Datatype: "WertpapierIdentifier" on page 5399
14.4.10.1.4.1.10  Dutch <Dtch>
Presence: [1..1]
Definition: Identifier for Dutch securities.
Datatype: "DutchIdentifier" on page 5392
14.4.10.1.4.1.11  Valoren <Vlrn>
Presence: [1..1]
Definition: Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency.
Datatype: "ValorenIdentifier" on page 5399
14.4.10.1.4.1.12  Sicovam <SCVM>
Presence: [1..1]
Definition: Identifier for French securities assigned by the Societe Interprofessionnelle Pour La
Compensation des Valeurs Mobilieres in France. The Sicovam is composed of 5-digits.
Datatype: "SicovamIdentifier" on page 5397
14.4.10.1.4.1.13  Belgian <Belgn>
Presence: [1..1]
Definition: Identifier for Belgian securities.
Datatype: "BelgianIdentifier" on page 5390
14.4.10.1.4.1.14  Common <Cmon>
Presence: [1..1]
Definition: Identifier of securities issued in Luxembourg. The common code is a 9-digit code that
replaces the CEDEL (Clearstream) and Euroclear codes.
Datatype: "EuroclearClearstreamIdentifier" on page 5393
14.4.10.1.4.1.15  DTI <DTI>
Presence: [1..1]
Definition: Digital Token Identifier, as defined in ISO 24165.
Datatype: "DTI2024Identifier" on page 5392
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 249 May 2026
```

