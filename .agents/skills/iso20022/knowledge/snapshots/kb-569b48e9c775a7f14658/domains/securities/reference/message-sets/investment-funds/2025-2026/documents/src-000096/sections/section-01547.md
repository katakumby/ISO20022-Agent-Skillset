---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.2 IndividualFee <IndvFee>", "44.4.4.9.15.2.5 DiscountDetails <DscntDtls>", "44.4.4.9.15.2.5.3 Basis <Bsis>", "44.4.4.9.15.2.5.3.2 Proprietary <Prtry>"]
file_pages: [2171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.2.5.3.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2171 to 2171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2171

```text
Definition: Type of discount or waiving expressed as a code.
Datatype: "WaivingInstruction1Code" on page 5388
CodeName Name Definition
WICA WaiveInCash Form of commission waived is cash.
WIUN WaiveInUnits Form of commission waived is additional
units of a financial instrument.
44.4.4.9.15.2.5.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of discount or waiving expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
44.4.4.9.15.2.6  RequestedAmount <ReqdAmt>
Presence: [0..1]
Definition: Requested fee (charge/commission) amount as agreed for the account.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
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
44.4.4.9.15.2.7  RequestedRate <ReqdRate>
Presence: [0..1]
Definition: Requested rate used to calculate the amount of the fee (charge/commission), as agreed for
the account.
Datatype: "PercentageRate" on page 5401
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2171 May 2026
```

