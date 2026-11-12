---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.2 CodeSet", "22.2.2.117 UnderlyingInterestRateType3Code"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.2.117 UnderlyingInterestRateType3Code

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
22.2.2.117  UnderlyingInterestRateType3Code
Definition: Specifies the type of an underlying contract for interest rate derivatives.
Type: CodeSet
CodeName Name Definition
BOND Bond Underlying is a bond.
BNDF BondFuture Underlying is a bond future.
INTR InterestRate Underlying is interest rate.
IFUT InterestRateFutureFRA Underlying is an interest rate future or a
forward rate agreement (FRA).
22.2.2.118  VariationType1Code
Definition: Specifies the type of variation.
Type: CodeSet
CodeName Name Definition
DECR Decrease Decrease to undertaking amount.
INCR Increase Increase to undertaking amount.
22.2.3 Date
22.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
22.2.4 DateTime
22.2.4.1  ISODateTime
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
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
449 July 2025
```

