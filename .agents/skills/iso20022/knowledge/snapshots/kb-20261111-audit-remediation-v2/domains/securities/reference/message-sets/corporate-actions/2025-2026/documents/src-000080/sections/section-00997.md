---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.139 UnicodeChartsCode"]
file_pages: [1243]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.139 UnicodeChartsCode

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1243 to 1243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1243

```text
16.2.2.139  UnicodeChartsCode
Definition: codelist containing the names of the UNICODE code block name as specified on http://
unicode.org/Public/UNIDATA/Blocks.txt.
Type: CodeSet
Constraints
• ValidationByTable
16.2.2.140  WithholdingTaxRateType1Code
Definition: Specifies the type of withholding tax rate.
Type: CodeSet
CodeName Name Definition
BWIT BackUpWithholding Withholding tax related to payments
subject to back up withholding.
FTCA FATCATax Withholding tax related to income
subject to FATCA (Foreign Account Tax
Compliance Act).
NRAT NRATax Withholding tax related to income
subject to NRA (Non Resident Alien).
16.2.3 Date
16.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
16.2.4 DateTime
16.2.4.1  ISODateTime
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1243 February 2026
```

