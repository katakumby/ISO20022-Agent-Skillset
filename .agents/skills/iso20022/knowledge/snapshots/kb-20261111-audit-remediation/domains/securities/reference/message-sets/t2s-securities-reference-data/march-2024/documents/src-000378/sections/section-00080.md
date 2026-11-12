---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["11 reda.033.001.01 SecuritiesAuditTrailQueryV01"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 11 reda.033.001.01 SecuritiesAuditTrailQueryV01

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
11 reda.033.001.01
SecuritiesAuditTrailQueryV01
11.1 MessageDefinition Functionality
The SecuritiesAuditTrailQuery message is sent by an instructing party to the executing party to query
for the securities audit trail recorded in the system.
Outline
The SecuritiesAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 130
   SearchCriteria <SchCrit> [1..1]  130
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
131
     DatePeriod <DtPrd> [0..1]  132
{Or       FromDate <FrDt> [1..1] Date 132
Or       ToDate <ToDt> [1..1] Date 132
Or       FromToDate <FrToDt> [1..1] ± 132
Or       EqualDate <EQDt> [1..1] Date 133
Or}       NotEqualDate <NEQDt> [1..1] Date 133
   SupplementaryData <SplmtryData> [0..*] ± C6 133
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities - Securities Reference Data 129 March 2024
```

