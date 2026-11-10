---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>"]
file_pages: [79, 80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1 Account <Acct>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 79 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Constraints
• ContractDates1Rule
ContractDates/TargetGoLiveDate and ContractDates/GoLiveDate should not be used as part of an
account closing process.
• ContractDates2Rule
ContractDates/ClosingDate should not be used as part of an account opening and maintenance
process.
3.4.4.2.1  Account <Acct>
Presence: [1..1]
Definition: Characteristics of the account.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 79 August 2026
```

## File page 80

```text
Account <Acct> contains the following CustomerAccount8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 81
   Name <Nm> [0..1] Text 81
   Status <Sts> [0..1] CodeSet 81
   Type <Tp> [0..1] ± 81
   Currency <Ccy> [1..1] CodeSet C1 82
   Proxy <Prxy> [0..1] ± 82
   MonthlyPaymentValue <MnthlyPmtVal> [0..1] Amount 82
   MonthlyReceivedValue <MnthlyRcvdVal> [0..1] Amount 82
   MonthlyTransactionNumber <MnthlyTxNb> [0..1] Text 82
   AverageBalance <AvrgBal> [0..1] Amount 82
   AccountPurpose <AcctPurp> [0..1] Text 83
   FloorNotificationAmount <FlrNtfctnAmt> [0..1] Amount 83
   CeilingNotificationAmount <ClngNtfctnAmt> [0..1] Amount 83
   StatementFrequencyAndFormat <StmtFrqcyAndFrmt> [0..*]  83
     Frequency <Frqcy> [1..1] CodeSet 83
     CommunicationMethod <ComMtd> [1..1]  84
{Or       Code <Cd> [1..1] CodeSet 84
Or}       Proprietary <Prtry> [1..1] Text 85
     DeliveryAddress <DlvryAdr> [1..1] Text 85
     Format <Frmt> [1..1]  85
{Or       Code <Cd> [1..1] CodeSet 85
Or}       Proprietary <Prtry> [1..1] Text 85
   ClosingDate <ClsgDt> [0..1] Date 85
   Restriction <Rstrctn> [0..*]  85
     RestrictionType <RstrctnTp> [1..1]  86
{Or       Code <Cd> [1..1] Text 86
Or}       Proprietary <Prtry> [1..1] ± 86
     ValidFrom <VldFr> [1..1] DateTime 86
     ValidUntil <VldUntil> [0..1] DateTime 87
   OpeningDate <OpngDt> [0..1] Date 87
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 80 August 2026
```

