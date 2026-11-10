---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["4 reda.038.001.01 CashAccountActivityAdviceV01"]
file_pages: [108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.038.001.01"]
---

# 4 reda.038.001.01 CashAccountActivityAdviceV01

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 108 to 108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 108

```text
4 reda.038.001.01
CashAccountActivityAdviceV01
4.1 MessageDefinition Functionality
The CashAccountActivityReport message is sent by the executing party to an instructing party
containing information about changes on cash account reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for cash account reference
data.
Outline
The CashAccountActivityAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CashAccountActivity
Activity report of changes occurred for a cash account defined in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CshAcctActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 109
   CashAccountActivity <CshAcctActvty> [1..1]  109
     SystemDate <SysDt> [1..1] Date 110
     Change <Chng> [0..*]  110
       CashAccountIdentification <CshAcctId> [1..1] ± C4, C3 110
       FieldName <FldNm> [1..1] Text 111
       OldFieldValue <OdFldVal> [1..1] Text 111
       NewFieldValue <NewFldVal> [1..1] Text 111
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 111
   SupplementaryData <SplmtryData> [0..*] ± C5 112
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.038.001.01 CashAccountActivityAdviceV01
Target2-Securities - Cash Account Query and Report 108 August 2026
```

