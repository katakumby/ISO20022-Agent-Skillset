---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.3 PaymentIdentification <PmtId>", "4.4.2.2.2.2.3.3.1 TransactionIdentification <TxId>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.3.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
PaymentIdentification <PmtId> contains one of the following PaymentIdentification8Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionIdentification <TxId> [1..1] Text 148
Or   UETR <UETR> [1..1] IdentifierSet 149
Or   QueueIdentification <QId> [1..1]  149
     QueueIdentification <QId> [1..1] Text 149
     PositionInQueue <PosInQ> [1..1] Text 149
Or   LongBusinessIdentification <LngBizId> [1..1]  C17 149
     TransactionIdentification <TxId> [0..1] Text 150
     UETR <UETR> [0..1] IdentifierSet 150
     InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 151
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 151
     PaymentMethod <PmtMtd> [0..1]  151
{Or       FINMessageType <FINMT> [1..1] Text 151
Or       XMLMessageName <XMLMsgNm> [1..1] Text 151
Or       Proprietary <Prtry> [1..1] Text 151
Or}       Instrument <Instrm> [1..1] CodeSet 151
     InstructingAgent <InstgAgt> [1..1] ± 152
     InstructedAgent <InstdAgt> [1..1] ± 153
     EntryType <NtryTp> [0..1] IdentifierSet 154
     EndToEndIdentification <EndToEndId> [0..1] Text 154
Or   ShortBusinessIdentification <ShrtBizId> [1..1]  C18 154
     TransactionIdentification <TxId> [0..1] Text 155
     UETR <UETR> [0..1] IdentifierSet 155
     InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 155
     InstructingAgent <InstgAgt> [1..1] ± 155
Or}   ProprietaryIdentification <PrtryId> [1..1] Text 156
4.4.2.2.2.2.3.3.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 148 February 2025
```

