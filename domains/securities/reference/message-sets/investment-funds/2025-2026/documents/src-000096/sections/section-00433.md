---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.8.16 ForeignExchangeDetails <FXDtls>"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.8.16 ForeignExchangeDetails <FXDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
IndividualTax <IndvTax> contains the following elements (see "Tax38" on page 5237 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5237
{Or     Code <Cd> [1..1] CodeSet 5238
Or}     Proprietary <Prtry> [1..1] ± 5238
   Basis <Bsis> [0..1]  5239
{Or     Code <Cd> [1..1] CodeSet 5239
Or}     Proprietary <Prtry> [1..1] ± 5239
   Amount <Amt> [1..1] Amount C1, C13 5239
   Country <Ctry> [0..1] CodeSet C12 5240
   ExemptionIndicator <XmptnInd> [1..1] Indicator 5240
   ExemptionReason <XmptnRsn> [0..1]  5240
{Or     Code <Cd> [1..1] CodeSet 5241
Or}     Proprietary <Prtry> [1..1] ± 5243
   RecipientIdentification <RcptId> [0..1] ± 5244
   TaxCalculationDetails <TaxClctnDtls> [0..1]  5244
     Basis <Bsis> [0..1]  5244
{Or       Code <Cd> [1..1] CodeSet 5245
Or}       Proprietary <Prtry> [1..1] ± 5245
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5245
26.4.8.16  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
How the exchange rate is expressed determines which currency is the Unit Currency and Quoted
Currency. If the amounts concerned are EUR 1000 and USD 1300, the exchange rate may be
expressed as per either of the following examples:
EXAMPLE 1
UnitCurrency EUR
QuotedCurrency USD
ExchangeRate 1.300
EXAMPLE 2
UnitCurrency USD
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 592 May 2026
```

