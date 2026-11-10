---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.8 FinancialInstrumentDetails <FinInstrmDtls>", "43.4.5.8.1 Identification <Id>", "43.4.5.8.1.9 Wertpapier <Wrtppr>"]
file_pages: [1932]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.8.1.9 Wertpapier <Wrtppr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1932 to 1932.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1932

```text
Datatype: "QUICKIdentifier" on page 5397
43.4.5.8.1.9  Wertpapier <Wrtppr>
Presence: [1..1]
Definition: Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The
Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are
different ranges of numbers representing different classes of securities.
Datatype: "WertpapierIdentifier" on page 5399
43.4.5.8.1.10  Dutch <Dtch>
Presence: [1..1]
Definition: Identifier for Dutch securities.
Datatype: "DutchIdentifier" on page 5392
43.4.5.8.1.11  Valoren <Vlrn>
Presence: [1..1]
Definition: Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency.
Datatype: "ValorenIdentifier" on page 5399
43.4.5.8.1.12  Sicovam <SCVM>
Presence: [1..1]
Definition: Identifier for French securities assigned by the Societe Interprofessionnelle Pour La
Compensation des Valeurs Mobilieres in France. The Sicovam is composed of 5-digits.
Datatype: "SicovamIdentifier" on page 5397
43.4.5.8.1.13  Belgian <Belgn>
Presence: [1..1]
Definition: Identifier for Belgian securities.
Datatype: "BelgianIdentifier" on page 5390
43.4.5.8.1.14  Common <Cmon>
Presence: [1..1]
Definition: Identifier of securities issued in Luxembourg. The common code is a 9-digit code that
replaces the CEDEL (Clearstream) and Euroclear codes.
Datatype: "EuroclearClearstreamIdentifier" on page 5393
43.4.5.8.1.15  DTI <DTI>
Presence: [1..1]
Definition: Digital Token Identifier, as defined in ISO 24165.
Datatype: "DTI2024Identifier" on page 5392
43.4.5.8.1.16  OtherProprietaryIdentification <OthrPrtryId>
Presence: [1..1]
Definition: Proprietary identification of the security assigned by an institution or organisation.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1932 May 2026
```

