---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "10.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 10.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt> contains the following
SecuritiesAccountAuditTrailReport3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountAuditTrailOrError
<SctiesAcctAudtTrlOrErr>
[1..1]  73
{Or     AuditTrail <AudtTrl> [1..*]  74
       FieldName <FldNm> [1..1] Text 74
       OldFieldValue <OdFldVal> [1..1] Text 74
       NewFieldValue <NewFldVal> [1..1] Text 75
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 75
       InstructingUser <InstgUsr> [1..1] Text 75
       ApprovingUser <ApprvgUsr> [0..1] Text 75
Or}     BusinessError <BizErr> [1..*]  75
       Error <Err> [1..1]  75
{Or         Code <Cd> [1..1] CodeSet 76
Or}         Proprietary <Prtry> [1..1] Text 76
       Description <Desc> [0..1] Text 76
   DatePeriod <DtPrd> [0..1]  76
{Or     FromDate <FrDt> [1..1] Date 76
Or     ToDate <ToDt> [1..1] Date 76
Or     FromToDate <FrToDt> [1..1] ± 76
Or     EqualDate <EQDt> [1..1] Date 77
Or}     NotEqualDate <NEQDt> [1..1] Date 77
   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 77
10.4.2.1.1  SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>
Presence: [1..1]
Definition: Provides the returned securities account reference data or error information.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities - Securities Account Reference Data 73 December 2019
```

