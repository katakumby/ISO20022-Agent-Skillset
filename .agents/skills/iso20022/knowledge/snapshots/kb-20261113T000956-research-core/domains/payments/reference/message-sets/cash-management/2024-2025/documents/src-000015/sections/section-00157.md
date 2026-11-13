---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.1 PaymentIdentification <PmtId>", "5.4.2.1.3.1.4 LongBusinessIdentification <LngBizId>", "5.4.2.1.3.1.4.1 TransactionIdentification <TxId>"]
file_pages: [259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.1.4.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 259 to 259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
LongBusinessIdentification <LngBizId> contains the following LongPaymentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [0..1] Text 259
   UETR <UETR> [0..1] IdentifierSet 259
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 260
   InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 260
   PaymentMethod <PmtMtd> [0..1]  260
{Or     FINMessageType <FINMT> [1..1] Text 260
Or     XMLMessageName <XMLMsgNm> [1..1] Text 260
Or     Proprietary <Prtry> [1..1] Text 260
Or}     Instrument <Instrm> [1..1] CodeSet 260
   InstructingAgent <InstgAgt> [1..1] ± 261
   InstructedAgent <InstdAgt> [1..1] ± 262
   EntryType <NtryTp> [0..1] IdentifierSet 263
   EndToEndIdentification <EndToEndId> [0..1] Text 263
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
5.4.2.1.3.1.4.1  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
5.4.2.1.3.1.4.2  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 259 February 2025
```

