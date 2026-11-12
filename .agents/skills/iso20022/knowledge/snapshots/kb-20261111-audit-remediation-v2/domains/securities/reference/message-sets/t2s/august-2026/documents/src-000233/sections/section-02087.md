---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.3 Amount", "82.1.3.2 AmountAndDirection20"]
file_pages: [2839]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.3.2 AmountAndDirection20

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2839 to 2839.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2839

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
82.1.3.2  AmountAndDirection20
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
82.1.3.2.1  Amount <Amt>
Presence: [1..1]
Definition: Total amount that needs to be settled.
Impacted by: C1 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 3210
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
82.1.3.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2839 August 2026
```

