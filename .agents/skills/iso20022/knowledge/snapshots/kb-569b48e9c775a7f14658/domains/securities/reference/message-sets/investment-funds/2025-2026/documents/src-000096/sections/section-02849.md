---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>"]
file_pages: [4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1 CashInOrOut <CshInOrOut>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4002 to 4009.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4002

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4096
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4097
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4098
           LEI <LEI> [0..1] IdentifierSet 4098
         DrawerIdentification <DrwrId> [0..1] ± 4099
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  4099
         Number <Nb> [0..1] Text 4099
         PayeeIdentification <PyeeId> [1..1] ± 4099
         DraweeIdentification <DrweeId> [0..1]  4100
           Party <Pty> [1..1]  4100
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4100
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4101
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4101
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4102
           LEI <LEI> [0..1] IdentifierSet 4102
         DrawerIdentification <DrwrId> [0..1] ± 4103
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 4103
         AccountIdentification <AcctId> [0..1] Text 4103
         Type <Tp> [0..1] ± 4103
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  4104
         Identification <Id> [1..1] Text 4104
         Type <Tp> [0..1] ± 4104
         Name <Nm> [0..1] Text 4104
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4105
55.4.5.21.1  CashInOrOut <CshInOrOut>
Presence: [1..1]
Definition: Choice between cash-in or cash-out.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4002 May 2026
```

## File page 4003

```text
CashInOrOut <CshInOrOut> contains one of the following CashInOrOut8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CashInPaymentInstrument <CshInPmtInstrm> [1..1]  4010
{Or     PaymentCardDetails <PmtCardDtls> [1..1]  4015
       Type <Tp> [1..1] CodeSet 4016
       Number <Nb> [1..1] Text 4016
       HolderName <HldrNm> [1..1] Text 4016
       StartDate <StartDt> [0..1] YearMonth 4016
       ExpiryDate <XpryDt> [1..1] YearMonth 4016
       CardIssuerName <CardIssrNm> [0..1] Text 4016
       CardIssuerIdentification <CardIssrId> [0..1] ± 4016
       SecurityCode <SctyCd> [0..1] Text 4017
       SequenceNumber <SeqNb> [0..1] Text 4017
Or     CreditTransferDetails <CdtTrfDtls> [1..1]  4017
       Reference <Ref> [0..1] Text 4020
       Debtor <Dbtr> [0..1] ± 4020
       DebtorAccount <DbtrAcct> [0..1]  4020
         Identification <Id> [1..1]  4020
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4021
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4021
Or}           Other <Othr> [1..1] ± 4021
         Name <Nm> [0..1] Text 4022
       DebtorAgent <DbtrAgt> [0..1]  4022
         Party <Pty> [1..1]  4022
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4023
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4023
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4023
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4024
         LEI <LEI> [0..1] IdentifierSet 4024
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  4025
         Identification <Id> [1..1]  4025
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4025
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4003 May 2026
```

## File page 4004

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4026
Or}           Other <Othr> [1..1] ± 4026
         Name <Nm> [0..1] Text 4026
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  4026
         Party <Pty> [1..1]  4027
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4027
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4027
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4028
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4029
         LEI <LEI> [0..1] IdentifierSet 4029
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4030
         Identification <Id> [1..1]  4030
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4030
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4031
Or}           Other <Othr> [1..1] ± 4031
         Name <Nm> [0..1] Text 4031
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  4031
         Party <Pty> [1..1]  4032
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4032
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4033
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4034
         LEI <LEI> [0..1] IdentifierSet 4034
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4035
         Identification <Id> [1..1]  4035
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4035
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4036
Or}           Other <Othr> [1..1] ± 4036
         Name <Nm> [0..1] Text 4036
       CreditorAgent <CdtrAgt> [1..1]  4036
         Party <Pty> [1..1]  4037
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4004 May 2026
```

## File page 4005

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4037
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4037
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4038
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4039
         LEI <LEI> [0..1] IdentifierSet 4039
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  4040
         Identification <Id> [1..1]  4040
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4040
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4041
Or}           Other <Othr> [1..1] ± 4041
         Name <Nm> [0..1] Text 4041
       Creditor <Cdtr> [0..1] ± 4041
       CreditorAccount <CdtrAcct> [1..1]  4042
         Identification <Id> [1..1]  4042
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4042
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4043
Or}           Other <Othr> [1..1] ± 4043
         Name <Nm> [0..1] Text 4043
Or     DirectDebitDetails <DrctDbtDtls> [1..1]  4043
       DebtorAccount <DbtrAcct> [1..1]  4044
         Identification <Id> [1..1]  4045
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4045
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4045
Or}           Other <Othr> [1..1] ± 4046
         Name <Nm> [0..1] Text 4046
       Debtor <Dbtr> [0..1] ± 4046
       DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4046
       DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 4047
       Creditor <Cdtr> [0..1] ± 4047
       DebtorAgent <DbtrAgt> [1..1]  4047
         Party <Pty> [1..1]  4047
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4005 May 2026
```

## File page 4006

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4048
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4048
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4049
         LEI <LEI> [0..1] IdentifierSet 4049
       DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4050
       CreditorAgent <CdtrAgt> [0..1]  4050
         Party <Pty> [1..1]  4050
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4051
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4051
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4051
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4052
         LEI <LEI> [0..1] IdentifierSet 4052
       CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4053
       RegistrationIdentification <RegnId> [0..1] Text 4053
       MandateIdentification <MndtId> [0..1] Text 4053
Or     ChequeDetails <ChqDtls> [1..1]  4053
       Number <Nb> [0..1] Text 4054
       PayeeIdentification <PyeeId> [1..1] ± 4054
       DraweeIdentification <DrweeId> [0..1]  4054
         Party <Pty> [1..1]  4055
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4055
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4055
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4056
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4057
         LEI <LEI> [0..1] IdentifierSet 4057
       DrawerIdentification <DrwrId> [0..1] ± 4058
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  4058
       Number <Nb> [0..1] Text 4058
       PayeeIdentification <PyeeId> [1..1] ± 4058
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4006 May 2026
```

## File page 4007

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  4059
         Party <Pty> [1..1]  4059
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4059
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4060
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4060
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4061
         LEI <LEI> [0..1] IdentifierSet 4061
       DrawerIdentification <DrwrId> [0..1] ± 4062
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 4062
       AccountIdentification <AcctId> [0..1] Text 4062
       Type <Tp> [0..1] ± 4062
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  4063
       Identification <Id> [1..1] Text 4063
       Type <Tp> [0..1] ± 4063
       Name <Nm> [0..1] Text 4063
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4064
Or}   CashOutPaymentInstrument <CshOutPmtInstrm> [1..1]  4064
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  4068
       Reference <Ref> [0..1] Text 4071
       Debtor <Dbtr> [0..1] ± 4071
       DebtorAccount <DbtrAcct> [0..1]  4071
         Identification <Id> [1..1]  4071
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4072
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4072
Or}           Other <Othr> [1..1] ± 4072
         Name <Nm> [0..1] Text 4073
       DebtorAgent <DbtrAgt> [0..1]  4073
         Party <Pty> [1..1]  4073
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4074
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4074
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4074
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4007 May 2026
```

## File page 4008

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4075
         LEI <LEI> [0..1] IdentifierSet 4075
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  4076
         Identification <Id> [1..1]  4076
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4076
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4077
Or}           Other <Othr> [1..1] ± 4077
         Name <Nm> [0..1] Text 4077
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  4077
         Party <Pty> [1..1]  4078
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4078
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4078
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4079
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4080
         LEI <LEI> [0..1] IdentifierSet 4080
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4081
         Identification <Id> [1..1]  4081
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4081
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4082
Or}           Other <Othr> [1..1] ± 4082
         Name <Nm> [0..1] Text 4082
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  4082
         Party <Pty> [1..1]  4083
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4083
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4083
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4084
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4085
         LEI <LEI> [0..1] IdentifierSet 4085
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4086
         Identification <Id> [1..1]  4086
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4086
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4008 May 2026
```

## File page 4009

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4087
Or}           Other <Othr> [1..1] ± 4087
         Name <Nm> [0..1] Text 4087
       CreditorAgent <CdtrAgt> [1..1]  4087
         Party <Pty> [1..1]  4088
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4088
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4088
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4089
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4090
         LEI <LEI> [0..1] IdentifierSet 4090
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  4091
         Identification <Id> [1..1]  4091
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4091
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4092
Or}           Other <Othr> [1..1] ± 4092
         Name <Nm> [0..1] Text 4092
       Creditor <Cdtr> [0..1] ± 4092
       CreditorAccount <CdtrAcct> [1..1]  4093
         Identification <Id> [1..1]  4093
{Or           IBAN <IBAN> [1..1] IdentifierSet C17 4093
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4094
Or}           Other <Othr> [1..1] ± 4094
         Name <Nm> [0..1] Text 4094
Or     ChequeDetails <ChqDtls> [1..1]  4094
       Number <Nb> [0..1] Text 4095
       PayeeIdentification <PyeeId> [1..1] ± 4095
       DraweeIdentification <DrweeId> [0..1]  4095
         Party <Pty> [1..1]  4096
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4096
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4096
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4097
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4009 May 2026
```

