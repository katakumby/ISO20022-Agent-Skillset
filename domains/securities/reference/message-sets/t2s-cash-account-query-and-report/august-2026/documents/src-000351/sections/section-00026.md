---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.6 Proxy <Prxy>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.6 Proxy <Prxy>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
Definition: Medium of exchange of value.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 173
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
2.4.5.6  Proxy <Prxy>
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
2.4.5.7  MinimumMonthlyPaymentValue <MinMnthlyPmtVal>
Presence: [0..1]
Definition: Minimum monthly average of the payment amounts (that is, payments going out) over a year.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.8  MaximumMonthlyPaymentValue <MaxMnthlyPmtVal>
Presence: [0..1]
Definition: Maximum monthly average of the payment amounts (that is, payments going out) over a
year.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.9  MinimumMonthlyReceivedValue <MinMnthlyRcvdVal>
Presence: [0..1]
Definition: Minimum monthly average of the received amounts over a year (that is, payments coming
in).
Datatype: "ImpliedCurrencyAndAmount" on page 172
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 30 August 2026
```

