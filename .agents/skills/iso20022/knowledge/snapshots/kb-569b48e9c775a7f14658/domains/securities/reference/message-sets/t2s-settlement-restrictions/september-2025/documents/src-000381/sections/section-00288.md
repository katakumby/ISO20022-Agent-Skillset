---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.5 IdentifierSet"]
file_pages: [341]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.5 IdentifierSet

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 341 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
9.2.5 IdentifierSet
9.2.5.1  AnyBICDec2014Identifier
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
9.2.5.2  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
9.2.5.3  ISINOct2015Identifier
Definition: The International Securities Identification Number is a code allocated to financial instruments
as well as referential instruments, as described in the ISO 6166 standard, associated with the minimum
descriptive data. The ISIN consists of a prefix using the alpha-2 country codes or reserved codes
specified in ISO 3166 or other prefixes as may be determined by the Registration Authority for the ISO
6166 standard, a nine characters (alphanumeric) basic code and a check digit.
Note: this identifier also supports the new version of the standard, which was published in 2021 (ISO
6166:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 341 September 2025
```

