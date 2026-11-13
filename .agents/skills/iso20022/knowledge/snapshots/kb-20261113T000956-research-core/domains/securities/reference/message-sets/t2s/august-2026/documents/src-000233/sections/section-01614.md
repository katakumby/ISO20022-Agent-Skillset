---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01"]
file_pages: [2241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2241 to 2241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2241

```text
56 reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
56.1 MessageDefinition Functionality
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
56.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctAudtTrlQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2242
   SearchCriteria <SchCrit> [1..1]  2242
     SecuritiesAccountIdentification <SctiesAcctId> [0..1] ± 2242
     DatePeriod <DtPrd> [0..1]  2243
{Or       FromDate <FrDt> [1..1] Date 2243
Or       ToDate <ToDt> [1..1] Date 2243
Or       FromToDate <FrToDt> [1..1] ± 2243
Or       EqualDate <EQDt> [1..1] Date 2244
Or}       NotEqualDate <NEQDt> [1..1] Date 2244
   SupplementaryData <SplmtryData> [0..*] ± C1 2244
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities 2241 August 2026
```

