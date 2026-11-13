---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks"]
file_pages: [2787, 2788, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C38", "C39", "C40"], "until_heading": "49.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2787, "topic": "49.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01990.md"}]
---

# 49.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2787 to 2796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 2787, C38–C40 before **49.4 Message Building Blocks** continue [49.3 Constraints](section-01990.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 2787

```text
C38 TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
C39 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C40 WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
49.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
49.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
49.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
49.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2787 May 2026
```

## File page 2788

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
49.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
49.4.5 BulkExecutionDetails <BlkExctnDtls>
Presence: [1..1]
Definition: General information related to the execution of the orders.
Impacted by: C8 "BulkCashSettlementDetailsRule", C35 "RequestedSettlementCurrencyRule", C37
"SettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2788 May 2026
```

## File page 2789

```text
BulkExecutionDetails <BlkExctnDtls> contains the following SubscriptionBulkExecution05
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 2805
   MasterReference <MstrRef> [0..1] Text 2805
   PlaceOfTrade <PlcOfTrad> [0..1] ± 2805
   OrderDateTime <OrdrDtTm> [0..1] DateTime 2805
   ReceivedDateTime <RcvdDtTm> [0..1] DateTime 2806
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 2806
   CancellationRight <CxlRght> [0..1] ± 2806
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 2806
     Identification <Id> [1..1]  2808
{Or       ISIN <ISIN> [1..1] IdentifierSet 2808
Or       SEDOL <SEDOL> [1..1] IdentifierSet 2809
Or       CUSIP <CUSIP> [1..1] IdentifierSet 2809
Or       RIC <RIC> [1..1] IdentifierSet 2809
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 2809
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 2809
Or       CTA <CTA> [1..1] IdentifierSet 2809
Or       QUICK <QUICK> [1..1] IdentifierSet 2809
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 2810
Or       Dutch <Dtch> [1..1] IdentifierSet 2810
Or       Valoren <Vlrn> [1..1] IdentifierSet 2810
Or       Sicovam <SCVM> [1..1] IdentifierSet 2810
Or       Belgian <Belgn> [1..1] IdentifierSet 2810
Or       Common <Cmon> [1..1] IdentifierSet 2810
Or       DTI <DTI> [1..1] IdentifierSet 2810
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  2810
         Identification <Id> [1..1] Text 2811
         IdentificationSource <IdSrc> [1..1] ± 2811
     Name <Nm> [0..1] Text 2811
     ShortName <ShrtNm> [0..1] Text 2811
     SupplementaryIdentification <SplmtryId> [0..1] Text 2811
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2789 May 2026
```

## File page 2790

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ClassType <ClssTp> [0..1] Text 2811
     SecuritiesForm <SctiesForm> [0..1] CodeSet 2812
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2812
     ProductGroup <PdctGrp> [0..1] Text 2812
     SeriesIdentification <SrsId> [0..1]  C36 2812
       SeriesDate <SrsDt> [0..1] ± 2813
       SeriesName <SrsNm> [0..1] Text 2813
   IndividualExecutionDetails <IndvExctnDtls> [1..*]  C26,
C30,
C31,
C32
2813
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
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 2828
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2828
     Rounding <Rndg> [0..1] CodeSet 2829
     NetAmount <NetAmt> [0..1] Amount C3, C10 2829
     GrossAmount <GrssAmt> [0..1] Amount C3, C10 2829
     TradeDateTime <TradDtTm> [1..1] ± 2830
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2790 May 2026
```

## File page 2791

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DealingPriceDetails <DealgPricDtls> [1..1] ± 2830
     InformativePriceDetails <InftvPricDtls> [0..2] ± 2830
     SettlementAmount <SttlmAmt> [1..1] Amount C3, C10 2831
     CashSettlementDate <CshSttlmDt> [0..1] Date 2831
     SettlementMethod <SttlmMtd> [0..1] CodeSet 2831
     PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 2832
     BestExecution <BestExctn> [0..1] CodeSet 2832
     CumDividendIndicator <CumDvddInd> [1..1] Indicator 2832
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
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 2837
       IndividualFee <IndvFee> [0..*]  C6 2838
         Type <Tp> [1..1]  2838
{Or           Code <Cd> [1..1] CodeSet 2839
Or}           Proprietary <Prtry> [1..1] ± 2840
         Basis <Bsis> [0..1]  2840
{Or           Code <Cd> [1..1] CodeSet 2840
Or}           Proprietary <Prtry> [1..1] ± 2841
         StandardAmount <StdAmt> [0..1] Amount C3, C10 2841
         StandardRate <StdRate> [0..1] Rate 2841
         DiscountDetails <DscntDtls> [0..1]  C17 2842
           Amount <Amt> [0..1] Amount C3, C10 2842
           Rate <Rate> [0..1] Rate 2843
           Basis <Bsis> [0..1]  2843
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2791 May 2026
```

## File page 2792

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 2843
Or}             Proprietary <Prtry> [1..1] ± 2843
         AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2844
         AppliedRate <ApldRate> [0..1] Rate 2844
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 2844
         RecipientIdentification <RcptId> [0..1] ± 2844
         InformativeIndicator <InftvInd> [1..1] Indicator 2845
       IndividualTax <IndvTax> [0..*] ± 2845
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
{Or               Code <Cd> [1..1] CodeSet 2849
Or}               Proprietary <Prtry> [1..1] Text 2850
           Description <Desc> [0..1] Text 2850
         Quantity <Qty> [1..1]  2851
{Or           Quantity <Qty> [1..1] ± C16 2851
Or}           ProprietaryQuantity <PrtryQty> [1..1]  2851
             Quantity <Qty> [1..1] Quantity 2852
             QuantityType <QtyTp> [1..1] Text 2852
             Issuer <Issr> [1..1] Text 2852
             SchemeName <SchmeNm> [0..1] Text 2852
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2852
     InformativeTaxDetails <InftvTaxDtls> [0..1] ± C38 2852
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2854
       SettlementDate <SttlmDt> [0..1] Date 2856
       SettlementPlace <SttlmPlc> [1..1]  2856
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2792 May 2026
```

## File page 2793

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Party <Pty> [1..1]  2857
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2857
Or           ProprietaryIdentification <PrtryId> [1..1] ± 2857
Or           NameAndAddress <NmAndAdr> [1..1] ± 2858
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2858
         LEI <LEI> [0..1] IdentifierSet 2858
       SafekeepingPlace <SfkpgPlc> [0..1] ± 2858
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
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2793 May 2026
```

## File page 2794

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PartyIdentification <PtyId> [1..1] ± 2866
           AccountIdentification <AcctId> [0..1] Text 2866
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2867
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2867
           PartyIdentification <PtyId> [1..1] ± 2867
           AccountIdentification <AcctId> [0..1] Text 2867
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
{Or         PaymentCardDetails <PmtCardDtls> [1..1]  2881
           Type <Tp> [1..1] CodeSet 2882
           Number <Nb> [1..1] Text 2882
           HolderName <HldrNm> [1..1] Text 2882
           StartDate <StartDt> [0..1] YearMonth 2882
           ExpiryDate <XpryDt> [1..1] YearMonth 2882
           CardIssuerName <CardIssrNm> [0..1] Text 2882
           CardIssuerIdentification <CardIssrId> [0..1] ± 2882
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2794 May 2026
```

## File page 2795

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           SecurityCode <SctyCd> [0..1] Text 2883
           SequenceNumber <SeqNb> [0..1] Text 2883
Or         CreditTransferDetails <CdtTrfDtls> [1..1]  2883
           Reference <Ref> [0..1] Text 2886
           Debtor <Dbtr> [0..1] ± 2886
           DebtorAccount <DbtrAcct> [0..1]  2886
             Identification <Id> [1..1]  2886
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2887
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2887
Or}               Other <Othr> [1..1] ± 2887
             Name <Nm> [0..1] Text 2888
           DebtorAgent <DbtrAgt> [0..1]  2888
             Party <Pty> [1..1]  2888
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2889
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2889
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2889
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2890
             LEI <LEI> [0..1] IdentifierSet 2890
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  2891
             Identification <Id> [1..1]  2891
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2891
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2892
Or}               Other <Othr> [1..1] ± 2892
             Name <Nm> [0..1] Text 2892
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  2892
             Party <Pty> [1..1]  2893
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2893
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2893
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2894
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2895
             LEI <LEI> [0..1] IdentifierSet 2895
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2795 May 2026
```

## File page 2796

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2896
             Identification <Id> [1..1]  2896
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2896
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2897
Or}               Other <Othr> [1..1] ± 2897
             Name <Nm> [0..1] Text 2897
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  2897
             Party <Pty> [1..1]  2898
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2898
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2898
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2899
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2900
             LEI <LEI> [0..1] IdentifierSet 2900
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2901
             Identification <Id> [1..1]  2901
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2901
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2902
Or}               Other <Othr> [1..1] ± 2902
             Name <Nm> [0..1] Text 2902
           CreditorAgent <CdtrAgt> [1..1]  2902
             Party <Pty> [1..1]  2903
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2903
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2903
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2904
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2905
             LEI <LEI> [0..1] IdentifierSet 2905
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  2906
             Identification <Id> [1..1]  2906
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2906
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2907
Or}               Other <Othr> [1..1] ± 2907
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2796 May 2026
```

