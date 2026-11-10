---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 reda.042.001.01 PartyAuditTrailQueryV01"]
file_pages: [111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.042.001.01"]
---

# 9 reda.042.001.01 PartyAuditTrailQueryV01

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 111 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
9 reda.042.001.01
PartyAuditTrailQueryV01
9.1 MessageDefinition Functionality
The PartyAuditTrailQuery message is sent by an instructing party to the executing party to query for the
party audit trail recorded in the system.
Outline
The PartyAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the party audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 112
   SearchCriteria <SchCrit> [1..1]  112
     PartyIdentification <PtyId> [0..1] ± 113
     DatePeriod <DtPrd> [0..1]  113
{Or       FromDate <FrDt> [1..1] Date 113
Or       ToDate <ToDt> [1..1] Date 114
Or       FromToDate <FrToDt> [1..1] ± 114
Or       EqualDate <EQDt> [1..1] Date 114
Or}       NotEqualDate <NEQDt> [1..1] Date 114
   SupplementaryData <SplmtryData> [0..*] ± C3 114
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.042.001.01 PartyAuditTrailQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
111 March 2024
```

