---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.26 TransactionOverhead <TxOvrhd>", "49.4.5.9.26.7 DigitalNetworkFee <DgtlNtwkFee>", "49.4.5.9.26.7.2 Quantity <Qty>", "49.4.5.9.26.7.2.2 ProprietaryQuantity <PrtryQty>", "49.4.5.9.26.7.2.2.1 Quantity <Qty>"]
file_pages: [2852, 2853]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.26.7.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2852 to 2853.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2852

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 2852
   QuantityType <QtyTp> [1..1] Text 2852
   Issuer <Issr> [1..1] Text 2852
   SchemeName <SchmeNm> [0..1] Text 2852
49.4.5.9.26.7.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
49.4.5.9.26.7.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
49.4.5.9.26.7.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
49.4.5.9.26.7.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
49.4.5.9.26.7.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
49.4.5.9.27  InformativeTaxDetails <InftvTaxDtls>
Presence: [0..1]
Definition: Additional information about tax that does not have an impact on the transaction overhead.
Impacted by: C38 "TaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2852 May 2026
```

## File page 2853

```text
InformativeTaxDetails <InftvTaxDtls> contains the following elements (see "InformativeTax2" on
page 5222 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C1, C13 5223
   EUCapitalGain <EUCptlGn> [0..1]  5224
{Or     Code <Cd> [1..1] CodeSet 5224
Or}     Proprietary <Prtry> [1..1] ± 5224
   EUDividendStatus <EUDvddSts> [0..1]  5225
{Or     Code <Cd> [1..1] CodeSet 5225
Or}     Proprietary <Prtry> [1..1] ± 5225
   PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 5226
   IndividualTax <IndvTax> [0..*]  5226
     Type <Tp> [1..1]  5226
{Or       Code <Cd> [1..1] CodeSet 5227
Or}       Proprietary <Prtry> [1..1] ± 5228
     InformativeAmount <InftvAmt> [0..1] Amount C1, C13 5228
     InformativeRate <InftvRate> [0..1] Rate 5229
     Country <Ctry> [0..1] CodeSet C12 5229
     ExemptionIndicator <XmptnInd> [1..1] Indicator 5229
     ExemptionReason <XmptnRsn> [0..1]  5229
{Or       Code <Cd> [1..1] CodeSet 5230
Or}       Proprietary <Prtry> [1..1] ± 5232
     RecipientIdentification <RcptId> [0..1] ± 5233
     TaxCalculationDetails <TaxClctnDtls> [0..1]  5233
       Basis <Bsis> [0..1]  5233
{Or         Code <Cd> [1..1] CodeSet 5234
Or}         Proprietary <Prtry> [1..1] ± 5234
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5234
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2853 May 2026
```

