---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.5 IdentifierSet", "7.2.5.5 IBAN2007Identifier"]
file_pages: [664]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.5.5 IBAN2007Identifier

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 664 to 664.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 664

```text
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
7.2.5.5  IBAN2007Identifier
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
7.2.5.6  ISINOct2015Identifier
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
7.2.5.7  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Type: IdentifierSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 664 February 2025
```

