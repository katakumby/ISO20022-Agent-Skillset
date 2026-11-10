---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.1 PaymentCardDetails <PmtCardDtls>", "52.4.5.12.1.1.8 SecurityCode <SctyCd>"]
file_pages: [3439, 3440, 3441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3439 to 3441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3439

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
52.4.5.12.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
52.4.5.12.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
52.4.5.12.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3439 May 2026
```

## File page 3440

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 3442
   Debtor <Dbtr> [0..1] ± 3442
   DebtorAccount <DbtrAcct> [0..1]  3442
     Identification <Id> [1..1]  3442
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3443
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3443
Or}       Other <Othr> [1..1] ± 3443
     Name <Nm> [0..1] Text 3444
   DebtorAgent <DbtrAgt> [0..1]  3444
     Party <Pty> [1..1]  3444
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3445
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3445
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3445
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3446
     LEI <LEI> [0..1] IdentifierSet 3446
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  3447
     Identification <Id> [1..1]  3447
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3447
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3448
Or}       Other <Othr> [1..1] ± 3448
     Name <Nm> [0..1] Text 3448
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  3448
     Party <Pty> [1..1]  3449
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3449
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3449
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3450
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3451
     LEI <LEI> [0..1] IdentifierSet 3451
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3452
     Identification <Id> [1..1]  3452
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3440 May 2026
```

## File page 3441

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3452
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3453
Or}       Other <Othr> [1..1] ± 3453
     Name <Nm> [0..1] Text 3453
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  3453
     Party <Pty> [1..1]  3454
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3454
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3454
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3455
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3456
     LEI <LEI> [0..1] IdentifierSet 3456
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3457
     Identification <Id> [1..1]  3457
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3457
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3458
Or}       Other <Othr> [1..1] ± 3458
     Name <Nm> [0..1] Text 3458
   CreditorAgent <CdtrAgt> [1..1]  3458
     Party <Pty> [1..1]  3459
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3459
Or       BICFI <BICFI> [1..1] IdentifierSet C7 3459
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3460
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3461
     LEI <LEI> [0..1] IdentifierSet 3461
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  3462
     Identification <Id> [1..1]  3462
{Or       IBAN <IBAN> [1..1] IdentifierSet C22 3462
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3463
Or}       Other <Othr> [1..1] ± 3463
     Name <Nm> [0..1] Text 3463
   Creditor <Cdtr> [0..1] ± 3463
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3441 May 2026
```

