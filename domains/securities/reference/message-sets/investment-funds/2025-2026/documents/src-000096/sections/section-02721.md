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
file_pages: [3813, 3814, 3815, 3816, 3817, 3818, 3819, 3820, 3821, 3822]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# Continuation at file page 3813

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3813 to 3822.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3813

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or                 Code <Cd> [1..1] CodeSet 3965
Or}                 Proprietary <Prtry> [1..1] Text 3966
             Description <Desc> [0..1] Text 3966
           Quantity <Qty> [1..1]  3967
{Or             Quantity <Qty> [1..1] ± C14 3967
Or}             ProprietaryQuantity <PrtryQty> [1..1]  3967
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
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3973
Or             ProprietaryIdentification <PrtryId> [1..1] ± 3973
Or             NameAndAddress <NmAndAdr> [1..1] ± 3974
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3813 May 2026
```

## File page 3814

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3974
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
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3977
           ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3978
             PartyIdentification <PtyId> [1..1] ± 3978
             AccountIdentification <AcctId> [0..1] Text 3978
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3978
           ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3979
             PartyIdentification <PtyId> [1..1] ± 3979
             AccountIdentification <AcctId> [0..1] Text 3979
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3979
           ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3980
             PartyIdentification <PtyId> [1..1] ± 3980
             AccountIdentification <AcctId> [0..1] Text 3980
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3980
         DeliveringSideDetails <DlvrgSdDtls> [1..1]  C10,
C11
3981
           DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3982
             PartyIdentification <PtyId> [1..1] ± 3982
             AccountIdentification <AcctId> [0..1] Text 3982
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3983
           DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3983
             PartyIdentification <PtyId> [1..1] ± 3983
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3814 May 2026
```

## File page 3815

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             AccountIdentification <AcctId> [0..1] Text 3983
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3983
           DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3984
             PartyIdentification <PtyId> [1..1] ± 3984
             AccountIdentification <AcctId> [0..1] Text 3984
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3984
           DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3985
             PartyIdentification <PtyId> [1..1] ± 3985
             AccountIdentification <AcctId> [0..1] Text 3985
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3985
       PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3986
       PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3986
       DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3986
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
{Or               Code <Cd> [1..1] CodeSet 3990
Or}               Proprietary <Prtry> [1..1] Text 3991
           Description <Desc> [0..1] Text 3991
         Quantity <Qty> [1..1]  3992
{Or           Quantity <Qty> [1..1] ± C14 3992
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3992
             Quantity <Qty> [1..1] Quantity 3993
             QuantityType <QtyTp> [1..1] Text 3993
             Issuer <Issr> [1..1] Text 3993
             SchemeName <SchmeNm> [0..1] Text 3993
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3993
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3815 May 2026
```

## File page 3816

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3993
       Equalisation <Equlstn> [0..1] ± 3993
     CashSettlementDetails <CshSttlmDtls> [0..1]  3994
       CashInOrOut <CshInOrOut> [1..1]  4002
{Or         CashInPaymentInstrument <CshInPmtInstrm> [1..1]  4010
{Or           PaymentCardDetails <PmtCardDtls> [1..1]  4015
             Type <Tp> [1..1] CodeSet 4016
             Number <Nb> [1..1] Text 4016
             HolderName <HldrNm> [1..1] Text 4016
             StartDate <StartDt> [0..1] YearMonth 4016
             ExpiryDate <XpryDt> [1..1] YearMonth 4016
             CardIssuerName <CardIssrNm> [0..1] Text 4016
             CardIssuerIdentification <CardIssrId> [0..1] ± 4016
             SecurityCode <SctyCd> [0..1] Text 4017
             SequenceNumber <SeqNb> [0..1] Text 4017
Or           CreditTransferDetails <CdtTrfDtls> [1..1]  4017
             Reference <Ref> [0..1] Text 4020
             Debtor <Dbtr> [0..1] ± 4020
             DebtorAccount <DbtrAcct> [0..1]  4020
               Identification <Id> [1..1]  4020
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4021
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4021
Or}                 Other <Othr> [1..1] ± 4021
               Name <Nm> [0..1] Text 4022
             DebtorAgent <DbtrAgt> [0..1]  4022
               Party <Pty> [1..1]  4022
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4023
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4023
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4023
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4024
               LEI <LEI> [0..1] IdentifierSet 4024
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3816 May 2026
```

## File page 3817

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             DebtorAgentAccount <DbtrAgtAcct> [0..1]  4025
               Identification <Id> [1..1]  4025
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4025
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4026
Or}                 Other <Othr> [1..1] ± 4026
               Name <Nm> [0..1] Text 4026
             IntermediaryAgent1 <IntrmyAgt1> [0..1]  4026
               Party <Pty> [1..1]  4027
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4027
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4027
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4028
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4029
               LEI <LEI> [0..1] IdentifierSet 4029
             IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4030
               Identification <Id> [1..1]  4030
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4030
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4031
Or}                 Other <Othr> [1..1] ± 4031
               Name <Nm> [0..1] Text 4031
             IntermediaryAgent2 <IntrmyAgt2> [0..1]  4031
               Party <Pty> [1..1]  4032
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4032
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4033
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4034
               LEI <LEI> [0..1] IdentifierSet 4034
             IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4035
               Identification <Id> [1..1]  4035
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4035
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4036
Or}                 Other <Othr> [1..1] ± 4036
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3817 May 2026
```

## File page 3818

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Name <Nm> [0..1] Text 4036
             CreditorAgent <CdtrAgt> [1..1]  4036
               Party <Pty> [1..1]  4037
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4037
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4037
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4038
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4039
               LEI <LEI> [0..1] IdentifierSet 4039
             CreditorAgentAccount <CdtrAgtAcct> [0..1]  4040
               Identification <Id> [1..1]  4040
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4040
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4041
Or}                 Other <Othr> [1..1] ± 4041
               Name <Nm> [0..1] Text 4041
             Creditor <Cdtr> [0..1] ± 4041
             CreditorAccount <CdtrAcct> [1..1]  4042
               Identification <Id> [1..1]  4042
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4042
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4043
Or}                 Other <Othr> [1..1] ± 4043
               Name <Nm> [0..1] Text 4043
Or           DirectDebitDetails <DrctDbtDtls> [1..1]  4043
             DebtorAccount <DbtrAcct> [1..1]  4044
               Identification <Id> [1..1]  4045
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4045
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4045
Or}                 Other <Othr> [1..1] ± 4046
               Name <Nm> [0..1] Text 4046
             Debtor <Dbtr> [0..1] ± 4046
             DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4046
             DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 4047
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3818 May 2026
```

## File page 3819

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Creditor <Cdtr> [0..1] ± 4047
             DebtorAgent <DbtrAgt> [1..1]  4047
               Party <Pty> [1..1]  4047
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4048
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4048
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4049
               LEI <LEI> [0..1] IdentifierSet 4049
             DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4050
             CreditorAgent <CdtrAgt> [0..1]  4050
               Party <Pty> [1..1]  4050
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4051
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4051
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4051
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4052
               LEI <LEI> [0..1] IdentifierSet 4052
             CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4053
             RegistrationIdentification <RegnId> [0..1] Text 4053
             MandateIdentification <MndtId> [0..1] Text 4053
Or           ChequeDetails <ChqDtls> [1..1]  4053
             Number <Nb> [0..1] Text 4054
             PayeeIdentification <PyeeId> [1..1] ± 4054
             DraweeIdentification <DrweeId> [0..1]  4054
               Party <Pty> [1..1]  4055
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4055
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4055
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4056
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4057
               LEI <LEI> [0..1] IdentifierSet 4057
             DrawerIdentification <DrwrId> [0..1] ± 4058
Or           BankersDraftDetails <BkrsDrftDtls> [1..1]  4058
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3819 May 2026
```

## File page 3820

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Number <Nb> [0..1] Text 4058
             PayeeIdentification <PyeeId> [1..1] ± 4058
             DraweeIdentification <DrweeId> [0..1]  4059
               Party <Pty> [1..1]  4059
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4059
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4060
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4060
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4061
               LEI <LEI> [0..1] IdentifierSet 4061
             DrawerIdentification <DrwrId> [0..1] ± 4062
Or           CashAccountDetails <CshAcctDtls> [1..1]  C1 4062
             AccountIdentification <AcctId> [0..1] Text 4062
             Type <Tp> [0..1] ± 4062
Or}           BlockChainCashWallet <BlckChainCshWllt> [1..1]  4063
             Identification <Id> [1..1] Text 4063
             Type <Tp> [0..1] ± 4063
             Name <Nm> [0..1] Text 4063
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4064
Or}         CashOutPaymentInstrument <CshOutPmtInstrm> [1..1]  4064
{Or           CreditTransferDetails <CdtTrfDtls> [1..1]  4068
             Reference <Ref> [0..1] Text 4071
             Debtor <Dbtr> [0..1] ± 4071
             DebtorAccount <DbtrAcct> [0..1]  4071
               Identification <Id> [1..1]  4071
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4072
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4072
Or}                 Other <Othr> [1..1] ± 4072
               Name <Nm> [0..1] Text 4073
             DebtorAgent <DbtrAgt> [0..1]  4073
               Party <Pty> [1..1]  4073
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4074
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3820 May 2026
```

## File page 3821

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4074
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4074
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4075
               LEI <LEI> [0..1] IdentifierSet 4075
             DebtorAgentAccount <DbtrAgtAcct> [0..1]  4076
               Identification <Id> [1..1]  4076
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4076
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4077
Or}                 Other <Othr> [1..1] ± 4077
               Name <Nm> [0..1] Text 4077
             IntermediaryAgent1 <IntrmyAgt1> [0..1]  4077
               Party <Pty> [1..1]  4078
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4078
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4078
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4079
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4080
               LEI <LEI> [0..1] IdentifierSet 4080
             IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4081
               Identification <Id> [1..1]  4081
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4081
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4082
Or}                 Other <Othr> [1..1] ± 4082
               Name <Nm> [0..1] Text 4082
             IntermediaryAgent2 <IntrmyAgt2> [0..1]  4082
               Party <Pty> [1..1]  4083
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4083
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4083
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4084
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4085
               LEI <LEI> [0..1] IdentifierSet 4085
             IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4086
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3821 May 2026
```

## File page 3822

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Identification <Id> [1..1]  4086
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4086
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4087
Or}                 Other <Othr> [1..1] ± 4087
               Name <Nm> [0..1] Text 4087
             CreditorAgent <CdtrAgt> [1..1]  4087
               Party <Pty> [1..1]  4088
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4088
Or                 BICFI <BICFI> [1..1] IdentifierSet C6 4088
Or                 ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4089
Or}                 ProprietaryIdentification <PrtryId> [1..1] Text 4090
               LEI <LEI> [0..1] IdentifierSet 4090
             CreditorAgentAccount <CdtrAgtAcct> [0..1]  4091
               Identification <Id> [1..1]  4091
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4091
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4092
Or}                 Other <Othr> [1..1] ± 4092
               Name <Nm> [0..1] Text 4092
             Creditor <Cdtr> [0..1] ± 4092
             CreditorAccount <CdtrAcct> [1..1]  4093
               Identification <Id> [1..1]  4093
{Or                 IBAN <IBAN> [1..1] IdentifierSet C17 4093
Or                 BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4094
Or}                 Other <Othr> [1..1] ± 4094
               Name <Nm> [0..1] Text 4094
Or           ChequeDetails <ChqDtls> [1..1]  4094
             Number <Nb> [0..1] Text 4095
             PayeeIdentification <PyeeId> [1..1] ± 4095
             DraweeIdentification <DrweeId> [0..1]  4095
               Party <Pty> [1..1]  4096
{Or                 NameAndAddress <NmAndAdr> [1..1] ± 4096
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3822 May 2026
```

