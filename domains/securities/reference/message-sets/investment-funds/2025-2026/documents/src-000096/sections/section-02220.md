---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>", "50.4.4.9.22.1 PaymentInstrument <PmtInstrm>", "50.4.4.9.22.1.1 PaymentCardDetails <PmtCardDtls>", "50.4.4.9.22.1.1.8 SecurityCode <SctyCd>"]
file_pages: [3124, 3125, 3126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3124 to 3126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3124

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.9.22.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
50.4.4.9.22.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
50.4.4.9.22.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3124 May 2026
```

## File page 3125

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 3127
   Debtor <Dbtr> [0..1] ± 3127
   DebtorAccount <DbtrAcct> [0..1]  3127
     Identification <Id> [1..1]  3127
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3128
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3128
Or}       Other <Othr> [1..1] ± 3128
     Name <Nm> [0..1] Text 3129
   DebtorAgent <DbtrAgt> [0..1]  3129
     Party <Pty> [1..1]  3129
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3130
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3130
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3130
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3131
     LEI <LEI> [0..1] IdentifierSet 3131
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  3132
     Identification <Id> [1..1]  3132
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3132
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3133
Or}       Other <Othr> [1..1] ± 3133
     Name <Nm> [0..1] Text 3133
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  3133
     Party <Pty> [1..1]  3134
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3134
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3134
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3135
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3136
     LEI <LEI> [0..1] IdentifierSet 3136
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3137
     Identification <Id> [1..1]  3137
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3125 May 2026
```

## File page 3126

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3137
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3138
Or}       Other <Othr> [1..1] ± 3138
     Name <Nm> [0..1] Text 3138
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  3138
     Party <Pty> [1..1]  3139
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3139
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3139
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3140
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3141
     LEI <LEI> [0..1] IdentifierSet 3141
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3142
     Identification <Id> [1..1]  3142
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3142
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3143
Or}       Other <Othr> [1..1] ± 3143
     Name <Nm> [0..1] Text 3143
   CreditorAgent <CdtrAgt> [1..1]  3143
     Party <Pty> [1..1]  3144
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3144
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3144
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3145
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3146
     LEI <LEI> [0..1] IdentifierSet 3146
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  3147
     Identification <Id> [1..1]  3147
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3147
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3148
Or}       Other <Othr> [1..1] ± 3148
     Name <Nm> [0..1] Text 3148
   Creditor <Cdtr> [0..1] ± 3148
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3126 May 2026
```

