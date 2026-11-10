---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["30 reda.009.001.01 SecurityActivityAdviceV01", "30.4 Message Building Blocks"]
file_pages: [1760]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 30.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1760 to 1760.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1760

```text
30.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
30.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
30.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
30.4.3 SecurityActivity <SctyActvty>
Presence: [1..1]
Definition: Activity report of changes occurred for a financial instrument defined in the system.
SecurityActivity <SctyActvty> contains the following SecurityStatement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [1..1] Date 1761
   Change <Chng> [0..*]  1761
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
1761
     FieldName <FldNm> [1..1] Text 1762
     OldFieldValue <OdFldVal> [1..1] Text 1762
     NewFieldValue <NewFldVal> [1..1] Text 1762
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 1762
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities 1760 August 2026
```

