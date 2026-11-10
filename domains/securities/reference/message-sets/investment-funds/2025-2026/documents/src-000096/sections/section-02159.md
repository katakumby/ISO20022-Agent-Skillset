---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>"]
file_pages: [3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4 MultipleOrderDetails <MltplOrdrDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3022 to 3031.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3022

```text
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
50.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
50.4.4 MultipleOrderDetails <MltplOrdrDtls>
Presence: [1..1]
Definition: General information related to the orders.
Impacted by: C7 "BulkCashSettlementDetailsRule", C26 "OrderOriginatorEligibility3Rule", C35
"SettlementCurrencyRule", C38 "TotalSettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3022 May 2026
```

## File page 3023

```text
MultipleOrderDetails <MltplOrdrDtls> contains the following SubscriptionMultipleOrder7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 3039
   PlaceOfTrade <PlcOfTrad> [0..1] ± 3039
   OrderDateTime <OrdrDtTm> [0..1] DateTime 3040
   ExpiryDateTime <XpryDtTm> [0..1] ± 3040
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 3040
   CancellationRight <CxlRght> [0..1] ± 3040
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 3041
     AccountIdentification <AcctId> [1..1] Text 3041
     AccountName <AcctNm> [0..1] Text 3041
     AccountDesignation <AcctDsgnt> [0..1] Text 3041
     OwnerIdentification <OwnrId> [0..*] ± 3042
     AccountServicer <AcctSvcr> [0..1] ± 3042
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3042
     SubAccountDetails <SubAcctDtls> [0..1] ± 3042
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3043
   BeneficiaryDetails <BnfcryDtls> [0..*] ± C28 3043
   IndividualOrderDetails <IndvOrdrDtls> [1..*]  C29,
C30,
C33
3044
     OrderReference <OrdrRef> [1..1] Text 3056
     ClientReference <ClntRef> [0..1] Text 3056
     NonceIdentification <NonceId> [0..1] Text 3056
     OrderType <OrdrTp> [0..10] ± 3057
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C21 3057
       Identification <Id> [1..1]  3059
{Or         ISIN <ISIN> [1..1] IdentifierSet 3059
Or         SEDOL <SEDOL> [1..1] IdentifierSet 3060
Or         CUSIP <CUSIP> [1..1] IdentifierSet 3060
Or         RIC <RIC> [1..1] IdentifierSet 3060
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 3060
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 3060
Or         CTA <CTA> [1..1] IdentifierSet 3060
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3023 May 2026
```

## File page 3024

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         QUICK <QUICK> [1..1] IdentifierSet 3060
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 3061
Or         Dutch <Dtch> [1..1] IdentifierSet 3061
Or         Valoren <Vlrn> [1..1] IdentifierSet 3061
Or         Sicovam <SCVM> [1..1] IdentifierSet 3061
Or         Belgian <Belgn> [1..1] IdentifierSet 3061
Or         Common <Cmon> [1..1] IdentifierSet 3061
Or         DTI <DTI> [1..1] IdentifierSet 3061
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  3061
           Identification <Id> [1..1] Text 3062
           IdentificationSource <IdSrc> [1..1] ± 3062
       Name <Nm> [0..1] Text 3062
       ShortName <ShrtNm> [0..1] Text 3062
       SupplementaryIdentification <SplmtryId> [0..1] Text 3062
       ClassType <ClssTp> [0..1] Text 3062
       SecuritiesForm <SctiesForm> [0..1] CodeSet 3063
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3063
       ProductGroup <PdctGrp> [0..1] Text 3063
       SeriesIdentification <SrsId> [0..1]  C34 3063
         SeriesDate <SrsDt> [0..1] ± 3064
         SeriesName <SrsNm> [0..1] Text 3064
     SubAccountForHolding <SubAcctForHldg> [0..1] ± 3064
     AmountOrUnits <AmtOrUnits> [1..1]  3064
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 3065
Or       GrossAmount <GrssAmt> [1..1] Amount C4, C9 3065
Or       NetAmount <NetAmt> [1..1] Amount C4, C9 3065
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3066
     Rounding <Rndg> [0..1] CodeSet 3066
     SettlementAmount <SttlmAmt> [0..1] Amount C3, C10 3066
     CashSettlementDate <CshSttlmDt> [0..1] Date 3067
     SettlementMethod <SttlmMtd> [0..1] CodeSet 3067
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3024 May 2026
```

## File page 3025

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ForeignExchangeDetails <FXDtls> [0..1]  3067
       UnitCurrency <UnitCcy> [1..1] CodeSet C3 3068
       QuotedCurrency <QtdCcy> [1..1] CodeSet C3 3068
       ExchangeRate <XchgRate> [1..1] Rate 3068
       QuotationDate <QtnDt> [0..1] DateTime 3069
       QuotingInstitution <QtgInstn> [0..1] ± 3069
     IncomePreference <IncmPref> [0..1] CodeSet 3069
     LetterIntentReference <LttrInttRef> [0..1] Text 3069
     AccumulationRightReference <AcmltnRghtRef> [0..1] Text 3070
     TransactionOverhead <TxOvrhd> [0..1]  C19 3070
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 3073
       IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
3073
         Type <Tp> [1..1]  3074
{Or           Code <Cd> [1..1] CodeSet 3074
Or}           Proprietary <Prtry> [1..1] ± 3075
         Basis <Bsis> [0..1]  3075
{Or           Code <Cd> [1..1] CodeSet 3076
Or}           Proprietary <Prtry> [1..1] ± 3076
         StandardAmount <StdAmt> [0..1] Amount C3, C10 3076
         StandardRate <StdRate> [0..1] Rate 3077
         DiscountDetails <DscntDtls> [0..1]  C16 3077
           Amount <Amt> [0..1] Amount C3, C10 3077
           Rate <Rate> [0..1] Rate 3078
           Basis <Bsis> [0..1]  3078
{Or             Code <Cd> [1..1] CodeSet 3078
Or}             Proprietary <Prtry> [1..1] ± 3079
         RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 3079
         RequestedRate <ReqdRate> [0..1] Rate 3079
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 3080
         RecipientIdentification <RcptId> [0..1] ± 3080
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3025 May 2026
```

## File page 3026

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IndividualTax <IndvTax> [0..*]  3080
         Type <Tp> [1..1]  3081
{Or           Code <Cd> [1..1] CodeSet 3081
Or}           Proprietary <Prtry> [1..1] ± 3083
         Tax <Tax> [0..1]  3083
{Or           Amount <Amt> [1..1] Amount C3, C10 3083
Or}           Rate <Rate> [1..1] Rate 3084
         Country <Ctry> [0..1] CodeSet C8 3084
         ExemptionIndicator <XmptnInd> [1..1] Indicator 3084
         ExemptionReason <XmptnRsn> [0..1]  3084
{Or           Code <Cd> [1..1] CodeSet 3084
Or}           Proprietary <Prtry> [1..1] ± 3087
         RecipientIdentification <RcptId> [0..1] ± 3087
         TaxCalculationDetails <TaxClctnDtls> [0..1]  3088
           Basis <Bsis> [1..1]  3088
{Or             Code <Cd> [1..1] CodeSet 3088
Or}             Proprietary <Prtry> [1..1] ± 3088
       DigitalNetworkFee <DgtlNtwkFee> [0..*]  3089
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
3089
           ISIN <ISIN> [0..1] IdentifierSet 3091
           OtherIdentification <OthrId> [0..*]  3091
             Identification <Id> [1..1] Text 3091
             Suffix <Sfx> [0..1] Text 3091
             Type <Tp> [1..1]  3091
{Or               Code <Cd> [1..1] CodeSet 3092
Or}               Proprietary <Prtry> [1..1] Text 3093
           Description <Desc> [0..1] Text 3093
         Quantity <Qty> [1..1]  3094
{Or           Quantity <Qty> [1..1] ± C15 3094
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3094
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3026 May 2026
```

## File page 3027

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Quantity <Qty> [1..1] Quantity 3095
             QuantityType <QtyTp> [1..1] Text 3095
             Issuer <Issr> [1..1] Text 3095
             SchemeName <SchmeNm> [0..1] Text 3095
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3095
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3095
       SettlementDate <SttlmDt> [0..1] Date 3097
       SettlementPlace <SttlmPlc> [1..1]  3097
         Party <Pty> [1..1]  3098
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 3098
Or           ProprietaryIdentification <PrtryId> [1..1] ± 3098
Or           NameAndAddress <NmAndAdr> [1..1] ± 3099
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3099
         LEI <LEI> [0..1] IdentifierSet 3099
       SafekeepingPlace <SfkpgPlc> [0..1] ± 3099
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3100
       TradeTransactionCondition <TradTxCond> [0..*] ± 3100
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3100
       ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
3101
         ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3102
           PartyIdentification <PtyId> [1..1] ± 3102
           AccountIdentification <AcctId> [0..1] Text 3102
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3102
         ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3103
           PartyIdentification <PtyId> [1..1] ± 3103
           AccountIdentification <AcctId> [0..1] Text 3103
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3103
         ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3104
           PartyIdentification <PtyId> [1..1] ± 3104
           AccountIdentification <AcctId> [0..1] Text 3104
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3027 May 2026
```

## File page 3028

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3104
         ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3105
           PartyIdentification <PtyId> [1..1] ± 3105
           AccountIdentification <AcctId> [0..1] Text 3105
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3105
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
3106
         DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3107
           PartyIdentification <PtyId> [1..1] ± 3107
           AccountIdentification <AcctId> [0..1] Text 3107
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3108
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3108
           PartyIdentification <PtyId> [1..1] ± 3108
           AccountIdentification <AcctId> [0..1] Text 3108
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3108
         DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3109
           PartyIdentification <PtyId> [1..1] ± 3109
           AccountIdentification <AcctId> [0..1] Text 3109
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3109
         DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3110
           PartyIdentification <PtyId> [1..1] ± 3110
           AccountIdentification <AcctId> [0..1] Text 3110
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3110
     PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3111
     PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3111
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 3111
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 3111
     CashSettlementDetails <CshSttlmDtls> [0..1]  3112
       PaymentInstrument <PmtInstrm> [1..1]  3117
{Or         PaymentCardDetails <PmtCardDtls> [1..1]  3122
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3028 May 2026
```

## File page 3029

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [1..1] CodeSet 3123
           Number <Nb> [1..1] Text 3123
           HolderName <HldrNm> [1..1] Text 3123
           StartDate <StartDt> [0..1] YearMonth 3123
           ExpiryDate <XpryDt> [1..1] YearMonth 3123
           CardIssuerName <CardIssrNm> [0..1] Text 3123
           CardIssuerIdentification <CardIssrId> [0..1] ± 3123
           SecurityCode <SctyCd> [0..1] Text 3124
           SequenceNumber <SeqNb> [0..1] Text 3124
Or         CreditTransferDetails <CdtTrfDtls> [1..1]  3124
           Reference <Ref> [0..1] Text 3127
           Debtor <Dbtr> [0..1] ± 3127
           DebtorAccount <DbtrAcct> [0..1]  3127
             Identification <Id> [1..1]  3127
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3128
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3128
Or}               Other <Othr> [1..1] ± 3128
             Name <Nm> [0..1] Text 3129
           DebtorAgent <DbtrAgt> [0..1]  3129
             Party <Pty> [1..1]  3129
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3130
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3130
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3130
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3131
             LEI <LEI> [0..1] IdentifierSet 3131
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  3132
             Identification <Id> [1..1]  3132
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3132
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3133
Or}               Other <Othr> [1..1] ± 3133
             Name <Nm> [0..1] Text 3133
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3029 May 2026
```

## File page 3030

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  3133
             Party <Pty> [1..1]  3134
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3134
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3134
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3135
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3136
             LEI <LEI> [0..1] IdentifierSet 3136
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3137
             Identification <Id> [1..1]  3137
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3137
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3138
Or}               Other <Othr> [1..1] ± 3138
             Name <Nm> [0..1] Text 3138
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  3138
             Party <Pty> [1..1]  3139
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3139
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3139
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3140
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3141
             LEI <LEI> [0..1] IdentifierSet 3141
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3142
             Identification <Id> [1..1]  3142
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3142
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3143
Or}               Other <Othr> [1..1] ± 3143
             Name <Nm> [0..1] Text 3143
           CreditorAgent <CdtrAgt> [1..1]  3143
             Party <Pty> [1..1]  3144
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3144
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3144
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3030 May 2026
```

## File page 3031

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3145
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3146
             LEI <LEI> [0..1] IdentifierSet 3146
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  3147
             Identification <Id> [1..1]  3147
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3147
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3148
Or}               Other <Othr> [1..1] ± 3148
             Name <Nm> [0..1] Text 3148
           Creditor <Cdtr> [0..1] ± 3148
           CreditorAccount <CdtrAcct> [1..1]  3149
             Identification <Id> [1..1]  3149
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3149
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3150
Or}               Other <Othr> [1..1] ± 3150
             Name <Nm> [0..1] Text 3150
Or         DirectDebitDetails <DrctDbtDtls> [1..1]  3150
           DebtorAccount <DbtrAcct> [1..1]  3151
             Identification <Id> [1..1]  3152
{Or               IBAN <IBAN> [1..1] IdentifierSet C20 3152
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3152
Or}               Other <Othr> [1..1] ± 3153
             Name <Nm> [0..1] Text 3153
           Debtor <Dbtr> [0..1] ± 3153
           DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3153
           DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3154
           Creditor <Cdtr> [0..1] ± 3154
           DebtorAgent <DbtrAgt> [1..1]  3154
             Party <Pty> [1..1]  3154
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3155
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3155
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3031 May 2026
```

