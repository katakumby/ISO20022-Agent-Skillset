---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["55 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "55.2 Structure"]
file_pages: [2237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 55.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2237 to 2237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2237

```text
55.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2237
   Pagination <Pgntn> [1..1] ± 2238
   SecuritiesAccountActivity <SctiesAcctActvty> [1..1]  2238
     SystemDate <SysDt> [1..1] Date 2238
     Change <Chng> [0..*]  2238
       SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 2239
       FieldName <FldNm> [1..1] Text 2239
       OldFieldValue <OdFldVal> [1..1] Text 2239
       NewFieldValue <NewFldVal> [1..1] Text 2239
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 2239
   SupplementaryData <SplmtryData> [0..*] ± C1 2240
55.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
55.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
55.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities 2237 August 2026
```

