---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.9 Text", "6.2.9.23 Min3Max4NumericText"]
file_pages: [918]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.9.23 Min3Max4NumericText

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 918 to 918.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 918

```text
6.2.9.23  Min3Max4NumericText
Definition: Specifies a numeric string with a minimum length of 3 digits, and a maximum length of 4
digits.
Type: Text
Format
pattern [0-9]{3,4}
6.2.9.24  Min8Max28NumericText
Definition: Specifies a numeric string with a minimum length of 8 digits, and a maximum length of 28
digits.
Type: Text
Format
pattern [0-9]{8,28}
6.2.9.25  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
6.2.10 Time
6.2.10.1  ISOTime
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
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
918 March 2026
```

