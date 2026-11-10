---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.1 SecurityDetails <SctyDtls>"]
file_pages: [174, 175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.1 SecurityDetails <SctyDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 174 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FinancialTransactionTaxRate <FinTxTaxRate> [0..1] ± 194
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 194
     SecondLevelTax <ScndLvlTax> [0..*] ± 195
   PriceDetails <PricDtls> [0..1]  C40 195
     IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  196
{Or       IndicativePrice <IndctvPric> [1..1] ± 196
Or}       MarketPrice <MktPric> [1..1] ± 197
     CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 197
     CashValueForTax <CshValForTax> [0..1] ± 197
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 198
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 198
   AmountDetails <AmtDtls> [0..1]  199
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 199
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 200
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
3.4.11.24.1  SecurityDetails <SctyDtls>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 174 February 2026
```

## File page 175

```text
Definition: Provides description of the financial instrument related to securities movement.
Impacted by: C71 "MaturityDateRule", C95 "PreviousNextFactorRule"
SecurityDetails <SctyDtls> contains the following FinancialInstrumentAttributes129 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C23,
C24,
C61,
C62,
C91
176
   PlaceOfListing <PlcOfListg> [0..1] ± 177
   DayCountBasis <DayCntBsis> [0..1] ± 177
   ClassificationType <ClssfctnTp> [0..1] ± 177
   OptionStyle <OptnStyle> [0..1] ± 178
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 178
   NextCouponDate <NxtCpnDt> [0..1] Date 178
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 178
   MaturityDate <MtrtyDt> [0..1] Date 178
   IssueDate <IsseDt> [0..1] Date 178
   NextCallableDate <NxtCllblDt> [0..1] Date 179
   PutableDate <PutblDt> [0..1] Date 179
   DatedDate <DtdDt> [0..1] Date 179
   ConversionDate <ConvsDt> [0..1] Date 179
   PreviousFactor <PrvsFctr> [0..1] ± 179
   NextFactor <NxtFctr> [0..1] ± 179
   InterestRate <IntrstRate> [0..1] ± 180
   NextInterestRate <NxtIntrstRate> [0..1] ± 180
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C25 180
   MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C25 181
   MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C25 181
   ContractSize <CtrctSz> [0..1] ± C25 182
   IssuePrice <IssePric> [0..1] ± 182
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 175 February 2026
```

