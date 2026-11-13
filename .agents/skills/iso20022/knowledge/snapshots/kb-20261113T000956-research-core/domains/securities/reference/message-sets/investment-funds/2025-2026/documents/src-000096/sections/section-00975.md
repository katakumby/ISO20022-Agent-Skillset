---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.12 TotalSubscriptionAmount <TtlSbcptAmt>"]
file_pages: [1355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.12 TotalSubscriptionAmount <TtlSbcptAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1355 to 1355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1355

```text
38.4.15.4.1.12  TotalSubscriptionAmount <TtlSbcptAmt>
Presence: [0..1]
Definition: Total amount subscribed over the lifetime of the product.
Impacted by: C1 "ActiveCurrency", C15 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
38.4.15.4.1.13  OtherAmount <OthrAmt>
Presence: [0..*]
Definition: Another amount such as the total qualifying additions in the year of transfer, interest
capitalised in the current year, total outstanding dividend and so on.
OtherAmount <OthrAmt> contains the following OtherAmount3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1355
   Amount <Amt> [1..1] Amount C1, C15 1355
38.4.15.4.1.13.1  Type <Tp>
Presence: [1..1]
Definition: Type of amount.
Type <Tp> contains the following elements (see "GenericIdentification1" on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
38.4.15.4.1.13.2  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount.
Impacted by: C1 "ActiveCurrency", C15 "CurrencyAmount"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1355 May 2026
```

