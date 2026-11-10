---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "47.4.4.12.1 PaymentInstrument <PmtInstrm>", "47.4.4.12.1.1 PaymentCardDetails <PmtCardDtls>", "47.4.4.12.1.1.8 SecurityCode <SctyCd>"]
file_pages: [2713, 2714, 2715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.12.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2713 to 2715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2713

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
47.4.4.12.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
47.4.4.12.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
47.4.4.12.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2713 May 2026
```

## File page 2714

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2716
   Debtor <Dbtr> [0..1] ± 2716
   DebtorAccount <DbtrAcct> [0..1]  2716
     Identification <Id> [1..1]  2716
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2717
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2717
Or}       Other <Othr> [1..1] ± 2717
     Name <Nm> [0..1] Text 2718
   DebtorAgent <DbtrAgt> [0..1]  2718
     Party <Pty> [1..1]  2718
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2719
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2719
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2719
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2720
     LEI <LEI> [0..1] IdentifierSet 2720
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2721
     Identification <Id> [1..1]  2721
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2721
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2722
Or}       Other <Othr> [1..1] ± 2722
     Name <Nm> [0..1] Text 2722
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2722
     Party <Pty> [1..1]  2723
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2723
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2723
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2724
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2725
     LEI <LEI> [0..1] IdentifierSet 2725
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2726
     Identification <Id> [1..1]  2726
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2714 May 2026
```

## File page 2715

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2726
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2727
Or}       Other <Othr> [1..1] ± 2727
     Name <Nm> [0..1] Text 2727
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2727
     Party <Pty> [1..1]  2728
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2728
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2728
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2729
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2730
     LEI <LEI> [0..1] IdentifierSet 2730
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2731
     Identification <Id> [1..1]  2731
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2731
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2732
Or}       Other <Othr> [1..1] ± 2732
     Name <Nm> [0..1] Text 2732
   CreditorAgent <CdtrAgt> [1..1]  2732
     Party <Pty> [1..1]  2733
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2733
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2733
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2734
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2735
     LEI <LEI> [0..1] IdentifierSet 2735
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2736
     Identification <Id> [1..1]  2736
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2736
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2737
Or}       Other <Othr> [1..1] ± 2737
     Name <Nm> [0..1] Text 2737
   Creditor <Cdtr> [0..1] ± 2737
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2715 May 2026
```

