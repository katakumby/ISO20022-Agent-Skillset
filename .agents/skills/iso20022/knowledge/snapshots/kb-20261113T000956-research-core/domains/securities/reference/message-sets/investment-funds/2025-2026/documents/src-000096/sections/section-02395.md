---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.1 PaymentCardDetails <PmtCardDtls>", "52.4.5.10.35.1.1.8 SecurityCode <SctyCd>"]
file_pages: [3369, 3370, 3371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3369 to 3371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3369

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
52.4.5.10.35.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
52.4.5.10.35.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
52.4.5.10.35.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3369 May 2026
```

## File page 3370

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 3372
   Debtor <Dbtr> [0..1] ± 3372
   DebtorAccount <DbtrAcct> [0..1]  3372
     Identification <Id> [1..1]  3372
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3373
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3373
Or}       Other <Othr> [1..1] ± 3373
     Name <Nm> [0..1] Text 3374
   DebtorAgent <DbtrAgt> [0..1]  3374
     Party <Pty> [1..1]  3374
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3375
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3375
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3375
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3376
     LEI <LEI> [0..1] IdentifierSet 3376
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  3377
     Identification <Id> [1..1]  3377
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3377
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3378
Or}       Other <Othr> [1..1] ± 3378
     Name <Nm> [0..1] Text 3378
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  3378
     Party <Pty> [1..1]  3379
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3379
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3379
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3380
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3381
     LEI <LEI> [0..1] IdentifierSet 3381
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3382
     Identification <Id> [1..1]  3382
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3370 May 2026
```

## File page 3371

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3382
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3383
Or}       Other <Othr> [1..1] ± 3383
     Name <Nm> [0..1] Text 3383
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  3383
     Party <Pty> [1..1]  3384
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3384
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3384
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3385
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3386
     LEI <LEI> [0..1] IdentifierSet 3386
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3387
     Identification <Id> [1..1]  3387
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3387
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3388
Or}       Other <Othr> [1..1] ± 3388
     Name <Nm> [0..1] Text 3388
   CreditorAgent <CdtrAgt> [1..1]  3388
     Party <Pty> [1..1]  3389
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3389
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3389
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3390
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3391
     LEI <LEI> [0..1] IdentifierSet 3391
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  3392
     Identification <Id> [1..1]  3392
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3392
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3393
Or}       Other <Othr> [1..1] ± 3393
     Name <Nm> [0..1] Text 3393
   Creditor <Cdtr> [0..1] ± 3393
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3371 May 2026
```

