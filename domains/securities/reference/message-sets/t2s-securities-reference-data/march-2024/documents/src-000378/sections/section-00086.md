---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["12 reda.034.001.01 SecuritiesAuditTrailReportV01", "12.2 Structure"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 12.2 Structure

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAudtTrlRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1]  136
     MessageIdentification <MsgId> [1..1] Text 137
     CreationDateTime <CreDtTm> [0..1] DateTime 137
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 137
   ReportOrError <RptOrErr> [1..1]  137
{Or     SecuritiesAuditTrailReport <SctiesAudtTrlRpt> [1..*]  138
       SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr> [1..1]  139
{Or         AuditTrail <AudtTrl> [1..*]  140
           FieldName <FldNm> [1..1] Text 140
           OldFieldValue <OdFldVal> [1..1] Text 140
           NewFieldValue <NewFldVal> [1..1] Text 141
           OperationTimeStamp <OprTmStmp> [1..1] DateTime 141
           InstructingUser <InstgUsr> [1..1] Text 141
           ApprovingUser <ApprvgUsr> [0..1] Text 141
Or}         BusinessError <BizErr> [1..*]  141
           Error <Err> [1..1]  141
{Or             Code <Cd> [1..1] CodeSet 142
Or}             Proprietary <Prtry> [1..1] Text 142
           Description <Desc> [0..1] Text 142
       DatePeriod <DtPrd> [0..1]  142
{Or         FromDate <FrDt> [1..1] Date 142
Or         ToDate <ToDt> [1..1] Date 142
Or         FromToDate <FrToDt> [1..1] ± 142
Or         EqualDate <EQDt> [1..1] Date 143
Or}         NotEqualDate <NEQDt> [1..1] Date 143
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
143
Or}     OperationalError <OprlErr> [1..*]  144
       Error <Err> [1..1]  144
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 135 March 2024
```

