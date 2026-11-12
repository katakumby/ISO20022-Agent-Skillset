---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range"]
file_pages: [789]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4 Amount Range

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 789 to 789.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 789

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
37.1.4 Amount Range
37.1.4.1  ImpliedCurrencyAndAmountRange1
Definition: Expresses an amount or an amount range with an explicit debit/credit indicator and where
the currency is implied.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 789
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 789
37.1.4.1.1  Amount <Amt>
Presence: [1..1]
Definition: A specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 794 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 794
Or   ToAmount <ToAmt> [1..1] ± 795
Or   FromToAmount <FrToAmt> [1..1]  795
     FromAmount <FrAmt> [1..1] ± 795
     ToAmount <ToAmt> [1..1] ± 795
Or   EqualAmount <EQAmt> [1..1] Amount 796
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 796
37.1.4.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 851
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 789 February 2025
```

