---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.1 PaymentCardDetails <PmtCardDtls>", "49.4.5.9.34.1.1.8 SecurityCode <SctyCd>"]
file_pages: [2883, 2884, 2885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.1.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2883 to 2885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2883

```text
CardIssuerIdentification <CardIssrId> contains the following elements (see "PartyIdentification139"
on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.9.34.1.1.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
49.4.5.9.34.1.1.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
49.4.5.9.34.1.2  CreditTransferDetails <CdtTrfDtls>
Presence: [1..1]
Definition: Payment instrument between a debtor and a creditor, which flows through one or more
financial institutions or systems.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2883 May 2026
```

## File page 2884

```text
CreditTransferDetails <CdtTrfDtls> contains the following CreditTransfer12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..1] Text 2886
   Debtor <Dbtr> [0..1] ± 2886
   DebtorAccount <DbtrAcct> [0..1]  2886
     Identification <Id> [1..1]  2886
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2887
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2887
Or}       Other <Othr> [1..1] ± 2887
     Name <Nm> [0..1] Text 2888
   DebtorAgent <DbtrAgt> [0..1]  2888
     Party <Pty> [1..1]  2888
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2889
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2889
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2889
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2890
     LEI <LEI> [0..1] IdentifierSet 2890
   DebtorAgentAccount <DbtrAgtAcct> [0..1]  2891
     Identification <Id> [1..1]  2891
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2891
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2892
Or}       Other <Othr> [1..1] ± 2892
     Name <Nm> [0..1] Text 2892
   IntermediaryAgent1 <IntrmyAgt1> [0..1]  2892
     Party <Pty> [1..1]  2893
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2893
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2893
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2894
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2895
     LEI <LEI> [0..1] IdentifierSet 2895
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2896
     Identification <Id> [1..1]  2896
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2884 May 2026
```

## File page 2885

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2896
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2897
Or}       Other <Othr> [1..1] ± 2897
     Name <Nm> [0..1] Text 2897
   IntermediaryAgent2 <IntrmyAgt2> [0..1]  2897
     Party <Pty> [1..1]  2898
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2898
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2898
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2899
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2900
     LEI <LEI> [0..1] IdentifierSet 2900
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2901
     Identification <Id> [1..1]  2901
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2901
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2902
Or}       Other <Othr> [1..1] ± 2902
     Name <Nm> [0..1] Text 2902
   CreditorAgent <CdtrAgt> [1..1]  2902
     Party <Pty> [1..1]  2903
{Or       NameAndAddress <NmAndAdr> [1..1] ± 2903
Or       BICFI <BICFI> [1..1] IdentifierSet C7 2903
Or       ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2904
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 2905
     LEI <LEI> [0..1] IdentifierSet 2905
   CreditorAgentAccount <CdtrAgtAcct> [0..1]  2906
     Identification <Id> [1..1]  2906
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2906
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2907
Or}       Other <Othr> [1..1] ± 2907
     Name <Nm> [0..1] Text 2907
   Creditor <Cdtr> [0..1] ± 2907
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2885 May 2026
```

