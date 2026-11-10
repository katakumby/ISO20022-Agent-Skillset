---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.2 Amount", "9.1.2.1 AmountAndDirection51", "9.1.2.1.1 Amount <Amt>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.2.1.1 Amount <Amt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C9 194
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 194
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C1, C10 194
9.1.2.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the cash entry.
Impacted by: C2 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 311
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
9.1.2.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 324
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.1.2.1.3  OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>
Presence: [0..1]
Definition: Posting/settlement amount in its original currency when conversion from/into another
currency has occurred.
Impacted by: C1 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 312
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 194 September 2025
```

