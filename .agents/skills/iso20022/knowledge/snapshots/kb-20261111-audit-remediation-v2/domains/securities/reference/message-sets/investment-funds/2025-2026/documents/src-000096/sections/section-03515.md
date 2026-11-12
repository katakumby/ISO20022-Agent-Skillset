---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.17 FundOrderData6", "66.1.26.17.3 AdditionalAmount <AddtlAmt>"]
file_pages: [4765]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.17.3 AdditionalAmount <AddtlAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4765 to 4765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4765

```text
CodeName Name Definition
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
66.1.26.17.3  AdditionalAmount <AddtlAmt>
Presence: [0..1]
Definition: Choice between additional cash in or resulting cash out.
AdditionalAmount <AddtlAmt> contains one of the following elements (see
"AdditionalAmount1Choice" on page 4774 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AdditionalCashIn <AddtlCshIn> [1..1] Amount C2, C10 4774
Or}   ResultingCashOut <RsltgCshOut> [1..1] Amount C2, C10 4775
66.1.26.17.4  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency from which the quoted currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.26.17.5  QuotedCurrency <QtdCcy>
Presence: [0..1]
Definition: Currency into which the unit currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4765 May 2026
```

