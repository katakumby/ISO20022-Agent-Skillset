---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.1 References <Refs>", "3.4.2.15.18.2.1.4 InstructionIdentification <InstrId>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.1.4 InstructionIdentification <InstrId>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.4  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the instruction.
Usage: The instruction identification is a point to point reference that can be used between the
instructing party and the instructed party to refer to the individual instruction. It can be included in
several messages related to the instruction.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.5  EndToEndIdentification <EndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction. It can be included in several messages related to the transaction.
Usage: In case there are technical limitations to pass on multiple references, the end-to-end
identification must be passed on throughout the entire end-to-end chain.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.6  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 911
3.4.2.15.18.2.1.7  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level.
Usage: The instructing agent has to make sure that the transaction identification is unique for a pre-
agreed period.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.1.8  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
382 March 2026
```

