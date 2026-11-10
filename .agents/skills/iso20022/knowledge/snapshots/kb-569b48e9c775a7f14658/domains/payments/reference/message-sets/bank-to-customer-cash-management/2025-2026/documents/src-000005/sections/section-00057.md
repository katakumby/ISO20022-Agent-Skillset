---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.1 References <Refs>", "2.4.2.15.18.2.1.4 InstructionIdentification <InstrId>"]
file_pages: [122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.1.4 InstructionIdentification <InstrId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 122 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.4  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the instruction.
Usage: The instruction identification is a point to point reference that can be used between the
instructing party and the instructed party to refer to the individual instruction. It can be included in
several messages related to the instruction.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.5  EndToEndIdentification <EndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction. It can be included in several messages related to the transaction.
Usage: In case there are technical limitations to pass on multiple references, the end-to-end
identification must be passed on throughout the entire end-to-end chain.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.6  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 911
2.4.2.15.18.2.1.7  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level.
Usage: The instructing agent has to make sure that the transaction identification is unique for a pre-
agreed period.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.1.8  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
122 March 2026
```

