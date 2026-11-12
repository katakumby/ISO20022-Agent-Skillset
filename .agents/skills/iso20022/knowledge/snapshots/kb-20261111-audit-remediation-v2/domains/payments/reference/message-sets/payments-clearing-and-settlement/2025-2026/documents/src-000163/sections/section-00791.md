---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.2 OriginalGroupInformation <OrgnlGrpInf>", "9.4.3.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>"]
file_pages: [1069]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1069 to 1069.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1069

```text
Definition: Point to point reference assigned by the original instructing party to unambiguously identify
the original message.
Datatype: "Max35Text" on page 1246
9.4.3.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
9.4.3.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Original date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
9.4.3.3  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 1246
9.4.3.4  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 1246
9.4.3.5  OriginalTransactionIdentification <OrgnlTxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original first instructing agent, to unambiguously
identify the transaction.
Datatype: "Max35Text" on page 1246
9.4.3.6  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Definition: Universally unique identifier to provide the original end-to-end reference of a payment
transaction.
Datatype: "UUIDv4Identifier" on page 1241
9.4.3.7  AcceptanceDateTime <AccptncDtTm>
Presence: [0..1]
Definition: Point in time when the payment order from the initiating party meets the processing
conditions of the account servicing agent. This means that the account servicing agent has received the
payment order and has applied checks such as authorisation, availability of funds.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1069 March 2026
```

