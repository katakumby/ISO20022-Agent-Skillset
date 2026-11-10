---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.6 AccountReturnCriteria <AcctRtrCrit>", "2.4.6.1 Identification <Id>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.6.1 Identification <Id>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
AccountReturnCriteria <AcctRtrCrit> contains the following CustomerAccountReturnCriteria1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Indicator 41
   Name <Nm> [1..1] Indicator 41
   Status <Sts> [1..1] Indicator 42
   Type <Tp> [1..1] Indicator 42
   Currency <Ccy> [1..1] Indicator 42
   MonthlyPaymentValue <MnthlyPmtVal> [1..1] Indicator 42
   MonthlyReceivedValue <MnthlyRcvdVal> [1..1] Indicator 42
   MonthlyTransactionNumber <MnthlyTxNb> [1..1] Indicator 43
   AverageBalance <AvrgBal> [1..1] Indicator 43
   AccountPurpose <AcctPurp> [1..1] Indicator 43
   FloorNotificationAmount <FlrNtfctnAmt> [1..1] Indicator 43
   CeilingNotificationAmount <ClngNtfctnAmt> [1..1] Indicator 43
   StatementCycle <StmtCycl> [1..1] Indicator 44
   ClosingDate <ClsgDt> [1..1] Indicator 44
   Restriction <Rstrctn> [1..1] Indicator 44
   OpeningDate <OpngDt> [1..1] Indicator 44
   AccountOwner <AcctOwnr> [1..1] Indicator 44
   ReferenceAccount <RefAcct> [1..1] Indicator 44
   Proprietary <Prtry> [0..*]  45
     SchemeName <SchmeNm> [0..1] Text 45
     Issuer <Issr> [0..1] Text 45
2.4.6.1  Identification <Id>
Presence: [1..1]
Definition: Indicates if this field must be present in the response.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 181):
• Meaning When True: Yes
• Meaning When False: No
2.4.6.2  Name <Nm>
Presence: [1..1]
Definition: Indicates if this field must be present in the response.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 41 August 2026
```

