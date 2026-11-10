---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.4 Mandate <Mndt>", "3.4.4.2.4.5 MandateHolder <MndtHldr>", "3.4.4.2.4.5.2 SignatureOrder <SgntrOrdr>"]
file_pages: [95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.4.5.2 SignatureOrder <SgntrOrdr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 95 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 95

```text
3.4.4.2.4.5.2  SignatureOrder <SgntrOrdr>
Presence: [0..1]
Definition: Order in which the mandate holder has to sign.
Datatype: "Max15PlusSignedNumericText" on page 182
3.4.4.2.4.5.3  Authorisation <Authstn>
Presence: [1..1]
Definition: Authorisation granted to a mandate holder.
Authorisation <Authstn> contains the following Authorisation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumAmountByTransaction <MaxAmtByTx> [0..1]  95
{Or     Amount <Amt> [1..1] Amount C1, C8 95
Or}     NotLimited <NotLtd> [1..1] Text 96
   MaximumAmountByPeriod <MaxAmtByPrd> [0..*]  96
     MaximumAmount <MaxAmt> [1..1] Amount C1, C8 96
     NumberOfDays <NbOfDays> [1..1] Text 97
   MaximumAmountByBulkSubmission
<MaxAmtByBlkSubmissn>
[0..1]  97
{Or     Amount <Amt> [1..1] Amount C1, C8 97
Or}     NotLimited <NotLtd> [1..1] Text 97
3.4.4.2.4.5.3.1  MaximumAmountByTransaction <MaxAmtByTx>
Presence: [0..1]
Definition: Maximum amount allowed by the mandate for each transaction.
MaximumAmountByTransaction <MaxAmtByTx> contains one of the following
FixedAmountOrUnlimited1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C8 95
Or}   NotLimited <NotLtd> [1..1] Text 96
3.4.4.2.4.5.3.1.1  Amount <Amt>
Presence: [1..1]
Definition: Fixed amount.
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 171
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 95 August 2026
```

