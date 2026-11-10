---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["8 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "8.2 Structure"]
file_pages: [60]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 8.2 Structure

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 60 to 60.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 60
   Pagination <Pgntn> [1..1] ± 61
   SecuritiesAccountActivity <SctiesAcctActvty> [1..1]  61
     SystemDate <SysDt> [1..1] Date 61
     Change <Chng> [0..*]  61
       SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 62
       FieldName <FldNm> [1..1] Text 62
       OldFieldValue <OdFldVal> [1..1] Text 62
       NewFieldValue <NewFldVal> [1..1] Text 62
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 62
   SupplementaryData <SplmtryData> [0..*] ± C1 63
8.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 82 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 82
   CreationDateTime <CreDtTm> [0..1] DateTime 82
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities - Securities Account Reference Data 60 December 2019
```

