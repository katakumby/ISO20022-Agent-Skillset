---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.2 SearchCriteria <SchCrit>", "8.4.2.2.2.2.8 UsedPercentage <UsdPctg>", "8.4.2.2.2.2.8.4 Equal <EQ>"]
file_pages: [387]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.2.8.4 Equal <EQ>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 387 to 387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 387

```text
8.4.2.2.2.2.8.4  Equal <EQ>
Presence: [1..1]
Definition: Exact percentage rate must match to be considered valid.
Datatype: "PercentageRate" on page 887
8.4.2.2.2.2.8.5  NotEqual <NEQ>
Presence: [1..1]
Definition: Value that percentage rate must not match to be considered valid.
Datatype: "PercentageRate" on page 887
8.4.2.2.2.2.9  LimitCurrency <LmtCcy>
Presence: [0..1]
Definition: Currency unit used to specify the limit amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
8.4.2.2.2.2.10  LimitAmount <LmtAmt>
Presence: [0..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
LimitAmount <LmtAmt> contains one of the following elements (see "ActiveAmountRange3Choice"
on page 791 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 791
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 791
8.4.2.2.2.2.11  LimitValidAsOfDate <LmtVldAsOfDt>
Presence: [0..1]
Definition: Range of dates when the limit becomes valid.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 387 February 2025
```

