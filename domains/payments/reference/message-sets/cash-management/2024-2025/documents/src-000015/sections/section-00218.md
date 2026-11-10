---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.1 PaymentIdentification <PmtId>", "6.4.2.1.4 LongBusinessIdentification <LngBizId>", "6.4.2.1.4.1 TransactionIdentification <TxId>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.1.4.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
LongBusinessIdentification <LngBizId> contains the following LongPaymentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [0..1] Text 335
   UETR <UETR> [0..1] IdentifierSet 335
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 336
   InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 336
   PaymentMethod <PmtMtd> [0..1]  336
{Or     FINMessageType <FINMT> [1..1] Text 336
Or     XMLMessageName <XMLMsgNm> [1..1] Text 336
Or     Proprietary <Prtry> [1..1] Text 336
Or}     Instrument <Instrm> [1..1] CodeSet 336
   InstructingAgent <InstgAgt> [1..1] ± 337
   InstructedAgent <InstdAgt> [1..1] ± 338
   EntryType <NtryTp> [0..1] IdentifierSet 339
   EndToEndIdentification <EndToEndId> [0..1] Text 339
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
6.4.2.1.4.1  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
6.4.2.1.4.2  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 335 February 2025
```

