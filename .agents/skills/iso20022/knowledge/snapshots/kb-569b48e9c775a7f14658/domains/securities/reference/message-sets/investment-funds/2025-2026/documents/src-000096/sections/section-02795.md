---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>"]
file_pages: [3929, 3930, 3931, 3932, 3933, 3934, 3935]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3929 to 3935.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3929

```text
55.4.5.20  SubscriptionLegDetails <SbcptLegDtls>
Presence: [1..*]
Definition: Subscription leg of a switch order execution.
Impacted by: C29 "PhysicalDeliveryDetails1Rule", C31 "PhysicalDeliveryDetails2Rule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3929 May 2026
```

## File page 3930

```text
SubscriptionLegDetails <SbcptLegDtls> contains the following SwitchSubscriptionLegExecution5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LegIdentification <LegId> [0..1] Text 3936
   LegExecutionIdentification <LegExctnId> [0..1] Text 3936
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C18 3936
     Identification <Id> [1..1]  3938
{Or       ISIN <ISIN> [1..1] IdentifierSet 3938
Or       SEDOL <SEDOL> [1..1] IdentifierSet 3939
Or       CUSIP <CUSIP> [1..1] IdentifierSet 3939
Or       RIC <RIC> [1..1] IdentifierSet 3939
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 3939
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 3939
Or       CTA <CTA> [1..1] IdentifierSet 3939
Or       QUICK <QUICK> [1..1] IdentifierSet 3939
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 3940
Or       Dutch <Dtch> [1..1] IdentifierSet 3940
Or       Valoren <Vlrn> [1..1] IdentifierSet 3940
Or       Sicovam <SCVM> [1..1] IdentifierSet 3940
Or       Belgian <Belgn> [1..1] IdentifierSet 3940
Or       Common <Cmon> [1..1] IdentifierSet 3940
Or       DTI <DTI> [1..1] IdentifierSet 3940
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  3940
         Identification <Id> [1..1] Text 3941
         IdentificationSource <IdSrc> [1..1] ± 3941
     Name <Nm> [0..1] Text 3941
     ShortName <ShrtNm> [0..1] Text 3941
     SupplementaryIdentification <SplmtryId> [0..1] Text 3941
     ClassType <ClssTp> [0..1] Text 3941
     SecuritiesForm <SctiesForm> [0..1] CodeSet 3942
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3942
     ProductGroup <PdctGrp> [0..1] Text 3942
     SeriesIdentification <SrsId> [0..1]  C34 3942
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3930 May 2026
```

## File page 3931

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SeriesDate <SrsDt> [0..1] ± 3943
       SeriesName <SrsNm> [0..1] Text 3943
   Units <Units> [1..1]  3943
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 3943
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3943
   NetAmount <NetAmt> [0..1] Amount C2, C8 3944
   GrossAmount <GrssAmt> [0..1] Amount C2, C8 3944
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C25 3944
     AccountIdentification <AcctId> [1..1] Text 3945
     AccountName <AcctNm> [0..1] Text 3945
     AccountDesignation <AcctDsgnt> [0..1] Text 3945
     OwnerIdentification <OwnrId> [0..*] ± 3945
     AccountServicer <AcctSvcr> [0..1] ± 3946
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3946
     SubAccountDetails <SubAcctDtls> [0..1] ± 3946
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3947
   TradeDateTime <TradDtTm> [1..1] ± 3947
   PriceDetails <PricDtls> [1..1] ± 3947
   InformativePriceDetails <InftvPricDtls> [0..2] ± 3948
   CumDividendIndicator <CumDvddInd> [1..1] Indicator 3948
   InterimProfitAmount <IntrmPrftAmt> [0..1] ± 3949
   IncomePreference <IncmPref> [0..1] CodeSet 3949
   RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C2 3949
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C3 3949
   TransactionOverhead <TxOvrhd> [0..1]  C23,
C36
3950
     TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C2, C8 3952
     TotalFees <TtlFees> [0..1] Amount C2, C8 3953
     TotalTaxes <TtlTaxs> [0..1] Amount C2, C8 3953
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3953
     IndividualFee <IndvFee> [0..*]  C5 3954
       Type <Tp> [1..1]  3954
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3931 May 2026
```

## File page 3932

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 3955
Or}         Proprietary <Prtry> [1..1] ± 3956
       Basis <Bsis> [0..1]  3956
{Or         Code <Cd> [1..1] CodeSet 3956
Or}         Proprietary <Prtry> [1..1] ± 3957
       StandardAmount <StdAmt> [0..1] Amount C2, C8 3957
       StandardRate <StdRate> [0..1] Rate 3957
       DiscountDetails <DscntDtls> [0..1]  C15 3958
         Amount <Amt> [0..1] Amount C2, C8 3958
         Rate <Rate> [0..1] Rate 3959
         Basis <Bsis> [0..1]  3959
{Or           Code <Cd> [1..1] CodeSet 3959
Or}           Proprietary <Prtry> [1..1] ± 3959
       AppliedAmount <ApldAmt> [0..1] Amount C2, C8 3960
       AppliedRate <ApldRate> [0..1] Rate 3960
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 3960
       RecipientIdentification <RcptId> [0..1] ± 3960
       InformativeIndicator <InftvInd> [1..1] Indicator 3961
     IndividualTax <IndvTax> [0..*] ± 3961
     DigitalNetworkFee <DgtlNtwkFee> [0..2]  3961
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3962
         ISIN <ISIN> [0..1] IdentifierSet 3964
         OtherIdentification <OthrId> [0..*]  3964
           Identification <Id> [1..1] Text 3964
           Suffix <Sfx> [0..1] Text 3964
           Type <Tp> [1..1]  3964
{Or             Code <Cd> [1..1] CodeSet 3965
Or}             Proprietary <Prtry> [1..1] Text 3966
         Description <Desc> [0..1] Text 3966
       Quantity <Qty> [1..1]  3967
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3932 May 2026
```

## File page 3933

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Quantity <Qty> [1..1] ± C14 3967
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3967
           Quantity <Qty> [1..1] Quantity 3968
           QuantityType <QtyTp> [1..1] Text 3968
           Issuer <Issr> [1..1] Text 3968
           SchemeName <SchmeNm> [0..1] Text 3968
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3968
   InformativeTaxDetails <InftvTaxDtls> [0..1] ± C35 3968
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3970
     SettlementDate <SttlmDt> [0..1] Date 3972
     SettlementPlace <SttlmPlc> [1..1]  3972
       Party <Pty> [1..1]  3973
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3973
Or         ProprietaryIdentification <PrtryId> [1..1] ± 3973
Or         NameAndAddress <NmAndAdr> [1..1] ± 3974
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3974
       LEI <LEI> [0..1] IdentifierSet 3974
     SafekeepingPlace <SfkpgPlc> [0..1] ± 3974
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3975
     TradeTransactionCondition <TradTxCond> [0..*] ± 3975
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3975
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C32,
C33
3976
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3977
         PartyIdentification <PtyId> [1..1] ± 3977
         AccountIdentification <AcctId> [0..1] Text 3977
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3977
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3978
         PartyIdentification <PtyId> [1..1] ± 3978
         AccountIdentification <AcctId> [0..1] Text 3978
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3978
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3933 May 2026
```

## File page 3934

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3979
         PartyIdentification <PtyId> [1..1] ± 3979
         AccountIdentification <AcctId> [0..1] Text 3979
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3979
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3980
         PartyIdentification <PtyId> [1..1] ± 3980
         AccountIdentification <AcctId> [0..1] Text 3980
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3980
     DeliveringSideDetails <DlvrgSdDtls> [1..1]  C10,
C11
3981
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3982
         PartyIdentification <PtyId> [1..1] ± 3982
         AccountIdentification <AcctId> [0..1] Text 3982
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3983
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3983
         PartyIdentification <PtyId> [1..1] ± 3983
         AccountIdentification <AcctId> [0..1] Text 3983
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3983
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3984
         PartyIdentification <PtyId> [1..1] ± 3984
         AccountIdentification <AcctId> [0..1] Text 3984
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3984
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3985
         PartyIdentification <PtyId> [1..1] ± 3985
         AccountIdentification <AcctId> [0..1] Text 3985
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3985
   PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3986
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3986
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3986
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3934 May 2026
```

## File page 3935

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3987
       ISIN <ISIN> [0..1] IdentifierSet 3989
       OtherIdentification <OthrId> [0..*]  3989
         Identification <Id> [1..1] Text 3989
         Suffix <Sfx> [0..1] Text 3989
         Type <Tp> [1..1]  3989
{Or           Code <Cd> [1..1] CodeSet 3990
Or}           Proprietary <Prtry> [1..1] Text 3991
       Description <Desc> [0..1] Text 3991
     Quantity <Qty> [1..1]  3992
{Or       Quantity <Qty> [1..1] ± C14 3992
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3992
         Quantity <Qty> [1..1] Quantity 3993
         QuantityType <QtyTp> [1..1] Text 3993
         Issuer <Issr> [1..1] Text 3993
         SchemeName <SchmeNm> [0..1] Text 3993
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3993
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3993
   Equalisation <Equlstn> [0..1] ± 3993
Constraints
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Following Must be True
    /PhysicalDeliveryDetails Must be absent
• PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'true'
 Or    /PhysicalDeliveryIndicator is equal to value '1'
Following Must be True
    /PhysicalDeliveryDetails Must be present
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3935 May 2026
```

