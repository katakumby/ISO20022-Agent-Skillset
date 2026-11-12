---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.3 Date"]
file_pages: [662]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.3 Date

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 662 to 662.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 662

```text
CodeName Name Definition
INTT InterestType Interest type does not match.
CUFC CurrentFactor Current factor does not match.
LTME LendingTransactionMethod Lending transaction method does not
match.
ENFC EndFactor End factor does not match.
CLSE ClearingSegment Counterparty's instruction is for
settlement through clearing segment,
your instruction is not, or vice versa.
7.2.3 Date
7.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
7.2.4 DateTime
7.2.4.1  ISODateTime
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
7.2.5 IdentifierSet
7.2.5.1  AnyBICDec2014Identifier
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages -
Business identifier code (BIC)".
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 662 February 2025
```

