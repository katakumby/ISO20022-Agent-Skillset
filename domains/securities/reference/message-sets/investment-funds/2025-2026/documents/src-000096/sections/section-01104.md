---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.14 DateFirstQualifyingAddition <DtFrstQlfygAddtn>"]
file_pages: [1547]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.14 DateFirstQualifyingAddition <DtFrstQlfygAddtn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1547 to 1547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1547

```text
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
40.4.15.5.1.14  DateFirstQualifyingAddition <DtFrstQlfygAddtn>
Presence: [0..1]
Definition: Date the first qualifying additional amount was made to the product. Qualifying additional
amounts may be made to a Lifetime Individual Savings Account (LISA) product.
Datatype: "ISODate" on page 5388
40.4.15.5.1.15  InvestorTaxReference <InvstrTaxRef>
Presence: [0..1]
Definition: Identification of the investor as assigned by a tax authority.
InvestorTaxReference <InvstrTaxRef> contains the following TaxReference2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  1547
{Or     Code <Cd> [1..1] CodeSet 1547
Or}     Proprietary <Prtry> [1..1] ± 1548
   Reference <Ref> [1..1] Text 1548
40.4.15.5.1.15.1  Type <Tp>
Presence: [0..1]
Definition: Type of tax reference.
Type <Tp> contains one of the following TaxReferenceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1547
Or}   Proprietary <Prtry> [1..1] ± 1548
40.4.15.5.1.15.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax reference expressed as a code.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1547 May 2026
```

