---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.5 Currency <Ccy>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.5 Currency <Ccy>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
3.4.4.2.1.5  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 173
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.4.2.1.6  Proxy <Prxy>
Presence: [0..1]
Definition: Specifies an alternate assumed name for the identification of the account.
Proxy <Prxy> contains the following elements (see "ProxyAccountIdentification1" on page 132 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  132
{Or     Code <Cd> [1..1] CodeSet 132
Or}     Proprietary <Prtry> [1..1] Text 132
   Identification <Id> [1..1] Text 132
3.4.4.2.1.7  MonthlyPaymentValue <MnthlyPmtVal>
Presence: [0..1]
Definition: Monthly average of the payment amounts (that is, payments going out) over a year.
Datatype: "ImpliedCurrencyAndAmount" on page 172
3.4.4.2.1.8  MonthlyReceivedValue <MnthlyRcvdVal>
Presence: [0..1]
Definition: Monthly average of the received amounts over a year (that is, payments coming in).
Datatype: "ImpliedCurrencyAndAmount" on page 172
3.4.4.2.1.9  MonthlyTransactionNumber <MnthlyTxNb>
Presence: [0..1]
Definition: Monthly average of the number of payments (coming in and going out) over a year.
Datatype: "Max5NumericText" on page 184
3.4.4.2.1.10  AverageBalance <AvrgBal>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 82 August 2026
```

