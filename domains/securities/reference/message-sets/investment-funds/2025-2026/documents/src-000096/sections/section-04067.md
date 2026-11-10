---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.250 ValuationTiming1Code"]
file_pages: [5388]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.250 ValuationTiming1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5388 to 5388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5388

```text
CodeName Name Definition
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
66.2.2.250  ValuationTiming1Code
Definition: Specifies how the price valuation timing is done based on the timeline defined in the
prospectus.
Type: CodeSet
CodeName Name Definition
EXCP Exceptional Price valuation is done exceptionally,
outside the timeframe specified in the
prospectus.
USUA Usual Price valuation is done within the
timeframe specified in the prospectus.
PATC Particular Price valuation that is done outside the
usual timeframe, but in conformance
with a case specified in the prospectus,
eg, market closing day.
66.2.2.251  WaivingInstruction1Code
Definition: Specifies the form of the rebate when commission is waived.
Type: CodeSet
CodeName Name Definition
WICA WaiveInCash Form of commission waived is cash.
WIUN WaiveInUnits Form of commission waived is additional
units of a financial instrument.
66.2.3 Date
66.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
66.2.4 DateTime
66.2.4.1  ISODateTime
Definition: A particular point in the progression of time defined by a mandatory date and a mandatory
time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with
UTC offset format (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm), or local time format (YYYY-MM-
DDThh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second
Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5388 May 2026
```

