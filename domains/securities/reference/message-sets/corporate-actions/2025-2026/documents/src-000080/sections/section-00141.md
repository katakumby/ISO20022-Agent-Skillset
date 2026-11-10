---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.19 AmountDetails <AmtDtls>", "3.4.11.24.19.2 SecondLevelTaxAmount <ScndLvlTaxAmt>"]
file_pages: [200, 201, 202, 203]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.19.2 SecondLevelTaxAmount <ScndLvlTaxAmt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 200 to 203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.11.24.19.2  SecondLevelTaxAmount <ScndLvlTaxAmt>
Presence: [0..1]
Definition: Amount of money withheld by the jurisdiction other than the jurisdiction of the issuer's
country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is levied in
complement or offset of the withholding tax rate levied by the jurisdiction of the issuer's tax domicile.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.11.25  CashMovementDetails <CshMvmntDtls>
Presence: [0..*]
Definition: Provides information about the cash movement linked to the corporate action option.
Impacted by: C35 "ExemptionTypeUsageRule", C51 "IncomeType2Rule", C53
"IncomeTypeUsageRule", C65 "IssuerOfferorTaxabilityIndicatorUsageRule", C41
"GenericCashPricePerProductGuideline"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 200 February 2026
```

## File page 201

```text
CashMovementDetails <CshMvmntDtls> contains the following CashOption116 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 204
   ContractualPaymentIndicator <CtrctlPmtInd> [0..1] CodeSet 205
   NonEligibleProceedsIndicator <NonElgblPrcdsInd> [0..1]  205
{Or     Code <Cd> [1..1] CodeSet 205
Or}     Proprietary <Prtry> [1..1] ± 205
   IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> [0..1]  206
{Or     Code <Cd> [1..1] CodeSet 206
Or}     Proprietary <Prtry> [1..1] ± 206
   IncomeType <IncmTp> [0..1] ± 206
   OtherIncomeType <OthrIncmTp> [0..*] ± 207
   ExemptionType <XmptnTp> [0..*] ± 207
   PriceCalculationMethod <PricClctnMtd> [0..1]  207
{Or     Code <Cd> [1..1] CodeSet 208
Or}     Proprietary <Prtry> [1..1] ± 208
   CountryOfIncomeSource <CtryOfIncmSrc> [0..1] CodeSet C17 208
   CashAccountIdentification <CshAcctId> [0..1] ± 209
   AmountDetails <AmtDtls> [0..1]  209
     GrossAmount <GrssAmt> [0..1] Amount C2, C18 211
     NetAmount <NetAmt> [0..1] Amount C2, C18 212
     SolicitationFees <SlctnFees> [0..1] Amount C2, C18 212
     CashInLieuOfShare <CshInLieuOfShr> [0..1] Amount C2, C18 212
     CapitalGain <CptlGn> [0..1] Amount C2, C18 213
     InterestAmount <IntrstAmt> [0..1] Amount C2, C18 213
     IndemnityAmount <IndmntyAmt> [0..1] Amount C2, C18 214
     ManufacturedDividendPaymentAmount
<ManfctrdDvddPmtAmt>
[0..1] Amount C2, C18 214
     ReinvestmentAmount <RinvstmtAmt> [0..1] Amount C2, C18 215
     FullyFrankedAmount <FullyFrnkdAmt> [0..1] Amount C2, C18 215
     UnfrankedAmount <UfrnkdAmt> [0..1] Amount C2, C18 215
     SundryOrOtherAmount <SndryOrOthrAmt> [0..1] Amount C2, C18 216
     TaxFreeAmount <TaxFreeAmt> [0..1] Amount C2, C18 216
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 201 February 2026
```

## File page 202

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxDeferredAmount <TaxDfrrdAmt> [0..1] Amount C2, C18 217
     ValueAddedTaxAmount <ValAddedTaxAmt> [0..1] Amount C2, C18 217
     StampDutyAmount <StmpDtyAmt> [0..1] Amount C2, C18 217
     TaxReclaimAmount <TaxRclmAmt> [0..1] Amount C2, C18 218
     TaxCreditAmount <TaxCdtAmt> [0..1] Amount C2, C18 218
     AdditionalTaxAmount <AddtlTaxAmt> [0..1] Amount C2, C18 219
     WithholdingTaxAmount <WhldgTaxAmt> [0..1] Amount C2, C18 219
     SecondLevelTaxAmount <ScndLvlTaxAmt> [0..1] Amount C2, C18 219
     FiscalStampAmount <FsclStmpAmt> [0..1] Amount C2, C18 220
     ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] Amount C2, C18 220
     PayingAgentCommissionAmount
<PngAgtComssnAmt>
[0..1] Amount C2, C18 221
     LocalBrokerCommissionAmount
<LclBrkrComssnAmt>
[0..1] Amount C2, C18 221
     RegulatoryFeesAmount <RgltryFeesAmt> [0..1] Amount C2, C18 221
     ShippingFeesAmount <ShppgFeesAmt> [0..1] Amount C2, C18 222
     ChargesAmount <ChrgsAmt> [0..1] Amount C2, C18 222
     EntitledAmount <EntitldAmt> [0..1] Amount C2, C18 223
     OriginalAmount <OrgnlAmt> [0..1] Amount C2, C18 223
     PrincipalOrCorpus <PrncplOrCrps> [0..1] Amount C2, C18 223
     RedemptionPremiumAmount <RedPrmAmt> [0..1] Amount C2, C18 224
     IncomePortion <IncmPrtn> [0..1] Amount C2, C18 224
     StockExchangeTax <StockXchgTax> [0..1] Amount C2, C18 225
     EUTaxRetentionAmount <EUTaxRtntnAmt> [0..1] Amount C2, C18 225
     AccruedInterestAmount <AcrdIntrstAmt> [0..1] Amount C2, C18 225
     EqualisationAmount <EqulstnAmt> [0..1] Amount C2, C18 226
     FATCATaxAmount <FATCATaxAmt> [0..1] Amount C2, C18 226
     NRATaxAmount <NRATaxAmt> [0..1] Amount C2, C18 227
     BackUpWithholdingTaxAmount
<BckUpWhldgTaxAmt>
[0..1] Amount C2, C18 227
     TaxOnIncomeAmount <TaxOnIncmAmt> [0..1] Amount C2, C18 227
     TransactionTax <TxTax> [0..1] Amount C2, C18 228
     DeemedAmount <DmdAmt> [0..1] Amount C2, C18 228
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 202 February 2026
```

## File page 203

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ForeignIncomeAmount <FrgnIncmAmt> [0..1] Amount C2, C18 229
     DeemedDividendAmount <DmdDvddAmt> [0..1] Amount C2, C18 229
     DeemedFundAmount <DmdFndAmt> [0..1] Amount C2, C18 229
     DeemedInterestAmount <DmdIntrstAmt> [0..1] Amount C2, C18 230
     DeemedRoyaltiesAmount <DmdRyltsAmt> [0..1] Amount C2, C18 230
     BuyUpAmount <BuyUpAmt> [0..1] Amount C2, C18 231
   DateDetails <DtDtls> [1..1]  231
     PaymentDate <PmtDt> [1..1] ± 231
     ValueDate <ValDt> [0..1] ± 232
     ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 232
     EarliestPaymentDate <EarlstPmtDt> [0..1] ± 232
   ForeignExchangeDetails <FXDtls> [0..1] ± 233
   RateAndAmountDetails <RateAndAmtDtls> [0..1]  C21,
C22,
C44,
C46,
C79,
C81,
C106,
C108,
C110,
C115,
C117
233
     AdditionalTax <AddtlTax> [0..1] ± 236
     GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 236
     GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 236
     WithholdingTaxRate <WhldgTaxRate> [0..*] ± 237
     SecondLevelTax <ScndLvlTax> [0..*] ± 237
     ChargesFees <ChrgsFees> [0..1] ± 238
     EarlySolicitationFeeRate <EarlySlctnFeeRate> [0..1] ± 238
     FiscalStamp <FsclStmp> [0..1] ± 239
     ThirdPartyIncentiveRate <ThrdPtyIncntivRate> [0..1] ± 239
     NetDistributionRate <NetDstrbtnRate> [0..*] ± 239
     ApplicableRate <AplblRate> [0..1] ± 240
     SolicitationFeeRate <SlctnFeeRate> [0..1] ± 240
     TaxCreditRate <TaxCdtRate> [0..1] ± 241
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 203 February 2026
```

