---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.19 LastTransaction <LastTx>"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.19 LastTransaction <LastTx>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
7.1.19.35.19  LastTransaction <LastTx>
Presence: [0..1]
Definition: Indicates whether or not this is the last transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.35.20  SpreadTransaction <SprdTx>
Presence: [0..1]
Definition: Specifies that there will be one price and one transaction when two contracts are carried out
simultaneously, one to buy and the other one to sell with two different expiration dates.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.36  CurrencyToBuyOrSell1Choice
Definition: Choice of counterparty type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 330
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 330
7.1.19.36.1  CurrencyToBuy <CcyToBuy>
Presence: [1..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash
proceeds.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.19.36.2  CurrencyToSell <CcyToSell>
Presence: [1..1]
Definition: Account servicer is instructed to sell the indicated currency in order to obtain the necessary
currency to fund the transaction.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 330 February 2025
```

