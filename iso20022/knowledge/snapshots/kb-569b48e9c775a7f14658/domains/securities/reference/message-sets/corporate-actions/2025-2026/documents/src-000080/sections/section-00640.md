---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.1 Account Identification", "16.1.1.3 CashAccountIdentification5Choice", "16.1.1.3.2 Proprietary <Prtry>"]
file_pages: [831]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.1.3.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 831 to 831.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 831

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
16.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Datatype: "Max34Text" on page 1250
16.1.2 Amount
16.1.2.1  AmountPrice2
Definition: Price expressed as an actual amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 831
   PriceValue <PricVal> [1..1] Amount C1 831
16.1.2.1.1  AmountPriceType <AmtPricTp>
Presence: [1..1]
Definition: Type of amount price.
Datatype: "AmountPriceType2Code" on page 1163
CodeName Name Definition
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
16.1.2.1.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Value of the price.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 831 February 2026
```

