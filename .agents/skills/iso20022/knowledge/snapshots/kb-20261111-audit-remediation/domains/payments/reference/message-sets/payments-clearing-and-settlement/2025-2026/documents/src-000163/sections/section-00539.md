---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.8 AdditionalDateTime <AddtlDtTm>", "6.4.2.8.1 AcceptanceDateTime <AccptncDtTm>"]
file_pages: [743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.8.1 AcceptanceDateTime <AccptncDtTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 743 to 743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 743

```text
Constraints
• AdditionalDateTimePresenceRule
AcceptanceDateTime or PoolingAdjustmentDate or ExpiryDateTime must be present. All can be
present.
Following Must be True
    /AcceptanceDateTime Must be present
 Or    /PoolingAdjustmentDate Must be present
 Or    /ExpiryDateTime Must be present
6.4.2.8.1  AcceptanceDateTime <AccptncDtTm>
Presence: [0..1]
Definition: Point in time when the payment order from the initiating party meets the processing
conditions of the account servicing agent. This means that the account servicing agent has received the
payment order and has applied checks such as authorisation, availability of funds.
Datatype: "ISODateTime" on page 1239
6.4.2.8.2  PoolingAdjustmentDate <PoolgAdjstmntDt>
Presence: [0..1]
Definition: Date used for the correction of the value date of a cash pool movement that has been posted
with a different value date.
Datatype: "ISODate" on page 1239
6.4.2.8.3  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date and time on which the payment should be expired if it has not settled.
Datatype: "ISODateTime" on page 1239
6.4.2.9  InstructedAmount <InstdAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
743 March 2026
```

