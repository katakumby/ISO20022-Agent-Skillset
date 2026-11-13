---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.4 Date"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.4 Date

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
CodeName Name Definition
QTR4 FourthQuarter Tax is related to the forth quarter of the
period.
HLF1 FirstHalf Tax is related to the first half of the
period.
HLF2 SecondHalf Tax is related to the second half of the
period.
6.2.4 Date
6.2.4.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
6.2.5 DateTime
6.2.5.1  ISODateTime
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
6.2.6 IdentifierSet
6.2.6.1  AnyBICDec2014Identifier
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages -
Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; AnyBICIdentifier
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 603 March 2026
```

