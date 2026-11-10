---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["54 reda.034.001.01 SecuritiesAuditTrailReportV01", "54.4 Message Building Blocks", "54.4.2 ReportOrError <RptOrErr>", "54.4.2.1 SecuritiesAuditTrailReport <SctiesAudtTrlRpt>", "54.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>"]
file_pages: [2229]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 54.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2229 to 2229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2229

```text
SecuritiesAuditTrailReport <SctiesAudtTrlRpt> contains the following SecuritiesAuditTrailReport4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr> [1..1]  2229
{Or     AuditTrail <AudtTrl> [1..*]  2230
       FieldName <FldNm> [1..1] Text 2230
       OldFieldValue <OdFldVal> [1..1] Text 2230
       NewFieldValue <NewFldVal> [1..1] Text 2231
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 2231
       InstructingUser <InstgUsr> [1..1] Text 2231
       ApprovingUser <ApprvgUsr> [0..1] Text 2231
Or}     BusinessError <BizErr> [1..*]  2231
       Error <Err> [1..1]  2231
{Or         Code <Cd> [1..1] CodeSet 2232
Or}         Proprietary <Prtry> [1..1] Text 2232
       Description <Desc> [0..1] Text 2232
   DatePeriod <DtPrd> [0..1]  2232
{Or     FromDate <FrDt> [1..1] Date 2232
Or     ToDate <ToDt> [1..1] Date 2232
Or     FromToDate <FrToDt> [1..1] ± 2232
Or     EqualDate <EQDt> [1..1] Date 2233
Or}     NotEqualDate <NEQDt> [1..1] Date 2233
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
2233
54.4.2.1.1  SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>
Presence: [1..1]
Definition: Identifies the returned securities reference data or error information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities 2229 August 2026
```

