---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.8 FinancialInstrumentDetails <FinInstrmDtls>", "49.4.5.8.9 SeriesIdentification <SrsId>", "49.4.5.8.9.1 SeriesDate <SrsDt>"]
file_pages: [2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.8.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2813 to 2822.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2813

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
49.4.5.8.9.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
49.4.5.8.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
49.4.5.9  IndividualExecutionDetails <IndvExctnDtls>
Presence: [1..*]
Definition: Execution of a subscription order.
Impacted by: C26 "OrderOriginatorEligibility3Rule", C30 "PhysicalDeliveryDetails1Rule", C31
"PhysicalDeliveryDetails2Rule", C32 "PriceDifferenceReasonRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2813 May 2026
```

## File page 2814

```text
IndividualExecutionDetails <IndvExctnDtls> contains the following SubscriptionExecution15
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 2824
   ClientReference <ClntRef> [0..1] Text 2824
   DealReference <DealRef> [1..1] Text 2824
   NonceIdentification <NonceId> [0..1] Text 2824
   OrderType <OrdrTp> [0..10] ± 2825
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 2825
     AccountIdentification <AcctId> [1..1] Text 2825
     AccountName <AcctNm> [0..1] Text 2826
     AccountDesignation <AcctDsgnt> [0..1] Text 2826
     OwnerIdentification <OwnrId> [0..*] ± 2826
     AccountServicer <AcctSvcr> [0..1] ± 2826
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 2826
     SubAccountDetails <SubAcctDtls> [0..1] ± 2827
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2827
   BeneficiaryDetails <BnfcryDtls> [0..*] ± C29 2827
   Units <Units> [1..1]  2828
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 2828
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2828
   Rounding <Rndg> [0..1] CodeSet 2829
   NetAmount <NetAmt> [0..1] Amount C3, C10 2829
   GrossAmount <GrssAmt> [0..1] Amount C3, C10 2829
   TradeDateTime <TradDtTm> [1..1] ± 2830
   DealingPriceDetails <DealgPricDtls> [1..1] ± 2830
   InformativePriceDetails <InftvPricDtls> [0..2] ± 2830
   SettlementAmount <SttlmAmt> [1..1] Amount C3, C10 2831
   CashSettlementDate <CshSttlmDt> [0..1] Date 2831
   SettlementMethod <SttlmMtd> [0..1] CodeSet 2831
   PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 2832
   BestExecution <BestExctn> [0..1] CodeSet 2832
   CumDividendIndicator <CumDvddInd> [1..1] Indicator 2832
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2814 May 2026
```

## File page 2815

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterimProfitAmount <IntrmPrftAmt> [0..1] ± 2832
   ForeignExchangeDetails <FXDtls> [0..*] ± 2833
   IncomePreference <IncmPref> [0..1] CodeSet 2833
   LetterIntentReference <LttrInttRef> [0..1] Text 2834
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 2834
   TransactionOverhead <TxOvrhd> [0..1]  C23,
C39
2834
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 2836
     TotalFees <TtlFees> [0..1] Amount C3, C10 2837
     TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 2837
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2837
     IndividualFee <IndvFee> [0..*]  C6 2838
       Type <Tp> [1..1]  2838
{Or         Code <Cd> [1..1] CodeSet 2839
Or}         Proprietary <Prtry> [1..1] ± 2840
       Basis <Bsis> [0..1]  2840
{Or         Code <Cd> [1..1] CodeSet 2840
Or}         Proprietary <Prtry> [1..1] ± 2841
       StandardAmount <StdAmt> [0..1] Amount C3, C10 2841
       StandardRate <StdRate> [0..1] Rate 2841
       DiscountDetails <DscntDtls> [0..1]  C17 2842
         Amount <Amt> [0..1] Amount C3, C10 2842
         Rate <Rate> [0..1] Rate 2843
         Basis <Bsis> [0..1]  2843
{Or           Code <Cd> [1..1] CodeSet 2843
Or}           Proprietary <Prtry> [1..1] ± 2843
       AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2844
       AppliedRate <ApldRate> [0..1] Rate 2844
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 2844
       RecipientIdentification <RcptId> [0..1] ± 2844
       InformativeIndicator <InftvInd> [1..1] Indicator 2845
     IndividualTax <IndvTax> [0..*] ± 2845
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2815 May 2026
```

## File page 2816

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DigitalNetworkFee <DgtlNtwkFee> [0..*]  2845
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2846
         ISIN <ISIN> [0..1] IdentifierSet 2848
         OtherIdentification <OthrId> [0..*]  2848
           Identification <Id> [1..1] Text 2848
           Suffix <Sfx> [0..1] Text 2848
           Type <Tp> [1..1]  2848
{Or             Code <Cd> [1..1] CodeSet 2849
Or}             Proprietary <Prtry> [1..1] Text 2850
         Description <Desc> [0..1] Text 2850
       Quantity <Qty> [1..1]  2851
{Or         Quantity <Qty> [1..1] ± C16 2851
Or}         ProprietaryQuantity <PrtryQty> [1..1]  2851
           Quantity <Qty> [1..1] Quantity 2852
           QuantityType <QtyTp> [1..1] Text 2852
           Issuer <Issr> [1..1] Text 2852
           SchemeName <SchmeNm> [0..1] Text 2852
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2852
   InformativeTaxDetails <InftvTaxDtls> [0..1] ± C38 2852
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2854
     SettlementDate <SttlmDt> [0..1] Date 2856
     SettlementPlace <SttlmPlc> [1..1]  2856
       Party <Pty> [1..1]  2857
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2857
Or         ProprietaryIdentification <PrtryId> [1..1] ± 2857
Or         NameAndAddress <NmAndAdr> [1..1] ± 2858
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2858
       LEI <LEI> [0..1] IdentifierSet 2858
     SafekeepingPlace <SfkpgPlc> [0..1] ± 2858
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2816 May 2026
```

## File page 2817

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2859
     TradeTransactionCondition <TradTxCond> [0..*] ± 2859
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2859
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C33,
C34
2860
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2861
         PartyIdentification <PtyId> [1..1] ± 2861
         AccountIdentification <AcctId> [0..1] Text 2861
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2861
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2862
         PartyIdentification <PtyId> [1..1] ± 2862
         AccountIdentification <AcctId> [0..1] Text 2862
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2862
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2863
         PartyIdentification <PtyId> [1..1] ± 2863
         AccountIdentification <AcctId> [0..1] Text 2863
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2863
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2864
         PartyIdentification <PtyId> [1..1] ± 2864
         AccountIdentification <AcctId> [0..1] Text 2864
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2864
     DeliveringSideDetails <DlvrgSdDtls> [1..1]  C12,
C13
2865
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2866
         PartyIdentification <PtyId> [1..1] ± 2866
         AccountIdentification <AcctId> [0..1] Text 2866
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2867
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2867
         PartyIdentification <PtyId> [1..1] ± 2867
         AccountIdentification <AcctId> [0..1] Text 2867
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2817 May 2026
```

## File page 2818

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2867
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2868
         PartyIdentification <PtyId> [1..1] ± 2868
         AccountIdentification <AcctId> [0..1] Text 2868
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2868
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2869
         PartyIdentification <PtyId> [1..1] ± 2869
         AccountIdentification <AcctId> [0..1] Text 2869
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2869
   PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 2870
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 2870
   StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 2870
   Refund <Rfnd> [0..1] Amount C3, C10 2870
   SubscriptionInterest <SbcptIntrst> [0..1] Amount C3, C10 2871
   CashSettlementDetails <CshSttlmDtls> [0..1]  2871
     PaymentInstrument <PmtInstrm> [1..1]  2876
{Or       PaymentCardDetails <PmtCardDtls> [1..1]  2881
         Type <Tp> [1..1] CodeSet 2882
         Number <Nb> [1..1] Text 2882
         HolderName <HldrNm> [1..1] Text 2882
         StartDate <StartDt> [0..1] YearMonth 2882
         ExpiryDate <XpryDt> [1..1] YearMonth 2882
         CardIssuerName <CardIssrNm> [0..1] Text 2882
         CardIssuerIdentification <CardIssrId> [0..1] ± 2882
         SecurityCode <SctyCd> [0..1] Text 2883
         SequenceNumber <SeqNb> [0..1] Text 2883
Or       CreditTransferDetails <CdtTrfDtls> [1..1]  2883
         Reference <Ref> [0..1] Text 2886
         Debtor <Dbtr> [0..1] ± 2886
         DebtorAccount <DbtrAcct> [0..1]  2886
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2818 May 2026
```

## File page 2819

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  2886
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2887
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2887
Or}             Other <Othr> [1..1] ± 2887
           Name <Nm> [0..1] Text 2888
         DebtorAgent <DbtrAgt> [0..1]  2888
           Party <Pty> [1..1]  2888
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2889
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2889
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2889
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2890
           LEI <LEI> [0..1] IdentifierSet 2890
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  2891
           Identification <Id> [1..1]  2891
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2891
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2892
Or}             Other <Othr> [1..1] ± 2892
           Name <Nm> [0..1] Text 2892
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  2892
           Party <Pty> [1..1]  2893
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2893
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2893
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2894
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2895
           LEI <LEI> [0..1] IdentifierSet 2895
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2896
           Identification <Id> [1..1]  2896
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2896
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2897
Or}             Other <Othr> [1..1] ± 2897
           Name <Nm> [0..1] Text 2897
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2819 May 2026
```

## File page 2820

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  2897
           Party <Pty> [1..1]  2898
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2898
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2898
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2899
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2900
           LEI <LEI> [0..1] IdentifierSet 2900
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2901
           Identification <Id> [1..1]  2901
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2901
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2902
Or}             Other <Othr> [1..1] ± 2902
           Name <Nm> [0..1] Text 2902
         CreditorAgent <CdtrAgt> [1..1]  2902
           Party <Pty> [1..1]  2903
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2903
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2903
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2904
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2905
           LEI <LEI> [0..1] IdentifierSet 2905
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  2906
           Identification <Id> [1..1]  2906
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2906
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2907
Or}             Other <Othr> [1..1] ± 2907
           Name <Nm> [0..1] Text 2907
         Creditor <Cdtr> [0..1] ± 2907
         CreditorAccount <CdtrAcct> [1..1]  2908
           Identification <Id> [1..1]  2908
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2908
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2909
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2820 May 2026
```

## File page 2821

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             Other <Othr> [1..1] ± 2909
           Name <Nm> [0..1] Text 2909
Or       DirectDebitDetails <DrctDbtDtls> [1..1]  2909
         DebtorAccount <DbtrAcct> [1..1]  2910
           Identification <Id> [1..1]  2911
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2911
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2911
Or}             Other <Othr> [1..1] ± 2912
           Name <Nm> [0..1] Text 2912
         Debtor <Dbtr> [0..1] ± 2912
         DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2912
         DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2913
         Creditor <Cdtr> [0..1] ± 2913
         DebtorAgent <DbtrAgt> [1..1]  2913
           Party <Pty> [1..1]  2913
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2914
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2914
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2914
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2915
           LEI <LEI> [0..1] IdentifierSet 2915
         DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2916
         CreditorAgent <CdtrAgt> [0..1]  2916
           Party <Pty> [1..1]  2916
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2917
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2917
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2917
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2918
           LEI <LEI> [0..1] IdentifierSet 2918
         CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2919
         RegistrationIdentification <RegnId> [0..1] Text 2919
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2821 May 2026
```

## File page 2822

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         MandateIdentification <MndtId> [0..1] Text 2919
Or       ChequeDetails <ChqDtls> [1..1]  2919
         Number <Nb> [0..1] Text 2920
         PayeeIdentification <PyeeId> [1..1] ± 2920
         DraweeIdentification <DrweeId> [0..1]  2920
           Party <Pty> [1..1]  2921
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2921
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2921
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2922
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2923
           LEI <LEI> [0..1] IdentifierSet 2923
         DrawerIdentification <DrwrId> [0..1] ± 2924
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  2924
         Number <Nb> [0..1] Text 2924
         PayeeIdentification <PyeeId> [1..1] ± 2924
         DraweeIdentification <DrweeId> [0..1]  2925
           Party <Pty> [1..1]  2925
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2925
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2926
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2926
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2927
           LEI <LEI> [0..1] IdentifierSet 2927
         DrawerIdentification <DrwrId> [0..1] ± 2928
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 2928
         AccountIdentification <AcctId> [0..1] Text 2928
         Type <Tp> [0..1] ± 2928
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  2929
         Identification <Id> [1..1] Text 2929
         Type <Tp> [0..1] ± 2929
         Name <Nm> [0..1] Text 2929
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2930
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2822 May 2026
```

