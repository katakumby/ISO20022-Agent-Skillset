---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.2 Message Datatypes", "4.2.4 DateTime"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.4 DateTime

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
4.2.4 DateTime
4.2.4.1  ISODateTime
Definition: A particular point in the progression of time defined by a mandatory date and a mandatory
time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with
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
4.2.5 IdentifierSet
4.2.5.1  AnyBICDec2014Identifier
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
4.2.5.2  BICFIDec2014Identifier
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362: 2014 - "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; BICIdentifier
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
79 March 2024
```

