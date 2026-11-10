---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.43 TickerIdentifier"]
file_pages: [5399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.43 TickerIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5399 to 5399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5399

```text
Type: IdentifierSet
Identification scheme: Swiss Interbank Clearing Ltd; SIC Identifier
Format
pattern SW[0-9]{6,6}
66.2.5.43  TickerIdentifier
Definition: Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and
convenient way of identifying a stock, for example, RTR.L for Reuters quoted in London.
Type: IdentifierSet
Identification scheme: Bloomberg; BloombergIdentifier
Format
minLength 1
maxLength 35
66.2.5.44  UKDomesticSortCodeIdentifier
Definition: United Kingdom (UK) Sort Code. Identifies British financial institutions on the British national
clearing systems. The sort code is assigned by the Association for Payments and Clearing Services
(APACS).
Type: IdentifierSet
Identification scheme: Association for Payment Clearing Services (APACS); UK Sort Code
Format
pattern SC[0-9]{6,6}
66.2.5.45  ValorenIdentifier
Definition: Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency.
Type: IdentifierSet
Identification scheme: Valoren; ValorenIdentifier
66.2.5.46  WertpapierIdentifier
Definition: Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The
Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are
different ranges of numbers representing different classes of securities.
Type: IdentifierSet
Identification scheme: Wertpapier; WertpapierIdentifier
66.2.6 Indicator
66.2.6.1  PlusOrMinusIndicator
Definition: Indicates a positive or negative value.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5399 May 2026
```

