---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.9 Text", "16.2.9.22 Max8000Text"]
file_pages: [1252]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.9.22 Max8000Text

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1252 to 1252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1252

```text
Type: Text
Format
minLength 1
maxLength 70
16.2.9.22  Max8000Text
Definition: Specifies a character string with a maximum length of 8000 characters.
Type: Text
Format
minLength 1
maxLength 8000
16.2.9.23  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
16.2.10 Time
16.2.10.1  ISOTime
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1252 February 2026
```

