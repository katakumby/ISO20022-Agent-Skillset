---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.1.6 ControlSum <CtrlSum>"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.1.6 ControlSum <CtrlSum>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
3.4.1.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
3.4.1.7  TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt>
Presence: [0..1]
Definition: Total amount of money moved between the instructing agent and the instructed agent.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1222
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.1.8  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
3.4.1.9  SettlementInformation <SttlmInf>
Presence: [1..1]
Definition: Specifies the details on how the settlement of the transaction(s) between the instructing
agent and the instructed agent is completed.
Impacted by: C29 "SettlementMethodAgentRule", C30 "SettlementMethodClearingRule"
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
146 March 2026
```

