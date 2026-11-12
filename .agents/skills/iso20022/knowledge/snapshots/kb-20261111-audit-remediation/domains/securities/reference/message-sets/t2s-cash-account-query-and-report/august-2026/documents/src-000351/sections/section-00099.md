---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["5 reda.039.001.01 CashAccountAuditTrailQueryV01"]
file_pages: [113]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.039.001.01"]
---

# 5 reda.039.001.01 CashAccountAuditTrailQueryV01

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 113 to 113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 113

```text
5 reda.039.001.01
CashAccountAuditTrailQueryV01
5.1 MessageDefinition Functionality
The CashAccountAuditTrailQuery message is sent by an instructing party to the executing party to
query for the cash account audit trail recorded in the system.
Outline
The CashAccountAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the cash account audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CshAcctAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 114
   SearchCriteria <SchCrit> [1..1]  114
     CashAccountIdentification <CshAcctId> [0..1] ± C4, C3 115
     DatePeriod <DtPrd> [0..1]  115
{Or       FromDate <FrDt> [1..1] Date 116
Or       ToDate <ToDt> [1..1] Date 116
Or       FromToDate <FrToDt> [1..1] ± 116
Or       EqualDate <EQDt> [1..1] Date 116
Or}       NotEqualDate <NEQDt> [1..1] Date 116
   SupplementaryData <SplmtryData> [0..*] ± C5 117
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.039.001.01 CashAccountAuditTrailQueryV01
Target2-Securities - Cash Account Query and Report 113 August 2026
```

