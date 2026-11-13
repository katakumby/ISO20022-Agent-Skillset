---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.3 PaymentIdentification <PmtId>", "4.4.2.2.2.2.3.3.4 LongBusinessIdentification <LngBizId>", "4.4.2.2.2.2.3.3.4.1 TransactionIdentification <TxId>"]
file_pages: [150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.3.4.1 TransactionIdentification <TxId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 150 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
LongBusinessIdentification <LngBizId> contains the following LongPaymentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [0..1] Text 150
   UETR <UETR> [0..1] IdentifierSet 150
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount 151
   InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 151
   PaymentMethod <PmtMtd> [0..1]  151
{Or     FINMessageType <FINMT> [1..1] Text 151
Or     XMLMessageName <XMLMsgNm> [1..1] Text 151
Or     Proprietary <Prtry> [1..1] Text 151
Or}     Instrument <Instrm> [1..1] CodeSet 151
   InstructingAgent <InstgAgt> [1..1] ± 152
   InstructedAgent <InstdAgt> [1..1] ± 153
   EntryType <NtryTp> [0..1] IdentifierSet 154
   EndToEndIdentification <EndToEndId> [0..1] Text 154
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
4.4.2.2.2.2.3.3.4.1  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level. The instructing agent has to make sure that the transaction
identification is unique for a pre-agreed period.
Usage: this is the former PaymentInstructionReference element.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.3.4.2  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 150 February 2025
```

