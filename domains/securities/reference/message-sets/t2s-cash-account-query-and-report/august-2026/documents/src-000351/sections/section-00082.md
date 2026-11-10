---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.4 Mandate <Mndt>", "3.4.4.2.4.5 MandateHolder <MndtHldr>", "3.4.4.2.4.5.3 Authorisation <Authstn>", "3.4.4.2.4.5.3.1 MaximumAmountByTransaction <MaxAmtByTx>", "3.4.4.2.4.5.3.1.2 NotLimited <NotLtd>"]
file_pages: [96]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.4.5.3.1.2 NotLimited <NotLtd>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 96 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.4.2.4.5.3.1.2  NotLimited <NotLtd>
Presence: [1..1]
Definition: Unlimited amount.
Datatype: "Unlimited9Text" on page 185
3.4.4.2.4.5.3.2  MaximumAmountByPeriod <MaxAmtByPrd>
Presence: [0..*]
Definition: Maximum amount allowed over a specific period of time.
MaximumAmountByPeriod <MaxAmtByPrd> contains the following MaximumAmountByPeriod1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumAmount <MaxAmt> [1..1] Amount C1, C8 96
   NumberOfDays <NbOfDays> [1..1] Text 97
3.4.4.2.4.5.3.2.1  MaximumAmount <MaxAmt>
Presence: [1..1]
Definition: Maximum amount allowed over a specific period of time.
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 171
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 96 August 2026
```

