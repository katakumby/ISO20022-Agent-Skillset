---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.1 PaymentCardDetails <PmtCardDtls>", "53.4.5.18.1.1.1.8 SecurityCode <SctyCd>"]
file_pages: [3704, 3705, 3706]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3704 to 3706.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3704

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.18.1.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
53.4.5.18.1.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
53.4.5.18.1.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3704 May 2026
```

## File page 3705

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 3707
   Debtor <Dbtr> [0..1] ± 3707
   DebtorAccount <DbtrAcct> [0..1]  3707
     Identification <Id> [1..1]  3707
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3708
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3708
Or}       Other <Othr> [1..1] ± 3708
     Name <Nm> [0..1] Text 3709
   DebtorAgent <DbtrAgt> [0..1]  3709
     Party <Pty> [1..1]  3709
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3710
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3710
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3710
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3711
     LEI <LEI> [0..1] IdentifierSet 3711
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  3712
     Identification <Id> [1..1]  3712
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Or}       Other <Othr> [1..1] ± 3713
     Name <Nm> [0..1] Text 3713
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  3713
     Party <Pty> [1..1]  3714
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3714
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3714
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3715
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3716
     LEI <LEI> [0..1] IdentifierSet 3716
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3717
     Identification <Id> [1..1]  3717
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3705 May 2026
```

## File page 3706

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3717
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3718
Or}       Other <Othr> [1..1] ± 3718
     Name <Nm> [0..1] Text 3718
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  3718
     Party <Pty> [1..1]  3719
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3719
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3719
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3720
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3721
     LEI <LEI> [0..1] IdentifierSet 3721
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3722
     Identification <Id> [1..1]  3722
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3722
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3723
Or}       Other <Othr> [1..1] ± 3723
     Name <Nm> [0..1] Text 3723
   CreditorAgent <CdtrAgt> [1..1]  3723
     Party <Pty> [1..1]  3724
{Or       NameAndAddress <NmAndAdr> [1..1] ± 3724
Or       BICFI <BICFI> [1..1] IdentifierSet C5 3724
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3725
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 3726
     LEI <LEI> [0..1] IdentifierSet 3726
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  3727
     Identification <Id> [1..1]  3727
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3727
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3728
Or}       Other <Othr> [1..1] ± 3728
     Name <Nm> [0..1] Text 3728
   Creditor <Cdtr> [0..1] ± 3728
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3706 May 2026
```

