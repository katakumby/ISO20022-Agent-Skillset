---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.1 PaymentCardDetails <PmtCardDtls>", "50.4.4.10.1.1.8 SecurityCode <SctyCd>"]
file_pages: [3194, 3195, 3196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3194 to 3196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3194

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.10.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
50.4.4.10.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
50.4.4.10.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3194 May 2026
```

## File page 3195

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 3197
   Debtor <Dbtr> [0..1] ± 3197
   DebtorAccount <DbtrAcct> [0..1]  3197
     Identification <Id> [1..1]  3197
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3198
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3198
Or}       Other <Othr> [1..1] ± 3198
     Name <Nm> [0..1] Text 3199
   DebtorAgent <DbtrAgt> [0..1]  3199
     Party <Pty> [1..1]  3199
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3200
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3200
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3200
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3201
     LEI <LEI> [0..1] IdentifierSet 3201
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  3202
     Identification <Id> [1..1]  3202
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3202
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3203
Or}       Other <Othr> [1..1] ± 3203
     Name <Nm> [0..1] Text 3203
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  3203
     Party <Pty> [1..1]  3204
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3204
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3204
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3205
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3206
     LEI <LEI> [0..1] IdentifierSet 3206
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3207
     Identification <Id> [1..1]  3207
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3195 May 2026
```

## File page 3196

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3207
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3208
Or}       Other <Othr> [1..1] ± 3208
     Name <Nm> [0..1] Text 3208
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  3208
     Party <Pty> [1..1]  3209
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3209
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3209
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3210
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3211
     LEI <LEI> [0..1] IdentifierSet 3211
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3212
     Identification <Id> [1..1]  3212
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3212
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3213
Or}       Other <Othr> [1..1] ± 3213
     Name <Nm> [0..1] Text 3213
   CreditorAgent <CdtrAgt> [1..1]  3213
     Party <Pty> [1..1]  3214
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3214
Or       BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3215
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3216
     LEI <LEI> [0..1] IdentifierSet 3216
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  3217
     Identification <Id> [1..1]  3217
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 3217
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3218
Or}       Other <Othr> [1..1] ± 3218
     Name <Nm> [0..1] Text 3218
   Creditor <Cdtr> [0..1] ± 3218
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3196 May 2026
```

