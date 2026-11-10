---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.6 Reference <Ref>"]
file_pages: [1400, 1401]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1400 to 1401.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1400

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
38.4.15.8.4.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
38.4.15.8.4.7  PriceDetails <PricDtls>
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
38.4.15.8.4.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C30 "NonStandardSLAReferenceRule", C46 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1400 May 2026
```

## File page 1401

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C15 1402
   TotalFees <TtlFees> [0..1] Amount C1, C15 1403
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C15 1403
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1403
   IndividualFee <IndvFee> [0..*]  C6 1404
     Type <Tp> [1..1]  1404
{Or       Code <Cd> [1..1] CodeSet 1405
Or}       Proprietary <Prtry> [1..1] ± 1406
     Basis <Bsis> [0..1]  1406
{Or       Code <Cd> [1..1] CodeSet 1406
Or}       Proprietary <Prtry> [1..1] ± 1407
     StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
     StandardRate <StdRate> [0..1] Rate 1407
     DiscountDetails <DscntDtls> [0..1]  C21 1408
       Amount <Amt> [0..1] Amount C1, C15 1408
       Rate <Rate> [0..1] Rate 1409
       Basis <Bsis> [0..1]  1409
{Or         Code <Cd> [1..1] CodeSet 1409
Or}         Proprietary <Prtry> [1..1] ± 1409
     AppliedAmount <ApldAmt> [0..1] Amount C1, C15 1410
     AppliedRate <ApldRate> [0..1] Rate 1410
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1410
     RecipientIdentification <RcptId> [0..1] ± 1410
     InformativeIndicator <InftvInd> [1..1] Indicator 1411
   IndividualTax <IndvTax> [0..*] ± 1411
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  1411
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C18,
C19,
C27,
C28,
C31
1412
       ISIN <ISIN> [0..1] IdentifierSet 1414
       OtherIdentification <OthrId> [0..*]  1414
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1401 May 2026
```

