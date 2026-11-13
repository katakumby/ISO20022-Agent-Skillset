---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "7.4.2.41.4 InterbankSettlementDate <IntrBkSttlmDt>"]
file_pages: [989]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41.4 InterbankSettlementDate <IntrBkSttlmDt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 989 to 989.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 989

```text
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
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
7.4.2.41.4  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
7.4.2.41.5  SettlementPriority <SttlmPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the settlement instruction.
Datatype: "Priority3Code" on page 1236
CodeName Name Definition
URGT Urgent Priority level is urgent (highest priority
possible).
HIGH High Priority level is high.
NORM Normal Priority level is normal.
7.4.2.41.6  SettlementTimeIndication <SttlmTmIndctn>
Presence: [0..1]
Definition: Provides information on the occurred settlement time(s) of the payment transaction.
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 990
   CreditDateTime <CdtDtTm> [0..1] DateTime 990
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
989 March 2026
```

