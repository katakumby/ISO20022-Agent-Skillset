---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.14 IndividualTax <IndvTax>"]
file_pages: [503]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.14 IndividualTax <IndvTax>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 503 to 503.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 503

```text
Constraints
• FeeTaxElementRule
One of the elements (CommercialAgreementReference, IndividualFee, IndividualTax) must be
present.
24.4.8.14  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Tax related to the transfer of the financial instrument.
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
24.4.8.15  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
How the exchange rate is expressed determines which currency is the Unit Currency and Quoted
Currency. If the amounts concerned are EUR 1000 and USD 1300, the exchange rate may be
expressed as per either of the following examples:
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 503 May 2026
```

