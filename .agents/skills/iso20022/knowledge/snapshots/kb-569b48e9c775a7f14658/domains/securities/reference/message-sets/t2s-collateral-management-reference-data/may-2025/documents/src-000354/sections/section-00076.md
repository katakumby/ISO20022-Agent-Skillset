---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.5 IdentifierSet"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.5 IdentifierSet

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
UTC offset format (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm), or local time format (YYYY-MM-
DDThh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second
Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.
Note on the time format:
1) beginning / end of calendar day
00:00:00 = the beginning of a calendar day
24:00:00 = the end of a calendar day
2) fractions of second in time format
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
10.2.5 IdentifierSet
10.2.5.1  AnyBICDec2014Identifier
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
10.2.5.2  ISINOct2015Identifier
Definition: The International Securities Identification Number is a code allocated to financial instruments
as well as referential instruments, as described in the ISO 6166 standard, associated with the minimum
descriptive data. The ISIN consists of a prefix using the alpha-2 country codes or reserved codes
specified in ISO 3166 or other prefixes as may be determined by the Registration Authority for the ISO
6166 standard, a nine characters (alphanumeric) basic code and a check digit.
Note: this identifier also supports the new version of the standard, which was published in 2021 (ISO
6166:2021) as there is no update in the pattern.
Type: IdentifierSet
Identification scheme: ANNA; ISINIdentifier
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 81 May 2025
```

