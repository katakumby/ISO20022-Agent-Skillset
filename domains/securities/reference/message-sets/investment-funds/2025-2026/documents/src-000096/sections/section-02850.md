---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>"]
file_pages: [4010, 4011, 4012, 4013, 4014]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4010 to 4014.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4010

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4098
         LEI <LEI> [0..1] IdentifierSet 4098
       DrawerIdentification <DrwrId> [0..1] ± 4099
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  4099
       Number <Nb> [0..1] Text 4099
       PayeeIdentification <PyeeId> [1..1] ± 4099
       DraweeIdentification <DrweeId> [0..1]  4100
         Party <Pty> [1..1]  4100
{Or           NameAndAddress <NmAndAdr> [1..1] ± 4100
Or           BICFI <BICFI> [1..1] IdentifierSet C6 4101
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4101
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 4102
         LEI <LEI> [0..1] IdentifierSet 4102
       DrawerIdentification <DrwrId> [0..1] ± 4103
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 4103
       AccountIdentification <AcctId> [0..1] Text 4103
       Type <Tp> [0..1] ± 4103
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  4104
       Identification <Id> [1..1] Text 4104
       Type <Tp> [0..1] ± 4104
       Name <Nm> [0..1] Text 4104
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4105
55.4.5.21.1.1  CashInPaymentInstrument <CshInPmtInstrm>
Presence: [1..1]
Definition: Payment instrument for the cash-in flow.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4010 May 2026
```

## File page 4011

```text
CashInPaymentInstrument <CshInPmtInstrm> contains one of the following
PaymentInstrument30Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  4015
     Type <Tp> [1..1] CodeSet 4016
     Number <Nb> [1..1] Text 4016
     HolderName <HldrNm> [1..1] Text 4016
     StartDate <StartDt> [0..1] YearMonth 4016
     ExpiryDate <XpryDt> [1..1] YearMonth 4016
     CardIssuerName <CardIssrNm> [0..1] Text 4016
     CardIssuerIdentification <CardIssrId> [0..1] ± 4016
     SecurityCode <SctyCd> [0..1] Text 4017
     SequenceNumber <SeqNb> [0..1] Text 4017
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  4017
     Reference <Ref> [0..1] Text 4020
     Debtor <Dbtr> [0..1] ± 4020
     DebtorAccount <DbtrAcct> [0..1]  4020
       Identification <Id> [1..1]  4020
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4021
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4021
Or}         Other <Othr> [1..1] ± 4021
       Name <Nm> [0..1] Text 4022
     DebtorAgent <DbtrAgt> [0..1]  4022
       Party <Pty> [1..1]  4022
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4023
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4023
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4023
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4024
       LEI <LEI> [0..1] IdentifierSet 4024
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  4025
       Identification <Id> [1..1]  4025
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4025
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4026
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4011 May 2026
```

## File page 4012

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 4026
       Name <Nm> [0..1] Text 4026
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  4026
       Party <Pty> [1..1]  4027
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4027
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4027
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4028
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4029
       LEI <LEI> [0..1] IdentifierSet 4029
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4030
       Identification <Id> [1..1]  4030
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4030
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4031
Or}         Other <Othr> [1..1] ± 4031
       Name <Nm> [0..1] Text 4031
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  4031
       Party <Pty> [1..1]  4032
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4032
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4033
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4034
       LEI <LEI> [0..1] IdentifierSet 4034
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4035
       Identification <Id> [1..1]  4035
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4035
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4036
Or}         Other <Othr> [1..1] ± 4036
       Name <Nm> [0..1] Text 4036
     CreditorAgent <CdtrAgt> [1..1]  4036
       Party <Pty> [1..1]  4037
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4037
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4012 May 2026
```

## File page 4013

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4037
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4038
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4039
       LEI <LEI> [0..1] IdentifierSet 4039
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  4040
       Identification <Id> [1..1]  4040
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4040
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4041
Or}         Other <Othr> [1..1] ± 4041
       Name <Nm> [0..1] Text 4041
     Creditor <Cdtr> [0..1] ± 4041
     CreditorAccount <CdtrAcct> [1..1]  4042
       Identification <Id> [1..1]  4042
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4042
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4043
Or}         Other <Othr> [1..1] ± 4043
       Name <Nm> [0..1] Text 4043
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  4043
     DebtorAccount <DbtrAcct> [1..1]  4044
       Identification <Id> [1..1]  4045
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4045
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4045
Or}         Other <Othr> [1..1] ± 4046
       Name <Nm> [0..1] Text 4046
     Debtor <Dbtr> [0..1] ± 4046
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4046
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 4047
     Creditor <Cdtr> [0..1] ± 4047
     DebtorAgent <DbtrAgt> [1..1]  4047
       Party <Pty> [1..1]  4047
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4048
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4013 May 2026
```

## File page 4014

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4048
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4049
       LEI <LEI> [0..1] IdentifierSet 4049
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4050
     CreditorAgent <CdtrAgt> [0..1]  4050
       Party <Pty> [1..1]  4050
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4051
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4051
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4051
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4052
       LEI <LEI> [0..1] IdentifierSet 4052
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4053
     RegistrationIdentification <RegnId> [0..1] Text 4053
     MandateIdentification <MndtId> [0..1] Text 4053
Or   ChequeDetails <ChqDtls> [1..1]  4053
     Number <Nb> [0..1] Text 4054
     PayeeIdentification <PyeeId> [1..1] ± 4054
     DraweeIdentification <DrweeId> [0..1]  4054
       Party <Pty> [1..1]  4055
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4055
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4055
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4056
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4057
       LEI <LEI> [0..1] IdentifierSet 4057
     DrawerIdentification <DrwrId> [0..1] ± 4058
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  4058
     Number <Nb> [0..1] Text 4058
     PayeeIdentification <PyeeId> [1..1] ± 4058
     DraweeIdentification <DrweeId> [0..1]  4059
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4014 May 2026
```

