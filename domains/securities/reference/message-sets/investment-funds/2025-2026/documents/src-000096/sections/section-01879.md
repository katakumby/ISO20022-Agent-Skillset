---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.1 PaymentCardDetails <PmtCardDtls>", "47.4.4.8.20.1.1.8 SecurityCode <SctyCd>"]
file_pages: [2643, 2644, 2645]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2643 to 2645.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2643

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
47.4.4.8.20.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
47.4.4.8.20.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
47.4.4.8.20.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2643 May 2026
```

## File page 2644

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2646
   Debtor <Dbtr> [0..1] ± 2646
   DebtorAccount <DbtrAcct> [0..1]  2646
     Identification <Id> [1..1]  2646
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2647
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2647
Or}       Other <Othr> [1..1] ± 2647
     Name <Nm> [0..1] Text 2648
   DebtorAgent <DbtrAgt> [0..1]  2648
     Party <Pty> [1..1]  2648
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2649
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2649
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2649
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2650
     LEI <LEI> [0..1] IdentifierSet 2650
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2651
     Identification <Id> [1..1]  2651
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2651
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2652
Or}       Other <Othr> [1..1] ± 2652
     Name <Nm> [0..1] Text 2652
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2652
     Party <Pty> [1..1]  2653
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2653
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2653
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2654
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2655
     LEI <LEI> [0..1] IdentifierSet 2655
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2656
     Identification <Id> [1..1]  2656
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2644 May 2026
```

## File page 2645

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2656
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2657
Or}       Other <Othr> [1..1] ± 2657
     Name <Nm> [0..1] Text 2657
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2657
     Party <Pty> [1..1]  2658
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2658
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2658
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2659
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2660
     LEI <LEI> [0..1] IdentifierSet 2660
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2661
     Identification <Id> [1..1]  2661
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2661
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2662
Or}       Other <Othr> [1..1] ± 2662
     Name <Nm> [0..1] Text 2662
   CreditorAgent <CdtrAgt> [1..1]  2662
     Party <Pty> [1..1]  2663
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2663
Or       BICFI <BICFI> [1..1] IdentifierSet C6 2663
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2664
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2665
     LEI <LEI> [0..1] IdentifierSet 2665
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2666
     Identification <Id> [1..1]  2666
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2666
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2667
Or}       Other <Othr> [1..1] ± 2667
     Name <Nm> [0..1] Text 2667
   Creditor <Cdtr> [0..1] ± 2667
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2645 May 2026
```

