---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.2 CostsAndCharges2", "66.1.8.2.2 IndividualCostOrCharge <IndvCostOrChrg>", "66.1.8.2.2.3 Amount <Amt>"]
file_pages: [4449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.2.2.3 Amount <Amt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4449 to 4449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4449

```text
Definition: Specifies if the cost or charge is ex ante (intended) or post ante (actual).
Datatype: "IntendedOrActual2Code" on page 5311
CodeName Name Definition
ANTE ExAnte Ex ante (intended).
POST ExPost Ex post (actual).
66.1.8.2.2.3  Amount <Amt>
Presence: [0..1]
Definition: Amount of the cost or charge.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.8.2.2.4  Sign <Sgn>
Presence: [0..1]
Definition: Indicates a negative amount.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
66.1.8.2.2.5  Rate <Rate>
Presence: [0..1]
Definition: Rate of the cost or charge.
Datatype: "PercentageRate" on page 5401
66.1.8.2.2.6  ReferencePeriod <RefPrd>
Presence: [0..1]
Definition: Start date and end date of the reference period for the ex post cost or charge. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 08090 and
08100.
ReferencePeriod <RefPrd> contains the following Period15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1] Date 4450
   EndDate <EndDt> [1..1] Date 4450
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4449 May 2026
```

