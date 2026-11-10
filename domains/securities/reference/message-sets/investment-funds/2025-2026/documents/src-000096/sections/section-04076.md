---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.33 QUICKIdentifier"]
file_pages: [5397]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.33 QUICKIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5397 to 5397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5397

```text
66.2.5.33  QUICKIdentifier
Definition: Identifier of a security assigned by the Japanese QUICK identification scheme for financial
instruments.
Type: IdentifierSet
Identification scheme: QUICK; QUICKIdentifier
66.2.5.34  RICIdentifier
Definition: Reuters Identification Code (RIC). A numbering system used within the Reuters system to
identify instruments worldwide. The RIC contains an X-character market specific code (can be the
CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, for example, IBM in
UK is IBM.UK.
Type: IdentifierSet
Identification scheme: REUTERS ; REUTERSIdentifier
Format
minLength 1
maxLength 35
66.2.5.35  RussianCentralBankIdentificationCodeIdentifier
Definition: Russian Central Bank Identification Code. Identifies Russian financial institutions on the
Russian national clearing system.
Type: IdentifierSet
Identification scheme: Central Bank of Russia; RussianCentralBankIdentificationCode
Format
pattern RU[0-9]{9,9}
66.2.5.36  SEDOLIdentifier
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Type: IdentifierSet
Identification scheme: London Stock Exchange; SEDOLIdentifier
66.2.5.37  SicovamIdentifier
Definition: Identifier for French securities assigned by the Societe Interprofessionnelle Pour La
Compensation des Valeurs Mobilieres in France. The Sicovam is composed of 5-digits.
Type: IdentifierSet
Identification scheme: Sicovam; SicovamIdentifier
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5397 May 2026
```

