---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.2 OriginalGroupInformation <OrgnlGrpInf>", "5.4.3.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 602 to 602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 602

```text
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupInformation33
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 602
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 602
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 602
5.4.3.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference assigned by the original instructing party to unambiguously identify
the original message.
Datatype: "Max35Text" on page 1246
5.4.3.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
5.4.3.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Original date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
5.4.3.3  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 1246
5.4.3.4  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 1246
5.4.3.5  OriginalTransactionIdentification <OrgnlTxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original first instructing agent, to unambiguously
identify the transaction.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
602 March 2026
```

