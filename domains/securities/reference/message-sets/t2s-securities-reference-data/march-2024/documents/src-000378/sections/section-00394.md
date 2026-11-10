---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.8 RateAndAmountFormat1Choice", "13.1.10.8.1 Rate <Rate>"]
file_pages: [487]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.8.1 Rate <Rate>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 487 to 487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 487

```text
13.1.10.8.1  Rate <Rate>
Presence: [1..1]
Definition: The value is expressed as a rate.
Datatype: "PercentageRate" on page 532
13.1.10.8.2  Amount <Amt>
Presence: [1..1]
Definition: The value is expressed as a currency and amount.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.10.8.3  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: No value is specified.
NotSpecifiedRate <NotSpcfdRate> contains one of the following RateType12FormatChoice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 487
Or}   Proprietary <Prtry> [1..1] ± 488
13.1.10.8.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of rate.
Datatype: "RateType12Code" on page 522
CodeName Name Definition
OPEN Open Rate has not been established.
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 487 March 2024
```

