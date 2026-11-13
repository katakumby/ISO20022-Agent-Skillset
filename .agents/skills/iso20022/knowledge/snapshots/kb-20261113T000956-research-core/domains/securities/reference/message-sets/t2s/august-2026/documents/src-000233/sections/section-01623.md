---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "57.4 Message Building Blocks", "57.4.2 ReportOrError <RptOrErr>", "57.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "57.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>"]
file_pages: [2250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 57.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2250 to 2250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2250

```text
SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt> contains the following
SecuritiesAccountAuditTrailReport3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountAuditTrailOrError
<SctiesAcctAudtTrlOrErr>
[1..1]  2250
{Or     AuditTrail <AudtTrl> [1..*]  2251
       FieldName <FldNm> [1..1] Text 2251
       OldFieldValue <OdFldVal> [1..1] Text 2251
       NewFieldValue <NewFldVal> [1..1] Text 2252
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 2252
       InstructingUser <InstgUsr> [1..1] Text 2252
       ApprovingUser <ApprvgUsr> [0..1] Text 2252
Or}     BusinessError <BizErr> [1..*]  2252
       Error <Err> [1..1]  2252
{Or         Code <Cd> [1..1] CodeSet 2253
Or}         Proprietary <Prtry> [1..1] Text 2253
       Description <Desc> [0..1] Text 2253
   DatePeriod <DtPrd> [0..1]  2253
{Or     FromDate <FrDt> [1..1] Date 2253
Or     ToDate <ToDt> [1..1] Date 2253
Or     FromToDate <FrToDt> [1..1] ± 2253
Or     EqualDate <EQDt> [1..1] Date 2254
Or}     NotEqualDate <NEQDt> [1..1] Date 2254
   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 2254
57.4.2.1.1  SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>
Presence: [1..1]
Definition: Provides the returned securities account reference data or error information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2250 August 2026
```

