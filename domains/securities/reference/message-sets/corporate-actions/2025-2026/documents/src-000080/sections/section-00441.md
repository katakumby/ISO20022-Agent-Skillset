---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>"]
file_pages: [593, 594, 595]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 593 to 595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 593

```text
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
8.4.12.10  SecuritiesMovementDetails <SctiesMvmntDtls>
Presence: [0..*]
Definition: Provides information about the securities movement linked to the corporate action option.
Impacted by: C19 "ExemptionTypeUsageRule", C31 "IncomeType1Rule", C33
"IncomeTypeUsageRule", C39 "IssuerOfferorTaxabilityIndicatorUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 593 February 2026
```

## File page 594

```text
SecuritiesMovementDetails <SctiesMvmntDtls> contains the following SecuritiesOption112
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C15,
C16,
C36,
C37,
C48
596
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 597
   TemporaryFinancialInstrumentIndicator
<TempFinInstrmInd>
[0..1] ± 597
   NewSecuritiesIssuanceIndicator <NewSctiesIssncInd> [0..1] CodeSet 597
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  598
{Or     Code <Cd> [1..1] CodeSet 598
Or}     Proprietary <Prtry> [1..1] ± 598
   IncomeType <IncmTp> [0..1] ± 598
   OtherIncomeType <OthrIncmTp> [0..*] ± 599
   ExemptionType <XmptnTp> [0..*] ± 599
   CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C11 599
   PostingQuantity <PstngQty> [1..1] ± 600
   SafekeepingPlace <SfkpgPlc> [0..1] ± 600
   FractionDisposition <FrctnDspstn> [0..1] ± 600
   CurrencyOption <CcyOptn> [0..1] CodeSet C1 601
   DateDetails <DtDtls> [1..1]  601
     PostingDate <PstngDt> [1..1] ± 601
     AvailableDate <AvlblDt> [0..1] ± 602
     PariPassuDate <PrpssDt> [0..1] ± 602
     DividendRankingDate <DvddRnkgDt> [0..1] ± 602
     EarliestPaymentDate <EarlstPmtDt> [0..1] ± 603
     PaymentDate <PmtDt> [0..1] ± 603
   RateDetails <RateDtls> [0..1]  603
     AdditionalQuantityForSubscribedResultantSecuritie
s <AddtlQtyForSbcbdRsltntScties>
[0..1] ± 604
     AdditionalQuantityForExistingSecurities
<AddtlQtyForExstgScties>
[0..1] ± 604
     NewToOld <NewToOd> [0..1] ± 605
     ChargesFees <ChrgsFees> [0..1] ± 605
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 594 February 2026
```

## File page 595

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FiscalStamp <FsclStmp> [0..1] Rate 606
     ApplicableRate <AplblRate> [0..1] Rate 606
     TaxCreditRate <TaxCdtRate> [0..1] ± 606
     FinancialTransactionTaxRate <FinTxTaxRate> [0..1] Rate 606
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 606
     SecondLevelTax <ScndLvlTax> [0..*] ± 607
   PriceDetails <PricDtls> [0..1]  C21 607
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 608
     IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  608
{Or       IndicativePrice <IndctvPric> [1..1] ± 609
Or}       MarketPrice <MktPric> [1..1] ± 609
     CashValueForTax <CshValForTax> [0..1] ± 609
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 609
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 610
   AmountDetails <AmtDtls> [0..1]  610
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C12 611
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C12 611
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C50,
C51
612
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C50,
C51
612
Constraints
• ExemptionTypeUsageRule
The lists of exemption type codes to be used in ExemptionType are provided in the document
"ETYP-ITYP Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
• IncomeType1Rule
If at least one occurrence of OtherIncomeType is present, then IncomeType must be present.
On Condition
    /OtherIncomeType[*] is present
Following Must be True
    /IncomeType Must be present
• IncomeTypeUsageRule
The lists of income type codes to be used in IncomeType are provided in the document "ETYP-ITYP
Exemption & Income Type Codes" available on the SMPG website at www.smpg.info.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 595 February 2026
```

