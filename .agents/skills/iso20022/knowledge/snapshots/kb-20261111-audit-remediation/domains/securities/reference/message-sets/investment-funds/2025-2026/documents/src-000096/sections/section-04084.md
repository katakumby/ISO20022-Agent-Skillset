---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.9 Text", "66.2.9.16 PhoneNumber"]
file_pages: [5405]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.9.16 PhoneNumber

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5405 to 5405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5405

```text
66.2.9.16  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
66.2.9.17  PreviousAll
Definition: Indicates that the investment plan issued during all the previous years have to be transferred.
Type: Text
Format
pattern ALL
66.2.10 Time
66.2.10.1  ISOTime
Definition: A particular point in the progression of time in a calendar day expressed in either UTC time
format (hh:mm:ss.sssZ), local time with UTC offset format (hh:mm:ss.sss+/-hh:mm), or local time format
(hh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second Edition -
W3C Recommendation 28 October 2004" which is aligned with ISO 8601.
Note on the time format:
1) beginning / end of calendar day
00:00:00 = the beginning of a calendar day
24:00:00 = the end of a calendar day
2) fractions of second in time format
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: Time
66.2.11 Year
66.2.11.1  ISOYear
Definition: Year represented by YYYY (ISO 8601).
Type: Year
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5405 May 2026
```

