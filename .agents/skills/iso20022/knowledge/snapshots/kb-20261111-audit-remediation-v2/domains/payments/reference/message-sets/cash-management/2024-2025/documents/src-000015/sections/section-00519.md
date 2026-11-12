---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["29 camt.051.001.07 LiquidityDebitTransferV07", "29.4 Message Building Blocks", "29.4.2 LiquidityDebitTransfer <LqdtyDbtTrf>", "29.4.2.1 LiquidityTransferIdentification <LqdtyTrfId>", "29.4.2.1.2 EndToEndIdentification <EndToEndId>"]
file_pages: [681]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.051.001.07"]
---

# 29.4.2.1.2 EndToEndIdentification <EndToEndId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 681 to 681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 681

```text
Usage: The instruction identification is a point to point reference that can be used between the
instructing party and the instructed party to refer to the individual instruction. It can be included in
several messages related to the instruction.
Datatype: "Max35Text" on page 889
29.4.2.1.2  EndToEndIdentification <EndToEndId>
Presence: [1..1]
Definition: Unique identification assigned by the initiating party to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction. It can be included in several messages related to the transaction.
Datatype: "Max35Text" on page 889
29.4.2.1.3  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level.
Usage: The instructing agent has to make sure that the transaction identification is unique for a pre-
agreed period.
Datatype: "Max35Text" on page 889
29.4.2.1.4  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 885
29.4.2.2  Creditor <Cdtr>
Presence: [0..1]
Definition: Owner of the account to be credited.
Approved by the Payments SEG on 04 February 2025 camt.051.001.07 LiquidityDebitTransferV07
Cash Management - Maintenance 2024 - 2025 681 February 2025
```

