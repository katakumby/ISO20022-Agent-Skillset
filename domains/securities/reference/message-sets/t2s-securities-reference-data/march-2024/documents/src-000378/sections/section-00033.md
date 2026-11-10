---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["5 reda.009.001.01 SecurityActivityAdviceV01", "5.4 Message Building Blocks"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 5.4 Message Building Blocks

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 481 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 481
   CreationDateTime <CreDtTm> [0..1] DateTime 481
5.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 485 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 485
   LastPageIndicator <LastPgInd> [1..1] Indicator 485
5.4.3 SecurityActivity <SctyActvty>
Presence: [1..1]
Definition: Activity report of changes occurred for a financial instrument defined in the system.
SecurityActivity <SctyActvty> contains the following SecurityStatement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [1..1] Date 74
   Change <Chng> [0..*]  74
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
74
     FieldName <FldNm> [1..1] Text 75
     OldFieldValue <OdFldVal> [1..1] Text 75
     NewFieldValue <NewFldVal> [1..1] Text 75
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 75
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 73 March 2024
```

