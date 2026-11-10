---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.17 InnovativeFinance <InnvtvFinc>", "40.4.15.5.1.17.1 Type <Tp>"]
file_pages: [1549]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.17.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1549 to 1549.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1549

```text
InnovativeFinance <InnvtvFinc> contains the following InnovativeFinance1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1549
   Information <Inf> [1..1] Text 1549
40.4.15.5.1.17.1  Type <Tp>
Presence: [1..1]
Definition: Type of innovative finance product.
Type <Tp> contains the following elements (see "GenericIdentification36" on page 4549 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
40.4.15.5.1.17.2  Information <Inf>
Presence: [1..1]
Definition: Details of an innovative finance product.
Datatype: "Max350Text" on page 5403
40.4.15.5.1.18  LowestInvestedAmountCurrentYear <LwstInvstdAmtCurYr>
Presence: [0..1]
Definition: Lowest investment amount in the current year, used to calculate a tax deduction amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
40.4.15.5.1.19  TaxCalculationBase <TaxClctnBase>
Presence: [0..1]
Definition: Amount of money from which the tax deduction is calculated.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1549 May 2026
```

