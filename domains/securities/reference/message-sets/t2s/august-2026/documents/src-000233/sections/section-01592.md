---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["53 reda.033.001.01 SecuritiesAuditTrailQueryV01"]
file_pages: [2219]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 53 reda.033.001.01 SecuritiesAuditTrailQueryV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2219 to 2219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2219

```text
53 reda.033.001.01
SecuritiesAuditTrailQueryV01
53.1 MessageDefinition Functionality
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
53.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2220
   SearchCriteria <SchCrit> [1..1]  2220
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C1, C2,
C3, C4,
C5
2221
     DatePeriod <DtPrd> [0..1]  2222
{Or       FromDate <FrDt> [1..1] Date 2222
Or       ToDate <ToDt> [1..1] Date 2222
Or       FromToDate <FrToDt> [1..1] ± 2222
Or       EqualDate <EQDt> [1..1] Date 2223
Or}       NotEqualDate <NEQDt> [1..1] Date 2223
   SupplementaryData <SplmtryData> [0..*] ± C6 2223
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities 2219 August 2026
```

