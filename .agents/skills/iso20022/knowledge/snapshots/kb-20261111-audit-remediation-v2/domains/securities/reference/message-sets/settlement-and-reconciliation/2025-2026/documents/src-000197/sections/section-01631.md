---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.5 IdentifierSet", "35.2.5.5 IBAN2007Identifier"]
file_pages: [2187]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.5.5 IBAN2007Identifier

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2187 to 2187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2187

```text
35.2.5.5  IBAN2007Identifier
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
35.2.5.6  ISINOct2015Identifier
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
35.2.5.7  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
35.2.5.8  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2187 March 2026
```

