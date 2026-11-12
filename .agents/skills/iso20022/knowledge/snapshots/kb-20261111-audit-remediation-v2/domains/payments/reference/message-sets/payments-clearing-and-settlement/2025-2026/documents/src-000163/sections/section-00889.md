---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.9 Identification Information", "10.1.9.2 PaymentIdentification13", "10.1.9.2.2 EndToEndIdentification <EndToEndId>"]
file_pages: [1184]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.9.2.2 EndToEndIdentification <EndToEndId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1184 to 1184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1184

```text
Usage: The instruction identification is a point to point reference that can be used between the
instructing party and the instructed party to refer to the individual instruction. It can be included in
several messages related to the instruction.
Datatype: "Max35Text" on page 1246
10.1.9.2.2  EndToEndIdentification <EndToEndId>
Presence: [1..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction. It can be included in several messages related to the transaction.
Usage: In case there are technical limitations to pass on multiple references, the end-to-end
identification must be passed on throughout the entire end-to-end chain.
Datatype: "Max35Text" on page 1246
10.1.9.2.3  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the first instructing agent, to unambiguously identify the
transaction that is passed on, unchanged, throughout the entire interbank chain.
Usage: The transaction identification can be used for reconciliation, tracking or to link tasks relating to
the transaction on the interbank level.
Usage: The instructing agent has to make sure that the transaction identification is unique for a pre-
agreed period.
Datatype: "Max35Text" on page 1246
10.1.9.2.4  UETR <UETR>
Presence: [0..1]
Definition: Universally unique identifier to provide an end-to-end reference of a payment transaction.
Datatype: "UUIDv4Identifier" on page 1241
10.1.9.2.5  ClearingSystemReference <ClrSysRef>
Presence: [0..1]
Definition: Unique reference, as assigned by a clearing system, to unambiguously identify the
instruction.
Datatype: "Max35Text" on page 1246
10.1.9.3  GenericIdentification3
Definition: Information related to an identification, for example, party identification or account
identification.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1184 March 2026
```

