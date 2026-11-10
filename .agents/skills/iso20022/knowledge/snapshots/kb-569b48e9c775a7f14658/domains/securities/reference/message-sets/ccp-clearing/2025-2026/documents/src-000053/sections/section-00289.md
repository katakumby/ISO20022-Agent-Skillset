---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.3 Amount", "12.1.3.1 AmountAndDirection21", "12.1.3.1.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [378]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.3.1.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 378 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.3.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: CreditDebitCode on page 476
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
12.1.3.2  AmountAndDirection20
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
12.1.3.2.1  Amount <Amt>
Presence: [1..1]
Definition: Total amount that needs to be settled.
Impacted by:   'C2 ActiveOrHistoricCurrency  ',   'C6 CurrencyAmount  '
Datatype: ActiveOrHistoricCurrencyAndAmount on page 471
Constraints
• ActiveOrHistoricCurrency
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 378
```

