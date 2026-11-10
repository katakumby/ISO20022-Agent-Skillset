---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.5 IdentifierSet"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.5 IdentifierSet

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
13.2.5 IdentifierSet
13.2.5.1  AnyBICDec2014Identifier
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
13.2.5.2  CFIOct2015Identifier
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or
registered.
Note: this identifier also supports the updated versions of the standard, which were published in 2019
and 2021 (ISO 10962 :2019 and ISO 10962:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; CFIIdentifier
Format
pattern [A-Z]{6,6}
13.2.5.3  ISIN2021Identifier
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Format
pattern [A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 530 March 2024
```

