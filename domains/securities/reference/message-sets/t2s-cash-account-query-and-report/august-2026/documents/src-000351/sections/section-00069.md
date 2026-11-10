---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.11 AccountPurpose <AcctPurp>"]
file_pages: [83]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.11 AccountPurpose <AcctPurp>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 83 to 83.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Definition: Sum of the end of day balances over a month divided by the number of business days in the
month.
Datatype: "ImpliedCurrencyAndAmount" on page 172
3.4.4.2.1.11  AccountPurpose <AcctPurp>
Presence: [0..1]
Definition: Specifies the purpose of the account.
Datatype: "Max140Text" on page 182
3.4.4.2.1.12  FloorNotificationAmount <FlrNtfctnAmt>
Presence: [0..1]
Definition: Specifies the value of the balance under which a notification will be sent to the account
owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
3.4.4.2.1.13  CeilingNotificationAmount <ClngNtfctnAmt>
Presence: [0..1]
Definition: Specifies the value of the balance above which a notification will be sent to the account
owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
3.4.4.2.1.14  StatementFrequencyAndFormat <StmtFrqcyAndFrmt>
Presence: [0..*]
Definition: Specifies how often statements (for audit purposes) will be sent, in which format, to which
address.
StatementFrequencyAndFormat <StmtFrqcyAndFrmt> contains the following
StatementFrequencyAndForm1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Frequency <Frqcy> [1..1] CodeSet 83
   CommunicationMethod <ComMtd> [1..1]  84
{Or     Code <Cd> [1..1] CodeSet 84
Or}     Proprietary <Prtry> [1..1] Text 85
   DeliveryAddress <DlvryAdr> [1..1] Text 85
   Format <Frmt> [1..1]  85
{Or     Code <Cd> [1..1] CodeSet 85
Or}     Proprietary <Prtry> [1..1] Text 85
3.4.4.2.1.14.1  Frequency <Frqcy>
Presence: [1..1]
Definition: Specifies the frequency for sending statements.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 83 August 2026
```

