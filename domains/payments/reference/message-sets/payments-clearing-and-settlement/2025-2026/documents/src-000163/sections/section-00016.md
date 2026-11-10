---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.2 OriginalGroupInformation <OrgnlGrpInf>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.2 OriginalGroupInformation <OrgnlGrpInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the reported status.
Usage: The instructing party is the party sending the status message and not the party that sent the
original instruction that is being reported on.
Datatype: "Max35Text" on page 1246
2.4.3.2  OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
OriginalGroupInformation <OrgnlGrpInf> contains the following OriginalGroupInformation33
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 33
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 33
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 33
2.4.3.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference assigned by the original instructing party to unambiguously identify
the original message.
Datatype: "Max35Text" on page 1246
2.4.3.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
2.4.3.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Original date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
2.4.3.3  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 1246
2.4.3.4  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
33 March 2026
```

