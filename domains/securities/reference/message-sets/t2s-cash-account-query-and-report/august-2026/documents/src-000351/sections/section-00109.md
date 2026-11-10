---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["6 reda.040.001.01 CashAccountAuditTrailReportV01", "6.4 Message Building Blocks", "6.4.2 ReportOrError <RptOrErr>", "6.4.2.1 CashAccountAuditTrailReport <CshAcctAudtTrlRpt>", "6.4.2.1.1 CashAccountAuditTrailOrError <CshAcctAudtTrlOrErr>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.040.001.01"]
---

# 6.4.2.1.1 CashAccountAuditTrailOrError <CshAcctAudtTrlOrErr>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
CashAccountAuditTrailReport <CshAcctAudtTrlRpt> contains the following
CashAccountAuditTrailReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountAuditTrailOrError
<CshAcctAudtTrlOrErr>
[1..1]  123
{Or     AuditTrail <AudtTrl> [1..*]  124
       FieldName <FldNm> [1..1] Text 124
       OldFieldValue <OdFldVal> [1..1] Text 124
       NewFieldValue <NewFldVal> [1..1] Text 125
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 125
       InstructingUser <InstgUsr> [1..1] Text 125
       ApprovingUser <ApprvgUsr> [0..1] Text 125
Or}     BusinessError <BizErr> [1..*]  125
       Error <Err> [1..1]  125
{Or         Code <Cd> [1..1] CodeSet 126
Or}         Proprietary <Prtry> [1..1] Text 126
       Description <Desc> [0..1] Text 126
   DatePeriod <DtPrd> [0..1]  126
{Or     FromDate <FrDt> [1..1] Date 126
Or     ToDate <ToDt> [1..1] Date 126
Or     FromToDate <FrToDt> [1..1] ± 126
Or     EqualDate <EQDt> [1..1] Date 127
Or}     NotEqualDate <NEQDt> [1..1] Date 127
   CashAccountIdentification <CshAcctId> [1..1] ± C4, C3 127
6.4.2.1.1  CashAccountAuditTrailOrError <CshAcctAudtTrlOrErr>
Presence: [1..1]
Definition: Identifies the returned cash account reference data or error information.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.040.001.01 CashAccountAuditTrailReportV01
Target2-Securities - Cash Account Query and Report 123 August 2026
```

