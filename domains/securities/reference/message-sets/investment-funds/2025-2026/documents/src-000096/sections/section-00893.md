---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.10 UnitsDetails <UnitsDtls>", "36.4.15.11.10.6 Reference <Ref>"]
file_pages: [1234, 1235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.10.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1234 to 1235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1234

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
36.4.15.11.10.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
36.4.15.11.10.7  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Information related to the price. This may specify the price of original order confirmation.
PriceDetails <PricDtls> contains the following elements (see "UnitPrice23" on page 5125 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 5125
   Value <Val> [1..1] ± 5125
   PriceMethod <PricMtd> [0..1] CodeSet 5125
   AccruedInterestNAV <AcrdIntrstNAV> [0..1] Amount C2, C10 5126
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 5126
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C1 5126
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  5127
{Or     Code <Cd> [1..1] CodeSet 5127
Or}     Proprietary <Prtry> [1..1] ± 5127
36.4.15.11.10.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C36 "NonStandardSLAReferenceRule", C53 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1234 May 2026
```

## File page 1235

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1236
   TotalFees <TtlFees> [0..1] Amount C1, C18 1237
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1237
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1237
   IndividualFee <IndvFee> [0..*]  C6 1238
     Type <Tp> [1..1]  1238
{Or       Code <Cd> [1..1] CodeSet 1239
Or}       Proprietary <Prtry> [1..1] ± 1240
     Basis <Bsis> [0..1]  1240
{Or       Code <Cd> [1..1] CodeSet 1240
Or}       Proprietary <Prtry> [1..1] ± 1241
     StandardAmount <StdAmt> [0..1] Amount C1, C18 1241
     StandardRate <StdRate> [0..1] Rate 1241
     DiscountDetails <DscntDtls> [0..1]  C24 1242
       Amount <Amt> [0..1] Amount C1, C18 1242
       Rate <Rate> [0..1] Rate 1243
       Basis <Bsis> [0..1]  1243
{Or         Code <Cd> [1..1] CodeSet 1243
Or}         Proprietary <Prtry> [1..1] ± 1243
     AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1244
     AppliedRate <ApldRate> [0..1] Rate 1244
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1244
     RecipientIdentification <RcptId> [0..1] ± 1244
     InformativeIndicator <InftvInd> [1..1] Indicator 1245
   IndividualTax <IndvTax> [0..*] ± 1245
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  1245
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1246
       ISIN <ISIN> [0..1] IdentifierSet 1248
       OtherIdentification <OthrId> [0..*]  1248
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1235 May 2026
```

