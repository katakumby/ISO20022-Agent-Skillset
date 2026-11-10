---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.1 SecurityDetails <SctyDtls>"]
file_pages: [457, 458]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.1 SecurityDetails <SctyDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 457 to 458.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 457

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FinancialTransactionTaxRate <FinTxTaxRate> [0..1] ± 477
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 477
     SecondLevelTax <ScndLvlTax> [0..*] ± 478
   PriceDetails <PricDtls> [0..1]  C29 478
     IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  479
{Or       IndicativePrice <IndctvPric> [1..1] ± 479
Or}       MarketPrice <MktPric> [1..1] ± 480
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 480
     CashValueForTax <CshValForTax> [0..1] ± 480
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 481
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 481
   AmountDetails <AmtDtls> [0..1]  482
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C1, C14 482
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C1, C14 483
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
• IssuerOfferorTaxabilityIndicatorUsageRule
The IssuerOfferorTaxabilityIndicator may only be used when no tax rate is provided in the message
and it must not be used in events such as dividend or interest.
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in the
document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
7.4.13.22.1  SecurityDetails <SctyDtls>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 457 February 2026
```

## File page 458

```text
Definition: Provides description of the financial instrument related to securities movement.
Impacted by: C49 "MaturityDateRule", C61 "PreviousNextFactorRule"
SecurityDetails <SctyDtls> contains the following FinancialInstrumentAttributes129 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C44,
C45,
C57
459
   PlaceOfListing <PlcOfListg> [0..1] ± 460
   DayCountBasis <DayCntBsis> [0..1] ± 460
   ClassificationType <ClssfctnTp> [0..1] ± 460
   OptionStyle <OptnStyle> [0..1] ± 461
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 461
   NextCouponDate <NxtCpnDt> [0..1] Date 461
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 461
   MaturityDate <MtrtyDt> [0..1] Date 461
   IssueDate <IsseDt> [0..1] Date 461
   NextCallableDate <NxtCllblDt> [0..1] Date 462
   PutableDate <PutblDt> [0..1] Date 462
   DatedDate <DtdDt> [0..1] Date 462
   ConversionDate <ConvsDt> [0..1] Date 462
   PreviousFactor <PrvsFctr> [0..1] ± 462
   NextFactor <NxtFctr> [0..1] ± 462
   InterestRate <IntrstRate> [0..1] ± 463
   NextInterestRate <NxtIntrstRate> [0..1] ± 463
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 463
   MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C19 464
   MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C19 464
   ContractSize <CtrctSz> [0..1] ± C19 465
   IssuePrice <IssePric> [0..1] ± 465
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 458 February 2026
```

