---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.4 Mandate <Mndt>", "3.4.4.2.4.1 Identification <Id>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.4.1 Identification <Id>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
Mandate <Mndt> contains the following OperationMandate7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 90
   ApplicableChannel <AplblChanl> [1..*]  91
{Or     Code <Cd> [1..1] CodeSet 91
Or}     Proprietary <Prtry> [1..1] Text 91
   RequiredSignatureNumber <ReqrdSgntrNb> [1..1] Text 91
   SignatureOrderIndicator <SgntrOrdrInd> [1..1] Indicator 91
   MandateHolder <MndtHldr> [0..*]  92
     PartyOrGroup <PtyOrGrp> [1..1]  92
{Or       GroupIdentification <GrpId> [1..1] Text 92
Or}       Party <Pty> [1..1]  93
         Party <Pty> [1..1] ± 93
         Certificate <Cert> [0..1] Binary 94
     SignatureOrder <SgntrOrdr> [0..1] Text 95
     Authorisation <Authstn> [1..1]  95
       MaximumAmountByTransaction <MaxAmtByTx> [0..1]  95
{Or         Amount <Amt> [1..1] Amount C1, C8 95
Or}         NotLimited <NotLtd> [1..1] Text 96
       MaximumAmountByPeriod <MaxAmtByPrd> [0..*]  96
         MaximumAmount <MaxAmt> [1..1] Amount C1, C8 96
         NumberOfDays <NbOfDays> [1..1] Text 97
       MaximumAmountByBulkSubmission
<MaxAmtByBlkSubmissn>
[0..1]  97
{Or         Amount <Amt> [1..1] Amount C1, C8 97
Or}         NotLimited <NotLtd> [1..1] Text 97
   BankOperation <BkOpr> [1..*] ± C9, C10 97
   StartDate <StartDt> [0..1] Date 98
   EndDate <EndDt> [0..1] Date 98
3.4.4.2.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of the mandate.
Datatype: "Max35Text" on page 183
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 90 August 2026
```

