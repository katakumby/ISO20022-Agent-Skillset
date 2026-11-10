---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.1 PaymentCardDetails <PmtCardDtls>", "55.4.5.21.1.1.1.8 SecurityCode <SctyCd>"]
file_pages: [4017, 4018, 4019]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4017 to 4019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4017

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
55.4.5.21.1.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
55.4.5.21.1.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
55.4.5.21.1.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4017 May 2026
```

## File page 4018

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 4020
   Debtor <Dbtr> [0..1] ± 4020
   DebtorAccount <DbtrAcct> [0..1]  4020
     Identification <Id> [1..1]  4020
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4021
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4021
Or}       Other <Othr> [1..1] ± 4021
     Name <Nm> [0..1] Text 4022
   DebtorAgent <DbtrAgt> [0..1]  4022
     Party <Pty> [1..1]  4022
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4023
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4023
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4023
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4024
     LEI <LEI> [0..1] IdentifierSet 4024
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  4025
     Identification <Id> [1..1]  4025
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4025
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4026
Or}       Other <Othr> [1..1] ± 4026
     Name <Nm> [0..1] Text 4026
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  4026
     Party <Pty> [1..1]  4027
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4027
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4027
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4028
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4029
     LEI <LEI> [0..1] IdentifierSet 4029
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  4030
     Identification <Id> [1..1]  4030
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4018 May 2026
```

## File page 4019

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4030
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4031
Or}       Other <Othr> [1..1] ± 4031
     Name <Nm> [0..1] Text 4031
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  4031
     Party <Pty> [1..1]  4032
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4032
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4032
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4033
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4034
     LEI <LEI> [0..1] IdentifierSet 4034
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  4035
     Identification <Id> [1..1]  4035
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4035
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4036
Or}       Other <Othr> [1..1] ± 4036
     Name <Nm> [0..1] Text 4036
   CreditorAgent <CdtrAgt> [1..1]  4036
     Party <Pty> [1..1]  4037
{Or       NameAndAddress <NmAndAdr> [1..1] ± 4037
Or       BICFI <BICFI> [1..1] IdentifierSet C6 4037
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4038
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 4039
     LEI <LEI> [0..1] IdentifierSet 4039
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  4040
     Identification <Id> [1..1]  4040
{Or       IBAN <IBAN> [1..1] IdentifierSet C17 4040
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 4041
Or}       Other <Othr> [1..1] ± 4041
     Name <Nm> [0..1] Text 4041
   Creditor <Cdtr> [0..1] ± 4041
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4019 May 2026
```

