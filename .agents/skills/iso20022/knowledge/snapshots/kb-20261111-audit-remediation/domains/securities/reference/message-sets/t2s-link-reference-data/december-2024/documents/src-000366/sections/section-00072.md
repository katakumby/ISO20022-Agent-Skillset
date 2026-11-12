---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.2 Message Datatypes", "8.2.4 IdentifierSet"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.2.4 IdentifierSet

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
8.2.4 IdentifierSet
8.2.4.1  AnyBICDec2014Identifier
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages -
Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; AnyBICIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
8.2.4.2  IBAN2007Identifier
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
8.2.4.3  ISINOct2015Identifier
Definition: The International Securities Identification Number is a code allocated to financial instruments
as well as referential instruments, as described in the ISO 6166 standard, associated with the minimum
descriptive data. The ISIN consists of a prefix using the alpha-2 country codes or reserved codes
specified in ISO 3166 or other prefixes as may be determined by the Registration Authority for the ISO
6166 standard, a nine characters (alphanumeric) basic code and a check digit.
Note: this identifier also supports the new version of the standard, which was published in 2021 (ISO
6166:2021) as there is no update in the pattern.
Type: IdentifierSet
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 76 December 2024
```

