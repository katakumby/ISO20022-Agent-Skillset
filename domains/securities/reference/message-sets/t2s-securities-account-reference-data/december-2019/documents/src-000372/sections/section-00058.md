---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
9 reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
9.1 MessageDefinition Functionality
The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to
query for the securities account audit trail recorded in the system.
Outline
The SecuritiesAccountAuditTrailQueryV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities account audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 65
   SearchCriteria <SchCrit> [1..1]  65
     SecuritiesAccountIdentification <SctiesAcctId> [0..1] ± 65
     DatePeriod <DtPrd> [0..1]  66
{Or       FromDate <FrDt> [1..1] Date 66
Or       ToDate <ToDt> [1..1] Date 66
Or       FromToDate <FrToDt> [1..1] ± 66
Or       EqualDate <EQDt> [1..1] Date 67
Or}       NotEqualDate <NEQDt> [1..1] Date 67
   SupplementaryData <SplmtryData> [0..*] ± C1 67
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities - Securities Account Reference Data 64 December 2019
```

