---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.51 WarrantStyle1Code"]
file_pages: [529]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.51 WarrantStyle1Code

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 529 to 529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 529

```text
13.2.2.51  WarrantStyle1Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
13.2.3 Date
13.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
13.2.4 DateTime
13.2.4.1  ISODateTime
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 529 March 2024
```

