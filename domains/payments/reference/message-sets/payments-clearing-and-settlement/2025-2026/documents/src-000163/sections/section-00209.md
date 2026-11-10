---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.2 OriginalGroupInformation <OrgnlGrpInf>", "4.4.3.2.3 OriginalCreationDateTime <OrgnlCreDtTm>"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.2.3 OriginalCreationDateTime <OrgnlCreDtTm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
4.4.3.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Original date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
4.4.3.3  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 1246
4.4.3.4  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 1246
4.4.3.5  OriginalTransactionIdentification <OrgnlTxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original first instructing agent, to unambiguously
identify the transaction.
Datatype: "Max35Text" on page 1246
4.4.3.6  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Definition: Universally unique identifier to provide the original end-to-end reference of a payment
transaction.
Datatype: "UUIDv4Identifier" on page 1241
4.4.3.7  OriginalClearingSystemReference <OrgnlClrSysRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the original clearing system, to unambiguously identify the
original instruction.
Datatype: "Max35Text" on page 1246
4.4.3.8  OriginalInterbankSettlementAmount <OrgnlIntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent, as provided
in the original instruction.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
310 March 2026
```

