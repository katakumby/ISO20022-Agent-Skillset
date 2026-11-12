---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "53.4.5.18.1.1.7 BlockChainCashWallet <BlckChainCshWllt>", "53.4.5.18.1.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [3751, 3752, 3753, 3754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3751 to 3754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3751

```text
53.4.5.18.1.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
53.4.5.18.1.2  CashOutPaymentInstrument <CshOutPmtInstrm>
Presence: [1..1]
Definition: Payment instrument for the cash-out flow.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3751 May 2026
```

## File page 3752

```text
CashOutPaymentInstrument <CshOutPmtInstrm> contains one of the following
PaymentInstrument28Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CreditTransferDetails <CdtTrfDtls> [1..1]  3755
     Reference <Ref> [0..1] Text 3758
     Debtor <Dbtr> [0..1] ± 3758
     DebtorAccount <DbtrAcct> [0..1]  3758
       Identification <Id> [1..1]  3758
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3759
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3759
Or}         Other <Othr> [1..1] ± 3759
       Name <Nm> [0..1] Text 3760
     DebtorAgent <DbtrAgt> [0..1]  3760
       Party <Pty> [1..1]  3760
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3761
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3761
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3761
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3762
       LEI <LEI> [0..1] IdentifierSet 3762
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  3763
       Identification <Id> [1..1]  3763
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3763
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3764
Or}         Other <Othr> [1..1] ± 3764
       Name <Nm> [0..1] Text 3764
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  3764
       Party <Pty> [1..1]  3765
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3765
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3765
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3766
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3767
       LEI <LEI> [0..1] IdentifierSet 3767
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3752 May 2026
```

## File page 3753

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3768
       Identification <Id> [1..1]  3768
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3768
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3769
Or}         Other <Othr> [1..1] ± 3769
       Name <Nm> [0..1] Text 3769
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  3769
       Party <Pty> [1..1]  3770
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3770
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3770
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3771
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3772
       LEI <LEI> [0..1] IdentifierSet 3772
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3773
       Identification <Id> [1..1]  3773
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3773
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3774
Or}         Other <Othr> [1..1] ± 3774
       Name <Nm> [0..1] Text 3774
     CreditorAgent <CdtrAgt> [1..1]  3774
       Party <Pty> [1..1]  3775
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3775
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3775
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3776
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3777
       LEI <LEI> [0..1] IdentifierSet 3777
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  3778
       Identification <Id> [1..1]  3778
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3778
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3779
Or}         Other <Othr> [1..1] ± 3779
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3753 May 2026
```

## File page 3754

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [0..1] Text 3779
     Creditor <Cdtr> [0..1] ± 3779
     CreditorAccount <CdtrAcct> [1..1]  3780
       Identification <Id> [1..1]  3780
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3780
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3781
Or}         Other <Othr> [1..1] ± 3781
       Name <Nm> [0..1] Text 3781
Or   ChequeDetails <ChqDtls> [1..1]  3781
     Number <Nb> [0..1] Text 3782
     PayeeIdentification <PyeeId> [1..1] ± 3782
     DraweeIdentification <DrweeId> [0..1]  3782
       Party <Pty> [1..1]  3783
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3783
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3783
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3784
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3785
       LEI <LEI> [0..1] IdentifierSet 3785
     DrawerIdentification <DrwrId> [0..1] ± 3786
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  3786
     Number <Nb> [0..1] Text 3786
     PayeeIdentification <PyeeId> [1..1] ± 3786
     DraweeIdentification <DrweeId> [0..1]  3787
       Party <Pty> [1..1]  3787
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3787
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3788
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3788
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3789
       LEI <LEI> [0..1] IdentifierSet 3789
     DrawerIdentification <DrwrId> [0..1] ± 3790
Or   CashAccountDetails <CshAcctDtls> [1..1]  C1 3790
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3754 May 2026
```

