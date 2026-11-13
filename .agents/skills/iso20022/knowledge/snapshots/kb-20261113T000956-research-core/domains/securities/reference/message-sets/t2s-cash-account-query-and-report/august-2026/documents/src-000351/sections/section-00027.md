---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.10 MaximumMonthlyReceivedValue <MaxMnthlyRcvdVal>"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.10 MaximumMonthlyReceivedValue <MaxMnthlyRcvdVal>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
2.4.5.10  MaximumMonthlyReceivedValue <MaxMnthlyRcvdVal>
Presence: [0..1]
Definition: Maximum monthly average of the received amounts over a year (that is, payments coming
in).
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.11  MinimumMonthlyTransactionNumber <MinMnthlyTxNb>
Presence: [0..1]
Definition: Minimum monthly average of the number of payments (coming in and going out) over a year.
Datatype: "Max5NumericText" on page 184
2.4.5.12  MaximumMonthlyTransactionNumber <MaxMnthlyTxNb>
Presence: [0..1]
Definition: Maximum monthly average of the number of payments (coming in and going out) over a
year.
Datatype: "Max5NumericText" on page 184
2.4.5.13  MinimumAverageBalance <MinAvrgBal>
Presence: [0..1]
Definition: Minimum average balance, that is, sum of the end of day balances over a month divided by
the number of business days in the month.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.14  MaximumAverageBalance <MaxAvrgBal>
Presence: [0..1]
Definition: Maximum average balance, that is, sum of the end of day balances over a month divided by
the number of business days in the month.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.15  AccountPurpose <AcctPurp>
Presence: [0..1]
Definition: Specifies the purpose of the account.
Datatype: "Max140Text" on page 182
2.4.5.16  MinimumFloorNotificationAmount <MinFlrNtfctnAmt>
Presence: [0..1]
Definition: Minimum floor notification amount, that is, the value of the balance under which a notification
will be sent to the account owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.17  MaximumFloorNotificationAmount <MaxFlrNtfctnAmt>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 31 August 2026
```

