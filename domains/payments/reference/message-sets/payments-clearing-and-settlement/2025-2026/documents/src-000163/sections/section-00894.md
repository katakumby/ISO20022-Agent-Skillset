---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.11 Miscellaneous"]
file_pages: [1189]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.11 Miscellaneous

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1189 to 1189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1189

```text
Classification <Clssfctn> contains one of the following elements (see "MandateClassification1Choice"
on page 1186 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1186
Or}   Proprietary <Prtry> [1..1] Text 1186
10.1.11 Miscellaneous
10.1.11.1  OriginalGroupInformation27
Definition: Set of elements used to provide information on the original group, to which the message
refers.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 1189
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 1189
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 1189
   OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 1189
   OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 1190
10.1.11.1.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 1246
10.1.11.1.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
10.1.11.1.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 1239
10.1.11.1.4  OriginalNumberOfTransactions <OrgnlNbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the original message.
Datatype: "Max15NumericText" on page 1244
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1189 March 2026
```

