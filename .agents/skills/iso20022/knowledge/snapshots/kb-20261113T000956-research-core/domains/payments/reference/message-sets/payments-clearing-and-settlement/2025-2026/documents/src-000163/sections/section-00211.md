---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.11 ReturnedInterbankSettlementAmount <RtrdIntrBkSttlmAmt>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.11 ReturnedInterbankSettlementAmount <RtrdIntrBkSttlmAmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
4.4.3.11  ReturnedInterbankSettlementAmount <RtrdIntrBkSttlmAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the instructing agent and the instructed agent in the
returned instruction.
Impacted by: C1 "ActiveCurrency", C11 "CurrencyAmount"
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
4.4.3.12  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Usage: the InterbankSettlementDate is the interbank settlement date of the return message, and not of
the original instruction.
Datatype: "ISODate" on page 1239
4.4.3.13  SettlementPriority <SttlmPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the settlement instruction.
Usage: the SettlementPriority is the settlement priority of the return message, and not of the original
instruction.
Datatype: "Priority3Code" on page 1236
CodeName Name Definition
URGT Urgent Priority level is urgent (highest priority
possible).
HIGH High Priority level is high.
NORM Normal Priority level is normal.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
312 March 2026
```

