---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.1 PaymentCardDetails <PmtCardDtls>", "49.4.5.13.1.1.8 SecurityCode <SctyCd>"]
file_pages: [2953, 2954, 2955]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2953 to 2955.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2953

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.13.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
49.4.5.13.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
49.4.5.13.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2953 May 2026
```

## File page 2954

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2956
   Debtor <Dbtr> [0..1] ± 2956
   DebtorAccount <DbtrAcct> [0..1]  2956
     Identification <Id> [1..1]  2956
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2957
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2957
Or}       Other <Othr> [1..1] ± 2957
     Name <Nm> [0..1] Text 2958
   DebtorAgent <DbtrAgt> [0..1]  2958
     Party <Pty> [1..1]  2958
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2959
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2959
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2959
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2960
     LEI <LEI> [0..1] IdentifierSet 2960
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2961
     Identification <Id> [1..1]  2961
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2961
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2962
Or}       Other <Othr> [1..1] ± 2962
     Name <Nm> [0..1] Text 2962
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2962
     Party <Pty> [1..1]  2963
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2963
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2963
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2964
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2965
     LEI <LEI> [0..1] IdentifierSet 2965
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2966
     Identification <Id> [1..1]  2966
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2954 May 2026
```

## File page 2955

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2966
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2967
Or}       Other <Othr> [1..1] ± 2967
     Name <Nm> [0..1] Text 2967
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2967
     Party <Pty> [1..1]  2968
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2968
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2968
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2969
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2970
     LEI <LEI> [0..1] IdentifierSet 2970
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2971
     Identification <Id> [1..1]  2971
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2971
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2972
Or}       Other <Othr> [1..1] ± 2972
     Name <Nm> [0..1] Text 2972
   CreditorAgent <CdtrAgt> [1..1]  2972
     Party <Pty> [1..1]  2973
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2973
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2973
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2974
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2975
     LEI <LEI> [0..1] IdentifierSet 2975
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2976
     Identification <Id> [1..1]  2976
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2976
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2977
Or}       Other <Othr> [1..1] ± 2977
     Name <Nm> [0..1] Text 2977
   Creditor <Cdtr> [0..1] ± 2977
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2955 May 2026
```

