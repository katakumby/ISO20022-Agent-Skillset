---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.5 IdentifierSet", "66.2.5.25 ISINIdentifier"]
file_pages: [5395]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.5.25 ISINIdentifier

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5395 to 5395.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5395

```text
Identification scheme: Irish Payment Services Organisation (IPSO); Irish National Sort Code
Format
pattern IE[0-9]{6,6}
66.2.5.25  ISINIdentifier
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Format
pattern [A-Z0-9]{12,12}
66.2.5.26  ISINOct2015Identifier
Definition: The International Securities Identification Number is a code allocated to financial instruments
as well as referential instruments, as described in the ISO 6166 standard, associated with the minimum
descriptive data. The ISIN consists of a prefix using the alpha-2 country codes or reserved codes
specified in ISO 3166 or other prefixes as may be determined by the Registration Authority for the ISO
6166 standard, a nine characters (alphanumeric) basic code and a check digit.
Note: this identifier also supports the new version of the standard, which was published in 2021 (ISO
6166:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Format
pattern [A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}
66.2.5.27  ItalianDomesticIdentifier
Definition: Italian Domestic Identification Code. Identifies Italian financial institutions on the Italian
national clearing system. The code is assigned by the Associazione Bancaria Italiana (ABI).
Type: IdentifierSet
Identification scheme: Associazione Bancaria Italiana; Italian Domestic Identification
Format
pattern IT[0-9]{10,10}
66.2.5.28  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5395 May 2026
```

