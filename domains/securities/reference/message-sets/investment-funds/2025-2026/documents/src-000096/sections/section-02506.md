---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [3524, 3525, 3526, 3527, 3528, 3529, 3530, 3531, 3532, 3533]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# Continuation at file page 3524

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3524 to 3533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3524

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DiscountDetails <DscntDtls> [0..1]  C14 3639
           Amount <Amt> [0..1] Amount C2, C7 3639
           Rate <Rate> [0..1] Rate 3640
           Basis <Bsis> [0..1]  3640
{Or             Code <Cd> [1..1] CodeSet 3640
Or}             Proprietary <Prtry> [1..1] ± 3641
         RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3641
         RequestedRate <ReqdRate> [0..1] Rate 3641
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 3642
         RecipientIdentification <RcptId> [0..1] ± 3642
       IndividualTax <IndvTax> [0..*]  3642
         Type <Tp> [1..1]  3643
{Or           Code <Cd> [1..1] CodeSet 3643
Or}           Proprietary <Prtry> [1..1] ± 3645
         Tax <Tax> [0..1]  3645
{Or           Amount <Amt> [1..1] Amount C2, C7 3645
Or}           Rate <Rate> [1..1] Rate 3646
         Country <Ctry> [0..1] CodeSet C6 3646
         ExemptionIndicator <XmptnInd> [1..1] Indicator 3646
         ExemptionReason <XmptnRsn> [0..1]  3646
{Or           Code <Cd> [1..1] CodeSet 3646
Or}           Proprietary <Prtry> [1..1] ± 3649
         RecipientIdentification <RcptId> [0..1] ± 3649
         TaxCalculationDetails <TaxClctnDtls> [0..1]  3650
           Basis <Bsis> [1..1]  3650
{Or             Code <Cd> [1..1] CodeSet 3650
Or}             Proprietary <Prtry> [1..1] ± 3650
       DigitalNetworkFee <DgtlNtwkFee> [0..*]  3651
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3651
           ISIN <ISIN> [0..1] IdentifierSet 3653
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3524 May 2026
```

## File page 3525

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           OtherIdentification <OthrId> [0..*]  3653
             Identification <Id> [1..1] Text 3653
             Suffix <Sfx> [0..1] Text 3653
             Type <Tp> [1..1]  3653
{Or               Code <Cd> [1..1] CodeSet 3654
Or}               Proprietary <Prtry> [1..1] Text 3655
           Description <Desc> [0..1] Text 3655
         Quantity <Qty> [1..1]  3656
{Or           Quantity <Qty> [1..1] ± C13 3656
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3656
             Quantity <Qty> [1..1] Quantity 3657
             QuantityType <QtyTp> [1..1] Text 3657
             Issuer <Issr> [1..1] Text 3657
             SchemeName <SchmeNm> [0..1] Text 3657
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3657
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3657
       SettlementDate <SttlmDt> [0..1] Date 3659
       SettlementPlace <SttlmPlc> [1..1]  3659
         Party <Pty> [1..1]  3660
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3660
Or           ProprietaryIdentification <PrtryId> [1..1] ± 3660
Or           NameAndAddress <NmAndAdr> [1..1] ± 3661
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3661
         LEI <LEI> [0..1] IdentifierSet 3661
       SafekeepingPlace <SfkpgPlc> [0..1] ± 3661
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3662
       TradeTransactionCondition <TradTxCond> [0..*] ± 3662
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3662
       ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
3663
         ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3664
           PartyIdentification <PtyId> [1..1] ± 3664
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3525 May 2026
```

## File page 3526

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AccountIdentification <AcctId> [0..1] Text 3664
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3664
         ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3665
           PartyIdentification <PtyId> [1..1] ± 3665
           AccountIdentification <AcctId> [0..1] Text 3665
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3665
         ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3666
           PartyIdentification <PtyId> [1..1] ± 3666
           AccountIdentification <AcctId> [0..1] Text 3666
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3666
         ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3667
           PartyIdentification <PtyId> [1..1] ± 3667
           AccountIdentification <AcctId> [0..1] Text 3667
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3667
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C9, C10 3668
         DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3669
           PartyIdentification <PtyId> [1..1] ± 3669
           AccountIdentification <AcctId> [0..1] Text 3669
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3670
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3670
           PartyIdentification <PtyId> [1..1] ± 3670
           AccountIdentification <AcctId> [0..1] Text 3670
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3670
         DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3671
           PartyIdentification <PtyId> [1..1] ± 3671
           AccountIdentification <AcctId> [0..1] Text 3671
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3671
         DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3672
           PartyIdentification <PtyId> [1..1] ± 3672
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3526 May 2026
```

## File page 3527

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AccountIdentification <AcctId> [0..1] Text 3672
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3672
     PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3673
     PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3673
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3673
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3674
         ISIN <ISIN> [0..1] IdentifierSet 3676
         OtherIdentification <OthrId> [0..*]  3676
           Identification <Id> [1..1] Text 3676
           Suffix <Sfx> [0..1] Text 3676
           Type <Tp> [1..1]  3676
{Or             Code <Cd> [1..1] CodeSet 3677
Or}             Proprietary <Prtry> [1..1] Text 3678
         Description <Desc> [0..1] Text 3678
       Quantity <Qty> [1..1]  3679
{Or         Quantity <Qty> [1..1] ± C13 3679
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3679
           Quantity <Qty> [1..1] Quantity 3680
           QuantityType <QtyTp> [1..1] Text 3680
           Issuer <Issr> [1..1] Text 3680
           SchemeName <SchmeNm> [0..1] Text 3680
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3680
     NonStandardSettlementInformation
<NonStdSttlmInf>
[0..1] Text 3680
     Equalisation <Equlstn> [0..1] ± 3680
   CashSettlementDetails <CshSttlmDtls> [0..1]  3681
     CashInOrOut <CshInOrOut> [1..1]  3689
{Or       CashInPaymentInstrument <CshInPmtInstrm> [1..1]  3697
{Or         PaymentCardDetails <PmtCardDtls> [1..1]  3702
           Type <Tp> [1..1] CodeSet 3703
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3527 May 2026
```

## File page 3528

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Number <Nb> [1..1] Text 3703
           HolderName <HldrNm> [1..1] Text 3703
           StartDate <StartDt> [0..1] YearMonth 3703
           ExpiryDate <XpryDt> [1..1] YearMonth 3703
           CardIssuerName <CardIssrNm> [0..1] Text 3703
           CardIssuerIdentification <CardIssrId> [0..1] ± 3703
           SecurityCode <SctyCd> [0..1] Text 3704
           SequenceNumber <SeqNb> [0..1] Text 3704
Or         CreditTransferDetails <CdtTrfDtls> [1..1]  3704
           Reference <Ref> [0..1] Text 3707
           Debtor <Dbtr> [0..1] ± 3707
           DebtorAccount <DbtrAcct> [0..1]  3707
             Identification <Id> [1..1]  3707
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3708
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3708
Or}               Other <Othr> [1..1] ± 3708
             Name <Nm> [0..1] Text 3709
           DebtorAgent <DbtrAgt> [0..1]  3709
             Party <Pty> [1..1]  3709
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3710
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3710
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3710
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3711
             LEI <LEI> [0..1] IdentifierSet 3711
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  3712
             Identification <Id> [1..1]  3712
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Or}               Other <Othr> [1..1] ± 3713
             Name <Nm> [0..1] Text 3713
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  3713
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3528 May 2026
```

## File page 3529

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Party <Pty> [1..1]  3714
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3714
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3714
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3715
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3716
             LEI <LEI> [0..1] IdentifierSet 3716
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3717
             Identification <Id> [1..1]  3717
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3717
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3718
Or}               Other <Othr> [1..1] ± 3718
             Name <Nm> [0..1] Text 3718
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  3718
             Party <Pty> [1..1]  3719
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3719
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3719
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3720
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3721
             LEI <LEI> [0..1] IdentifierSet 3721
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3722
             Identification <Id> [1..1]  3722
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3722
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3723
Or}               Other <Othr> [1..1] ± 3723
             Name <Nm> [0..1] Text 3723
           CreditorAgent <CdtrAgt> [1..1]  3723
             Party <Pty> [1..1]  3724
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3724
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3724
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3725
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3529 May 2026
```

## File page 3530

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3726
             LEI <LEI> [0..1] IdentifierSet 3726
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  3727
             Identification <Id> [1..1]  3727
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3727
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3728
Or}               Other <Othr> [1..1] ± 3728
             Name <Nm> [0..1] Text 3728
           Creditor <Cdtr> [0..1] ± 3728
           CreditorAccount <CdtrAcct> [1..1]  3729
             Identification <Id> [1..1]  3729
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3729
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3730
Or}               Other <Othr> [1..1] ± 3730
             Name <Nm> [0..1] Text 3730
Or         DirectDebitDetails <DrctDbtDtls> [1..1]  3730
           DebtorAccount <DbtrAcct> [1..1]  3731
             Identification <Id> [1..1]  3732
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3732
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3732
Or}               Other <Othr> [1..1] ± 3733
             Name <Nm> [0..1] Text 3733
           Debtor <Dbtr> [0..1] ± 3733
           DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3733
           DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3734
           Creditor <Cdtr> [0..1] ± 3734
           DebtorAgent <DbtrAgt> [1..1]  3734
             Party <Pty> [1..1]  3734
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3735
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3735
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3735
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3530 May 2026
```

## File page 3531

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3736
             LEI <LEI> [0..1] IdentifierSet 3736
           DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3737
           CreditorAgent <CdtrAgt> [0..1]  3737
             Party <Pty> [1..1]  3737
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3738
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3738
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3738
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3739
             LEI <LEI> [0..1] IdentifierSet 3739
           CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3740
           RegistrationIdentification <RegnId> [0..1] Text 3740
           MandateIdentification <MndtId> [0..1] Text 3740
Or         ChequeDetails <ChqDtls> [1..1]  3740
           Number <Nb> [0..1] Text 3741
           PayeeIdentification <PyeeId> [1..1] ± 3741
           DraweeIdentification <DrweeId> [0..1]  3741
             Party <Pty> [1..1]  3742
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3742
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3742
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3743
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3744
             LEI <LEI> [0..1] IdentifierSet 3744
           DrawerIdentification <DrwrId> [0..1] ± 3745
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  3745
           Number <Nb> [0..1] Text 3745
           PayeeIdentification <PyeeId> [1..1] ± 3745
           DraweeIdentification <DrweeId> [0..1]  3746
             Party <Pty> [1..1]  3746
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3746
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3747
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3531 May 2026
```

## File page 3532

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3747
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3748
             LEI <LEI> [0..1] IdentifierSet 3748
           DrawerIdentification <DrwrId> [0..1] ± 3749
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 3749
           AccountIdentification <AcctId> [0..1] Text 3749
           Type <Tp> [0..1] ± 3749
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  3750
           Identification <Id> [1..1] Text 3750
           Type <Tp> [0..1] ± 3750
           Name <Nm> [0..1] Text 3750
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3751
Or}       CashOutPaymentInstrument <CshOutPmtInstrm> [1..1]  3751
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  3755
           Reference <Ref> [0..1] Text 3758
           Debtor <Dbtr> [0..1] ± 3758
           DebtorAccount <DbtrAcct> [0..1]  3758
             Identification <Id> [1..1]  3758
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3759
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3759
Or}               Other <Othr> [1..1] ± 3759
             Name <Nm> [0..1] Text 3760
           DebtorAgent <DbtrAgt> [0..1]  3760
             Party <Pty> [1..1]  3760
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3761
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3761
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3761
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3762
             LEI <LEI> [0..1] IdentifierSet 3762
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  3763
             Identification <Id> [1..1]  3763
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3532 May 2026
```

## File page 3533

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3763
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3764
Or}               Other <Othr> [1..1] ± 3764
             Name <Nm> [0..1] Text 3764
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  3764
             Party <Pty> [1..1]  3765
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3765
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3765
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3766
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3767
             LEI <LEI> [0..1] IdentifierSet 3767
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3768
             Identification <Id> [1..1]  3768
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3768
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3769
Or}               Other <Othr> [1..1] ± 3769
             Name <Nm> [0..1] Text 3769
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  3769
             Party <Pty> [1..1]  3770
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3770
Or               BICFI <BICFI> [1..1] IdentifierSet C5 3770
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3771
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3772
             LEI <LEI> [0..1] IdentifierSet 3772
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3773
             Identification <Id> [1..1]  3773
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 3773
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3774
Or}               Other <Othr> [1..1] ± 3774
             Name <Nm> [0..1] Text 3774
           CreditorAgent <CdtrAgt> [1..1]  3774
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3533 May 2026
```

