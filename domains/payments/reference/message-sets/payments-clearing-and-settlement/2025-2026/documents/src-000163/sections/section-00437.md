---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.6 OriginalUETR <OrgnlUETR>"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.6 OriginalUETR <OrgnlUETR>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
5.4.3.6  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Definition: Universally unique identifier to provide the original end-to-end reference of a payment
transaction.
Datatype: "UUIDv4Identifier" on page 1241
5.4.3.7  OriginalClearingSystemReference <OrgnlClrSysRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the original clearing system, to unambiguously identify the
original instruction.
Datatype: "Max35Text" on page 1246
5.4.3.8  OriginalInterbankSettlementAmount <OrgnlIntrBkSttlmAmt>
Presence: [0..1]
Definition: Amount of money moved between the instructing agent and the instructed agent, as provided
in the original instruction.
Impacted by: C2 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.3.9  ReversedInterbankSettlementAmount <RvsdIntrBkSttlmAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the instructing agent and the instructed agent in the
reversed instruction.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1222
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
603 March 2026
```

