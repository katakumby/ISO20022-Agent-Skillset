---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [3994, 3995, 3996, 3997, 3998, 3999, 4000, 4001]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3994 to 4001.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3994

```text
Definition: Part of an investor's subscription amount that is held by the fund in order to pay incentive/
performance fees at the end of the fiscal year.
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
55.4.5.21  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3994 May 2026
```

## File page 3995

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction181 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInOrOut <CshInOrOut> [1..1]  4002
{Or     CashInPaymentInstrument <CshInPmtInstrm> [1..1]  4010
{Or       PaymentCardDetails <PmtCardDtls> [1..1]  4015
         Type <Tp> [1..1] CodeSet 4016
         Number <Nb> [1..1] Text 4016
         HolderName <HldrNm> [1..1] Text 4016
         StartDate <StartDt> [0..1] YearMonth 4016
         ExpiryDate <XpryDt> [1..1] YearMonth 4016
         CardIssuerName <CardIssrNm> [0..1] Text 4016
         CardIssuerIdentification <CardIssrId> [0..1] ± 4016
         SecurityCode <SctyCd> [0..1] Text 4017
         SequenceNumber <SeqNb> [0..1] Text 4017
Or       CreditTransferDetails <CdtTrfDtls> [1..1]  4017
         Reference <Ref> [0..1] Text 4020
         Debtor <Dbtr> [0..1] ± 4020
         DebtorAccount <DbtrAcct> [0..1]  4020
           Identification <Id> [1..1]  4020
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4021
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4021
Or}             Other <Othr> [1..1] ± 4021
           Name <Nm> [0..1] Text 4022
         DebtorAgent <DbtrAgt> [0..1]  4022
           Party <Pty> [1..1]  4022
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4023
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4023
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4023
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4024
           LEI <LEI> [0..1] IdentifierSet 4024
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  4025
           Identification <Id> [1..1]  4025
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3995 May 2026
```

## File page 3996

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4025
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4026
Or}             Other <Othr> [1..1] ± 4026
           Name <Nm> [0..1] Text 4026
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  4026
           Party <Pty> [1..1]  4027
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4027
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4027
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4028
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4029
           LEI <LEI> [0..1] IdentifierSet 4029
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4030
           Identification <Id> [1..1]  4030
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4030
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4031
Or}             Other <Othr> [1..1] ± 4031
           Name <Nm> [0..1] Text 4031
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  4031
           Party <Pty> [1..1]  4032
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4032
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4033
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4034
           LEI <LEI> [0..1] IdentifierSet 4034
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4035
           Identification <Id> [1..1]  4035
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4035
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4036
Or}             Other <Othr> [1..1] ± 4036
           Name <Nm> [0..1] Text 4036
         CreditorAgent <CdtrAgt> [1..1]  4036
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3996 May 2026
```

## File page 3997

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Party <Pty> [1..1]  4037
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4037
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4037
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4038
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4039
           LEI <LEI> [0..1] IdentifierSet 4039
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  4040
           Identification <Id> [1..1]  4040
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4040
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4041
Or}             Other <Othr> [1..1] ± 4041
           Name <Nm> [0..1] Text 4041
         Creditor <Cdtr> [0..1] ± 4041
         CreditorAccount <CdtrAcct> [1..1]  4042
           Identification <Id> [1..1]  4042
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4042
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4043
Or}             Other <Othr> [1..1] ± 4043
           Name <Nm> [0..1] Text 4043
Or       DirectDebitDetails <DrctDbtDtls> [1..1]  4043
         DebtorAccount <DbtrAcct> [1..1]  4044
           Identification <Id> [1..1]  4045
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4045
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4045
Or}             Other <Othr> [1..1] ± 4046
           Name <Nm> [0..1] Text 4046
         Debtor <Dbtr> [0..1] ± 4046
         DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4046
         DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 4047
         Creditor <Cdtr> [0..1] ± 4047
         DebtorAgent <DbtrAgt> [1..1]  4047
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3997 May 2026
```

## File page 3998

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Party <Pty> [1..1]  4047
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4048
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4048
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4049
           LEI <LEI> [0..1] IdentifierSet 4049
         DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4050
         CreditorAgent <CdtrAgt> [0..1]  4050
           Party <Pty> [1..1]  4050
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4051
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4051
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4051
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4052
           LEI <LEI> [0..1] IdentifierSet 4052
         CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4053
         RegistrationIdentification <RegnId> [0..1] Text 4053
         MandateIdentification <MndtId> [0..1] Text 4053
Or       ChequeDetails <ChqDtls> [1..1]  4053
         Number <Nb> [0..1] Text 4054
         PayeeIdentification <PyeeId> [1..1] ± 4054
         DraweeIdentification <DrweeId> [0..1]  4054
           Party <Pty> [1..1]  4055
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4055
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4055
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4056
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4057
           LEI <LEI> [0..1] IdentifierSet 4057
         DrawerIdentification <DrwrId> [0..1] ± 4058
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  4058
         Number <Nb> [0..1] Text 4058
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3998 May 2026
```

## File page 3999

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PayeeIdentification <PyeeId> [1..1] ± 4058
         DraweeIdentification <DrweeId> [0..1]  4059
           Party <Pty> [1..1]  4059
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4059
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4060
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4060
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4061
           LEI <LEI> [0..1] IdentifierSet 4061
         DrawerIdentification <DrwrId> [0..1] ± 4062
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 4062
         AccountIdentification <AcctId> [0..1] Text 4062
         Type <Tp> [0..1] ± 4062
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  4063
         Identification <Id> [1..1] Text 4063
         Type <Tp> [0..1] ± 4063
         Name <Nm> [0..1] Text 4063
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4064
Or}     CashOutPaymentInstrument <CshOutPmtInstrm> [1..1]  4064
{Or       CreditTransferDetails <CdtTrfDtls> [1..1]  4068
         Reference <Ref> [0..1] Text 4071
         Debtor <Dbtr> [0..1] ± 4071
         DebtorAccount <DbtrAcct> [0..1]  4071
           Identification <Id> [1..1]  4071
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4072
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4072
Or}             Other <Othr> [1..1] ± 4072
           Name <Nm> [0..1] Text 4073
         DebtorAgent <DbtrAgt> [0..1]  4073
           Party <Pty> [1..1]  4073
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4074
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4074
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3999 May 2026
```

## File page 4000

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4074
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4075
           LEI <LEI> [0..1] IdentifierSet 4075
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  4076
           Identification <Id> [1..1]  4076
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4076
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4077
Or}             Other <Othr> [1..1] ± 4077
           Name <Nm> [0..1] Text 4077
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  4077
           Party <Pty> [1..1]  4078
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4078
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4078
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4079
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4080
           LEI <LEI> [0..1] IdentifierSet 4080
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4081
           Identification <Id> [1..1]  4081
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4081
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4082
Or}             Other <Othr> [1..1] ± 4082
           Name <Nm> [0..1] Text 4082
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  4082
           Party <Pty> [1..1]  4083
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4083
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4083
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4084
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4085
           LEI <LEI> [0..1] IdentifierSet 4085
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4086
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4000 May 2026
```

## File page 4001

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  4086
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4086
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4087
Or}             Other <Othr> [1..1] ± 4087
           Name <Nm> [0..1] Text 4087
         CreditorAgent <CdtrAgt> [1..1]  4087
           Party <Pty> [1..1]  4088
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4088
Or             BICFI <BICFI> [1..1] IdentifierSet C6 4088
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4089
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 4090
           LEI <LEI> [0..1] IdentifierSet 4090
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  4091
           Identification <Id> [1..1]  4091
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4091
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4092
Or}             Other <Othr> [1..1] ± 4092
           Name <Nm> [0..1] Text 4092
         Creditor <Cdtr> [0..1] ± 4092
         CreditorAccount <CdtrAcct> [1..1]  4093
           Identification <Id> [1..1]  4093
{Or             IBAN <IBAN> [1..1] IdentifierSet C17 4093
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4094
Or}             Other <Othr> [1..1] ± 4094
           Name <Nm> [0..1] Text 4094
Or       ChequeDetails <ChqDtls> [1..1]  4094
         Number <Nb> [0..1] Text 4095
         PayeeIdentification <PyeeId> [1..1] ± 4095
         DraweeIdentification <DrweeId> [0..1]  4095
           Party <Pty> [1..1]  4096
{Or             NameAndAddress <NmAndAdr> [1..1] ± 4096
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4001 May 2026
```

