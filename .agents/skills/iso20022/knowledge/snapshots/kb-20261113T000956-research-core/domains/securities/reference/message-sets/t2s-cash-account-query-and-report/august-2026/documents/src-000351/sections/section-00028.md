---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.18 MinimumCeilingNotificationAmount <MinClngNtfctnAmt>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.18 MinimumCeilingNotificationAmount <MinClngNtfctnAmt>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
Definition: Maximum floor notification amount, that is, the value of the balance under which a notification
will be sent to the account owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.18  MinimumCeilingNotificationAmount <MinClngNtfctnAmt>
Presence: [0..1]
Definition: Minimum ceiling notification amount, that is, the value of the balance above which a
notification will be sent to the account owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.19  MaximumCeilingNotificationAmount <MaxClngNtfctnAmt>
Presence: [0..1]
Definition: Maximum ceiling notification amount, that is, the value of the balance above which a
notification will be sent to the account owner.
Datatype: "ImpliedCurrencyAndAmount" on page 172
2.4.5.20  StatementFrequencyAndFormat <StmtFrqcyAndFrmt>
Presence: [0..*]
Definition: Specifies how often statements (for audit purposes) will be sent, in which format, to which
address.
StatementFrequencyAndFormat <StmtFrqcyAndFrmt> contains the following
StatementFrequencyAndForm1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Frequency <Frqcy> [1..1] CodeSet 32
   CommunicationMethod <ComMtd> [1..1]  33
{Or     Code <Cd> [1..1] CodeSet 33
Or}     Proprietary <Prtry> [1..1] Text 33
   DeliveryAddress <DlvryAdr> [1..1] Text 34
   Format <Frmt> [1..1]  34
{Or     Code <Cd> [1..1] CodeSet 34
Or}     Proprietary <Prtry> [1..1] Text 34
2.4.5.20.1  Frequency <Frqcy>
Presence: [1..1]
Definition: Specifies the frequency for sending statements.
Datatype: "Frequency7Code" on page 178
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 32 August 2026
```

