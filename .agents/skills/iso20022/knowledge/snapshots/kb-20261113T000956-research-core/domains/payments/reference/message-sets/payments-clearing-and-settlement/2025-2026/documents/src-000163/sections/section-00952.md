---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.10 Text", "10.2.10.20 SHA256SignatureText"]
file_pages: [1247]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.10.20 SHA256SignatureText

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1247 to 1247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1247

```text
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
10.2.10.20  SHA256SignatureText
Definition: Specifies a character string with an exact length of 32 binary bytes (64 hexadecimal text
characters).
Used only for hex binary data only, supports only characters A-F and 0-9.
Type: Text
Format
pattern ([0-9A-F][0-9A-F]){32}
10.2.11 Time
10.2.11.1  ISOTime
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
10.2.12 Year
10.2.12.1  ISOYear
Definition: Year represented by YYYY (ISO 8601).
Type: Year
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1247 March 2026
```

