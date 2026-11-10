---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.2 Structure"]
file_pages: [817, 818, 819, 820, 821, 822, 823, 824, 825]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 817 to 825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 817

```text
34.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfInstrStsRpt> [1..1]  C24,
C26
   MessageIdentification <MsgId> [1..1] ± 0
   CounterpartyReference <CtrPtyRef> [0..1] ± 0
   Reference <Ref> [0..1] ± 829
   StatusReport <StsRpt> [1..1]  C7, C28,
C29
829
     MasterReference <MstrRef> [0..1] Text 840
     TransferReference <TrfRef> [1..1] ± 841
     ClientReference <ClntRef> [0..1] ± 841
     CancellationReference <CxlRef> [0..1] Text 841
     TransferEventType <TrfEvtTp> [0..*]  841
{Or       Code <Cd> [1..1] CodeSet 841
Or}       Proprietary <Prtry> [1..1] ± 842
     TransferStatus <TrfSts> [1..1]  842
{Or       Status <Sts> [1..1] ± 843
Or       PendingSettlement <PdgSttlm> [1..1] ± 843
Or       Unmatched <Umtchd> [1..1] ± 844
Or       InRepair <InRpr> [1..1] ± 844
Or       Rejected <Rjctd> [1..10]  C25 844
         Reason <Rsn> [1..1]  845
{Or           Code <Cd> [1..1] CodeSet 845
Or}           Proprietary <Prtry> [1..1] ± 847
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 848
Or       FailedSettlement <FaildSttlm> [1..1] ± 848
Or       Cancelled <Canc> [1..1] ± 848
Or       Reversed <Rvsd> [1..1] ± 848
Or}       CancellationPending <CxlPdg> [1..1] ± 849
     Instrument <Instrm> [0..1]  849
{Or       Security <Scty> [1..1]  C18 850
         Identification <Id> [1..1]  851
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 817 May 2026
```

## File page 818

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           ISIN <ISIN> [1..1] IdentifierSet 852
Or           SEDOL <SEDOL> [1..1] IdentifierSet 852
Or           CUSIP <CUSIP> [1..1] IdentifierSet 853
Or           RIC <RIC> [1..1] IdentifierSet 853
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 853
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 853
Or           CTA <CTA> [1..1] IdentifierSet 853
Or           QUICK <QUICK> [1..1] IdentifierSet 853
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 853
Or           Dutch <Dtch> [1..1] IdentifierSet 854
Or           Valoren <Vlrn> [1..1] IdentifierSet 854
Or           Sicovam <SCVM> [1..1] IdentifierSet 854
Or           Belgian <Belgn> [1..1] IdentifierSet 854
Or           Common <Cmon> [1..1] IdentifierSet 854
Or           DTI <DTI> [1..1] IdentifierSet 854
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  854
             Identification <Id> [1..1] Text 855
             IdentificationSource <IdSrc> [1..1] ± 855
         Name <Nm> [0..1] Text 855
         ShortName <ShrtNm> [0..1] Text 855
         ClassificationType <ClssfctnTp> [0..1] ± 855
Or       CashAsset <CshAsst> [1..1] ± C16 855
Or}       OtherAsset <OthrAsst> [1..1] ± 856
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  856
       OwnerIdentification <OwnrId> [0..1] ± 857
       AccountIdentification <AcctId> [0..1] Text 857
       AccountDesignation <AcctDsgnt> [0..1] Text 857
       AccountName <AcctNm> [0..1] Text 858
       Type <Tp> [0..1] ± 858
       Servicer <Svcr> [0..1] ± 858
       SubAccountDetails <SubAcctDtls> [0..1] ± 858
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 818 May 2026
```

## File page 819

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 859
     IntermediaryInformation <IntrmyInf> [0..*] ± 859
     TradeDate <TradDt> [0..1] Date 859
     SettlementDate <SttlmDt> [0..1] Date 860
     SendOutDate <SndOutDt> [0..1] Date 860
     CashSettlementDate <CshSttlmDt> [0..1] Date 860
     TotalUnitsNumber <TtlUnitsNb> [0..1] Quantity 860
     AveragePrice <AvrgPric> [0..1] Amount C2 860
     UnitsDetails <UnitsDtls> [0..*]  860
       Units <Units> [1..1]  863
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 863
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 863
       OrderDate <OrdrDt> [0..1] Date 863
       AcquisitionDate <AcqstnDt> [0..1] Date 863
       CertificateNumber <CertNb> [0..*] Text 863
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 863
       Reference <Ref> [0..1] Text 864
       PriceDetails <PricDtls> [0..1] ± 864
       TransactionOverhead <TxOvrhd> [0..1]  C22,
C27
864
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 866
         TotalFees <TtlFees> [0..1] Amount C1, C10 867
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 867
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 867
         IndividualFee <IndvFee> [0..*]  C4 868
           Type <Tp> [1..1]  868
{Or             Code <Cd> [1..1] CodeSet 869
Or}             Proprietary <Prtry> [1..1] ± 870
           Basis <Bsis> [0..1]  870
{Or             Code <Cd> [1..1] CodeSet 870
Or}             Proprietary <Prtry> [1..1] ± 871
           StandardAmount <StdAmt> [0..1] Amount C1, C10 871
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 819 May 2026
```

## File page 820

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           StandardRate <StdRate> [0..1] Rate 871
           DiscountDetails <DscntDtls> [0..1]  C14 872
             Amount <Amt> [0..1] Amount C1, C10 872
             Rate <Rate> [0..1] Rate 873
             Basis <Bsis> [0..1]  873
{Or               Code <Cd> [1..1] CodeSet 873
Or}               Proprietary <Prtry> [1..1] ± 873
           AppliedAmount <ApldAmt> [0..1] Amount C1, C10 874
           AppliedRate <ApldRate> [0..1] Rate 874
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 874
           RecipientIdentification <RcptId> [0..1] ± 874
           InformativeIndicator <InftvInd> [1..1] Indicator 875
         IndividualTax <IndvTax> [0..*] ± 875
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  875
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C20,
C21,
C23
876
             ISIN <ISIN> [0..1] IdentifierSet 878
             OtherIdentification <OthrId> [0..*]  878
               Identification <Id> [1..1] Text 878
               Suffix <Sfx> [0..1] Text 878
               Type <Tp> [1..1]  878
{Or                 Code <Cd> [1..1] CodeSet 879
Or}                 Proprietary <Prtry> [1..1] Text 880
             Description <Desc> [0..1] Text 880
           Quantity <Qty> [1..1]  881
{Or             Quantity <Qty> [1..1] ± C13 881
Or}             ProprietaryQuantity <PrtryQty> [1..1]  881
               Quantity <Qty> [1..1] Quantity 882
               QuantityType <QtyTp> [1..1] Text 882
               Issuer <Issr> [1..1] Text 882
               SchemeName <SchmeNm> [0..1] Text 882
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 820 May 2026
```

## File page 821

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 882
       OtherAmount <OthrAmt> [0..*]  882
         Type <Tp> [1..1]  883
{Or           Code <Cd> [1..1] CodeSet 883
Or}           ProprietaryCode <PrtryCd> [1..1] ± 883
         Amount <Amt> [1..1] Amount C1, C10 883
     Conversion <Convs> [0..1]  884
       SourceSecurity <SrcScty> [1..1]  C19 886
         Identification <Id> [1..1]  887
{Or           ISIN <ISIN> [1..1] IdentifierSet 887
Or           SEDOL <SEDOL> [1..1] IdentifierSet 888
Or           CUSIP <CUSIP> [1..1] IdentifierSet 888
Or           RIC <RIC> [1..1] IdentifierSet 888
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 888
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 888
Or           CTA <CTA> [1..1] IdentifierSet 888
Or           QUICK <QUICK> [1..1] IdentifierSet 888
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 889
Or           Dutch <Dtch> [1..1] IdentifierSet 889
Or           Valoren <Vlrn> [1..1] IdentifierSet 889
Or           Sicovam <SCVM> [1..1] IdentifierSet 889
Or           Belgian <Belgn> [1..1] IdentifierSet 889
Or           Common <Cmon> [1..1] IdentifierSet 889
Or           DTI <DTI> [1..1] IdentifierSet 889
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  889
             Identification <Id> [1..1] Text 890
             IdentificationSource <IdSrc> [1..1] ± 890
         Name <Nm> [0..1] Text 890
         ShortName <ShrtNm> [0..1] Text 890
       TotalUnitsNumber <TtlUnitsNb> [0..1] Quantity 890
       UnitsDetails <UnitsDtls> [0..*]  890
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 821 May 2026
```

## File page 822

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Units <Units> [1..1]  891
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 891
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 891
         OrderDate <OrdrDt> [0..1] Date 891
         AcquisitionDate <AcqstnDt> [0..1] Date 891
         CertificateNumber <CertNb> [0..*] Text 892
         Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 892
         Reference <Ref> [0..1] Text 892
       AdditionalInformation <AddtlInf> [0..*] ± 892
     TotalTransferValue <TtlTrfVal> [0..1] Amount C1 892
     PaymentDetails <PmtDtls> [0..*]  893
       Reference <Ref> [0..1] Text 896
       Amount <Amt> [1..1] Amount C1 896
       PaymentDate <PmtDt> [0..1] Date 897
       CashSettlementDetails <CshSttlmDtls> [0..1]  897
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  900
           Debtor <Dbtr> [0..1] ± 903
           DebtorAccount <DbtrAcct> [0..1]  903
             Name <Nm> [0..1] Text 903
             IBAN <IBAN> [0..1] IdentifierSet C17 903
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 904
             Other <Othr> [0..1] ± 904
           DebtorAgent <DbtrAgt> [0..1]  904
             BICFI <BICFI> [0..1] IdentifierSet C6 905
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 905
             NameAndAddress <NmAndAdr> [0..1] ± 906
             LEI <LEI> [0..1] IdentifierSet 906
             ProprietaryIdentification <PrtryId> [0..1] Text 907
             BranchIdentification <BrnchId> [0..1] ± 907
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  907
             Name <Nm> [0..1] Text 907
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 822 May 2026
```

## File page 823

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             IBAN <IBAN> [0..1] IdentifierSet C17 907
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 908
             Other <Othr> [0..1] ± 908
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  908
             BICFI <BICFI> [0..1] IdentifierSet C6 909
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 909
             NameAndAddress <NmAndAdr> [0..1] ± 910
             LEI <LEI> [0..1] IdentifierSet 910
             ProprietaryIdentification <PrtryId> [0..1] Text 911
             BranchIdentification <BrnchId> [0..1] ± 911
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  911
             Name <Nm> [0..1] Text 911
             IBAN <IBAN> [0..1] IdentifierSet C17 911
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 912
             Other <Othr> [0..1] ± 912
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  912
             BICFI <BICFI> [0..1] IdentifierSet C6 913
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 913
             NameAndAddress <NmAndAdr> [0..1] ± 914
             LEI <LEI> [0..1] IdentifierSet 914
             ProprietaryIdentification <PrtryId> [0..1] Text 915
             BranchIdentification <BrnchId> [0..1] ± 915
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  915
             Name <Nm> [0..1] Text 915
             IBAN <IBAN> [0..1] IdentifierSet C17 915
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 916
             Other <Othr> [0..1] ± 916
           CreditorAgent <CdtrAgt> [1..1]  916
             BICFI <BICFI> [0..1] IdentifierSet C6 917
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 917
             NameAndAddress <NmAndAdr> [0..1] ± 918
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 823 May 2026
```

## File page 824

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             LEI <LEI> [0..1] IdentifierSet 918
             ProprietaryIdentification <PrtryId> [0..1] Text 919
             BranchIdentification <BrnchId> [0..1] ± 919
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  919
             Name <Nm> [0..1] Text 919
             IBAN <IBAN> [0..1] IdentifierSet C17 919
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 920
             Other <Othr> [0..1] ± 920
           Creditor <Cdtr> [0..1] ± 920
           CreditorAccount <CdtrAcct> [1..1]  921
             Name <Nm> [0..1] Text 921
             IBAN <IBAN> [0..1] IdentifierSet C17 921
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 922
             Other <Othr> [0..1] ± 922
Or}         ChequeDetails <ChqDtls> [1..1]  922
           Number <Nb> [0..1] Text 923
           PayeeIdentification <PyeeId> [0..1] ± 923
           DraweeIdentification <DrweeId> [0..1]  923
             Party <Pty> [1..1]  924
{Or               NameAndAddress <NmAndAdr> [1..1] ± 924
Or               BICFI <BICFI> [1..1] IdentifierSet C6 924
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 925
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 926
             LEI <LEI> [0..1] IdentifierSet 926
           DrawerIdentification <DrwrId> [0..1] ± 927
     BenefitCrystallisationEvent <BnftCrstllstnEvt> [0..*] ± 927
     DrawdownTranche <DrwdwnTrch> [0..*]  C5 927
       Identification <Id> [0..1] Text 929
       TrancheType <TrchTp> [1..1] ± 929
       ApplicableRules <AplblRules> [0..1]  929
{Or         Code <Cd> [1..1] CodeSet 930
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 824 May 2026
```

## File page 825

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 930
       InvestorTaxReference <InvstrTaxRef> [0..1]  930
         Type <Tp> [0..1]  930
{Or           Code <Cd> [1..1] CodeSet 931
Or}           Proprietary <Prtry> [1..1] ± 931
         Reference <Ref> [1..1] Text 931
       PercentageOfTotalTransferValue <PctgOfTtlTrfVal> [0..1] Rate 931
       TotalAmountNetDrawdown <TtlAmtNetDrwdwn> [0..1] Amount C1 931
       AdditionalFundsDesignated <AddtlFndsDsgntd> [0..1] Indicator 932
       PensionCommencementLumpSumRemaining
<PnsnCmcmntLumpSumRmng>
[0..1] Amount C1 932
       PensionCommencementLumpSumDate
<PnsnCmcmntLumpSumDt>
[0..1] Date 932
       MultiplePensionCommencementLumpSums
<MltplPnsnCmcmntLumpSums>
[0..1] Indicator 932
       LifetimeAllowance <LftmAllwnc> [0..1] Rate 933
       RecipientOfDrawdownIndicator <RcptOfDrwdwnInd> [0..1] Indicator 933
       BeneficiaryDetails <BnfcryDtls> [0..1]  933
         BeneficiaryType <BnfcryTp> [0..1]  933
{Or           Code <Cd> [1..1] CodeSet 933
Or}           Proprietary <Prtry> [1..1] ± 934
         DeathUnderLimit <DthUdrLmt> [0..1] Indicator 934
         DateOfDeath <DtOfDth> [0..1] Date 934
         DateDesignatedToBeneficiary <DtDsgntdToBnfcry> [0..1] Date 934
         AdditionalInformation <AddtlInf> [0..*] ± 934
       CappedLimits <CapdLmts> [0..1]  935
         StartDate <StartDt> [0..1] Date 935
         IncomeLimitCurrentPeriod <IncmLmtCurPrd> [0..1] Amount C1 935
         IncomeCurrentPeriod <IncmCurPrd> [0..1] Amount C1 935
         IncomeLimitNextPeriod <IncmLmtNxtPrd> [0..1] Amount C1 936
         AdditionalInformation <AddtlInf> [0..*] ± 936
       FlexibleDrawdownTriggeredDate <FlxblDrwdwnTrggrdDt> [0..1] Date 936
       TrancheDate <TrchDt> [0..1] Date 936
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 825 May 2026
```

