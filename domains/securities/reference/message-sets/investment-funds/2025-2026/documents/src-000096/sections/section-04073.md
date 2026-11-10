---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.21 HongKongBankIdentifier"]
file_pages: [5394]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.21 HongKongBankIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5394 to 5394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5394

```text
Identification scheme: Hellenic Central Bank; Payment Routing Number
Format
pattern GR[0-9]{7,7}
66.2.5.21  HongKongBankIdentifier
Definition: Hong Kong Bank Code. Identifies Hong Kong financial institutions on the Hong Kong local
clearing system.
Type: IdentifierSet
Identification scheme: Hong Kong Interbank Clearing Ltd (HKICL); Bank Code of Hong Kong
Format
pattern HK[0-9]{3,3}
66.2.5.22  IBAN2007Identifier
Definition: The International Bank Account Number is a code used internationally by financial
institutions to uniquely identify the account of a customer at a financial institution as described in the
2007 edition of the ISO 13616 standard "Banking and related financial services - International Bank
Account Number (IBAN)" and replaced by the more recent edition of the standard.
Type: IdentifierSet
Identification scheme: National Banking Association; International Bank Account Number (ISO 13616)
Format
pattern [A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
66.2.5.23  IndianFinancialSystemCodeIdentifier
Definition: Indian Financial System Code Identifier. Identifies Indian financial institutions on the Indian
national clearing system.
Type: IdentifierSet
Identification scheme: Indian Financial System; Payment Routing Number
Format
pattern IN[a-zA-Z0-9]{11,11}
66.2.5.24  IrishNSCIdentifier
Definition: Irish National Sorting Code. Identifies Irish financial institutions on the Irish national clearing
system.
Type: IdentifierSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5394 May 2026
```

