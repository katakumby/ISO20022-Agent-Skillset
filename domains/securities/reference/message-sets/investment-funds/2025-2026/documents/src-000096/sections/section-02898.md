---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.7 BlockChainCashWallet <BlckChainCshWllt>", "55.4.5.21.1.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [4064, 4065, 4066, 4067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4064 to 4067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4064

```text
55.4.5.21.1.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
55.4.5.21.1.2  CashOutPaymentInstrument <CshOutPmtInstrm>
Presence: [1..1]
Definition: Payment instrument for the cash-out flow.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4064 May 2026
```

## File page 4065

```text
CashOutPaymentInstrument <CshOutPmtInstrm> contains one of the following
PaymentInstrument28Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CreditTransferDetails <CdtTrfDtls> [1..1]  4068
     Reference <Ref> [0..1] Text 4071
     Debtor <Dbtr> [0..1] ± 4071
     DebtorAccount <DbtrAcct> [0..1]  4071
       Identification <Id> [1..1]  4071
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4072
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4072
Or}         Other <Othr> [1..1] ± 4072
       Name <Nm> [0..1] Text 4073
     DebtorAgent <DbtrAgt> [0..1]  4073
       Party <Pty> [1..1]  4073
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4074
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4074
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4074
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4075
       LEI <LEI> [0..1] IdentifierSet 4075
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  4076
       Identification <Id> [1..1]  4076
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4076
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4077
Or}         Other <Othr> [1..1] ± 4077
       Name <Nm> [0..1] Text 4077
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  4077
       Party <Pty> [1..1]  4078
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4078
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4078
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4079
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4080
       LEI <LEI> [0..1] IdentifierSet 4080
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4065 May 2026
```

## File page 4066

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4081
       Identification <Id> [1..1]  4081
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4081
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4082
Or}         Other <Othr> [1..1] ± 4082
       Name <Nm> [0..1] Text 4082
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  4082
       Party <Pty> [1..1]  4083
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4083
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4083
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4084
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4085
       LEI <LEI> [0..1] IdentifierSet 4085
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4086
       Identification <Id> [1..1]  4086
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4086
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4087
Or}         Other <Othr> [1..1] ± 4087
       Name <Nm> [0..1] Text 4087
     CreditorAgent <CdtrAgt> [1..1]  4087
       Party <Pty> [1..1]  4088
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4088
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4088
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4089
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4090
       LEI <LEI> [0..1] IdentifierSet 4090
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  4091
       Identification <Id> [1..1]  4091
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4091
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4092
Or}         Other <Othr> [1..1] ± 4092
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4066 May 2026
```

## File page 4067

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [0..1] Text 4092
     Creditor <Cdtr> [0..1] ± 4092
     CreditorAccount <CdtrAcct> [1..1]  4093
       Identification <Id> [1..1]  4093
{Or         IBAN <IBAN> [1..1] IdentifierSet C17 4093
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4094
Or}         Other <Othr> [1..1] ± 4094
       Name <Nm> [0..1] Text 4094
Or   ChequeDetails <ChqDtls> [1..1]  4094
     Number <Nb> [0..1] Text 4095
     PayeeIdentification <PyeeId> [1..1] ± 4095
     DraweeIdentification <DrweeId> [0..1]  4095
       Party <Pty> [1..1]  4096
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4096
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4096
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4097
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4098
       LEI <LEI> [0..1] IdentifierSet 4098
     DrawerIdentification <DrwrId> [0..1] ± 4099
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  4099
     Number <Nb> [0..1] Text 4099
     PayeeIdentification <PyeeId> [1..1] ± 4099
     DraweeIdentification <DrweeId> [0..1]  4100
       Party <Pty> [1..1]  4100
{Or         NameAndAddress <NmAndAdr> [1..1] ± 4100
Or         BICFI <BICFI> [1..1] IdentifierSet C6 4101
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4101
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 4102
       LEI <LEI> [0..1] IdentifierSet 4102
     DrawerIdentification <DrwrId> [0..1] ± 4103
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 4103
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4067 May 2026
```

