---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.10 Currency <Ccy>"]
file_pages: [99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.10 Currency <Ccy>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 99 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
CodeName Name Definition
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
3.4.8.10  Currency <Ccy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.8.11  CustomDate <CstmDt>
Presence: [0..1]
Definition: Indicates an instruction to override an investment's default start and/or end date with a
custom date.
CustomDate <CstmDt> contains the following elements (see "DateTimePeriod2" on page 261 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 261
   ToDateTime <ToDtTm> [0..1] DateTime 261
3.4.8.12  Haircut <Hrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Datatype: "PercentageRate" on page 667
3.4.8.13  InsuredIndicator <InsrdInd>
Presence: [0..1]
Definition: Identifies whether the lender is assured partial or full payment by a third party if the borrower
defaults.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 99 February 2025
```

