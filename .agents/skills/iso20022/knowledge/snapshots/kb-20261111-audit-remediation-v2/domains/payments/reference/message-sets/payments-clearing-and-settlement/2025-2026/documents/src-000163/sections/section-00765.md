---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.5 InterbankSettlementDate <IntrBkSttlmDt>"]
file_pages: [1028]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.5 InterbankSettlementDate <IntrBkSttlmDt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1028 to 1028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1028

```text
Definition: Amount of money moved between the instructing agent and the instructed agent.
Impacted by: C1 "ActiveCurrency", C6 "CurrencyAmount"
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
8.4.2.5  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
8.4.2.6  SettlementTimeIndication <SttlmTmIndctn>
Presence: [0..1]
Definition: Provides information on the occurred settlement time(s) of the payment transaction.
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 1028
   CreditDateTime <CdtDtTm> [0..1] DateTime 1028
8.4.2.6.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
8.4.2.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1028 March 2026
```

