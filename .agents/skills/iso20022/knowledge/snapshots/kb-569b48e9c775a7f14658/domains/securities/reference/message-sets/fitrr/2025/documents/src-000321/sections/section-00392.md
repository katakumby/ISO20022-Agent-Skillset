---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.5 IdentifierSet"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.5 IdentifierSet

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
22.2.5 IdentifierSet
22.2.5.1  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
22.2.5.2  DTI2021Identifier
Definition: The Digital Token Identifier (DTI) is an 8 character code assigned to fungible digital assets
which uses distributed ledger technology for its issuance, storage, exchange, record of ownership or
transaction validation and is not a currency (ISO 4217) as described in ISO 24165 - DTI. A check
character, using the same character set as the base number, shall be calculated and added.
Type: IdentifierSet
Identification scheme: Digital Token Identifier Foundation (DTIF)
Format
pattern [1-9B-DF-HJ-NP-XZ][0-9B-DF-HJ-NP-XZ]{8,8}
22.2.5.3  ISINOct2015Identifier
Definition: The International Securities Identification Number is a code allocated to financial instruments
as well as referential instruments, as described in the ISO 6166 standard, associated with the minimum
descriptive data. The ISIN consists of a prefix using the alpha-2 country codes or reserved codes
specified in ISO 3166 or other prefixes as may be determined by the Registration Authority for the ISO
6166 standard, a nine characters (alphanumeric) basic code and a check digit.
Note: this identifier also supports the new version of the standard, which was published in 2021 (ISO
6166:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
450 July 2025
```

