---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.2 OriginalPaymentIdentification <OrgnlPmtId>", "23.4.2.2.4 LongBusinessIdentification <LngBizId>", "23.4.2.2.4.1 TransactionIdentification <TxId>"]
file_pages: [612]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.2.4.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 612 to 612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 612

```text
LongBusinessIdentification <LngBizId> contains the following LongPaymentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [0..1] Text 612
   UETR <UETR> [0..1] IdentifierSet 612
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 613
   InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 613
   PaymentMethod <PmtMtd> [0..1]  613
{Or     FINMessageType <FINMT> [1..1] Text 613
Or     XMLMessageName <XMLMsgNm> [1..1] Text 613
Or     Proprietary <Prtry> [1..1] Text 613
Or}     Instrument <Instrm> [1..1] CodeSet 613
   InstructingAgent <InstgAgt> [1..1] ± 614
   InstructedAgent <InstdAgt> [1..1] ± 615
   EntryType <NtryTp> [0..1] IdentifierSet 616
   EndToEndIdentification <EndToEndId> [0..1] Text 616
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
23.4.2.2.4.1  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
23.4.2.2.4.2  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 612 February 2025
```

