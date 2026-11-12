---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>"]
file_pages: [3697, 3698, 3699, 3700, 3701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.1 CashInPaymentInstrument <CshInPmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3697 to 3701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3697

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3785
         LEI <LEI> [0..1] IdentifierSet 3785
       DrawerIdentification <DrwrId> [0..1] ± 3786
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  3786
       Number <Nb> [0..1] Text 3786
       PayeeIdentification <PyeeId> [1..1] ± 3786
       DraweeIdentification <DrweeId> [0..1]  3787
         Party <Pty> [1..1]  3787
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3787
Or           BICFI <BICFI> [1..1] IdentifierSet C5 3788
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3788
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3789
         LEI <LEI> [0..1] IdentifierSet 3789
       DrawerIdentification <DrwrId> [0..1] ± 3790
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 3790
       AccountIdentification <AcctId> [0..1] Text 3790
       Type <Tp> [0..1] ± 3790
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  3791
       Identification <Id> [1..1] Text 3791
       Type <Tp> [0..1] ± 3791
       Name <Nm> [0..1] Text 3791
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3792
53.4.5.18.1.1  CashInPaymentInstrument <CshInPmtInstrm>
Presence: [1..1]
Definition: Payment instrument for the cash-in flow.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3697 May 2026
```

## File page 3698

```text
CashInPaymentInstrument <CshInPmtInstrm> contains one of the following
PaymentInstrument30Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  3702
     Type <Tp> [1..1] CodeSet 3703
     Number <Nb> [1..1] Text 3703
     HolderName <HldrNm> [1..1] Text 3703
     StartDate <StartDt> [0..1] YearMonth 3703
     ExpiryDate <XpryDt> [1..1] YearMonth 3703
     CardIssuerName <CardIssrNm> [0..1] Text 3703
     CardIssuerIdentification <CardIssrId> [0..1] ± 3703
     SecurityCode <SctyCd> [0..1] Text 3704
     SequenceNumber <SeqNb> [0..1] Text 3704
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  3704
     Reference <Ref> [0..1] Text 3707
     Debtor <Dbtr> [0..1] ± 3707
     DebtorAccount <DbtrAcct> [0..1]  3707
       Identification <Id> [1..1]  3707
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3708
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3708
Or}         Other <Othr> [1..1] ± 3708
       Name <Nm> [0..1] Text 3709
     DebtorAgent <DbtrAgt> [0..1]  3709
       Party <Pty> [1..1]  3709
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3710
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3710
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3710
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3711
       LEI <LEI> [0..1] IdentifierSet 3711
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  3712
       Identification <Id> [1..1]  3712
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3698 May 2026
```

## File page 3699

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 3713
       Name <Nm> [0..1] Text 3713
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  3713
       Party <Pty> [1..1]  3714
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3714
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3714
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3715
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3716
       LEI <LEI> [0..1] IdentifierSet 3716
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3717
       Identification <Id> [1..1]  3717
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3717
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3718
Or}         Other <Othr> [1..1] ± 3718
       Name <Nm> [0..1] Text 3718
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  3718
       Party <Pty> [1..1]  3719
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3719
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3719
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3720
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3721
       LEI <LEI> [0..1] IdentifierSet 3721
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3722
       Identification <Id> [1..1]  3722
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3722
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3723
Or}         Other <Othr> [1..1] ± 3723
       Name <Nm> [0..1] Text 3723
     CreditorAgent <CdtrAgt> [1..1]  3723
       Party <Pty> [1..1]  3724
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3724
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3699 May 2026
```

## File page 3700

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3724
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3725
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3726
       LEI <LEI> [0..1] IdentifierSet 3726
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  3727
       Identification <Id> [1..1]  3727
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3727
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3728
Or}         Other <Othr> [1..1] ± 3728
       Name <Nm> [0..1] Text 3728
     Creditor <Cdtr> [0..1] ± 3728
     CreditorAccount <CdtrAcct> [1..1]  3729
       Identification <Id> [1..1]  3729
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3729
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3730
Or}         Other <Othr> [1..1] ± 3730
       Name <Nm> [0..1] Text 3730
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  3730
     DebtorAccount <DbtrAcct> [1..1]  3731
       Identification <Id> [1..1]  3732
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 3732
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3732
Or}         Other <Othr> [1..1] ± 3733
       Name <Nm> [0..1] Text 3733
     Debtor <Dbtr> [0..1] ± 3733
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3733
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3734
     Creditor <Cdtr> [0..1] ± 3734
     DebtorAgent <DbtrAgt> [1..1]  3734
       Party <Pty> [1..1]  3734
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3735
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3700 May 2026
```

## File page 3701

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3735
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3735
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3736
       LEI <LEI> [0..1] IdentifierSet 3736
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3737
     CreditorAgent <CdtrAgt> [0..1]  3737
       Party <Pty> [1..1]  3737
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3738
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3738
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3738
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3739
       LEI <LEI> [0..1] IdentifierSet 3739
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3740
     RegistrationIdentification <RegnId> [0..1] Text 3740
     MandateIdentification <MndtId> [0..1] Text 3740
Or   ChequeDetails <ChqDtls> [1..1]  3740
     Number <Nb> [0..1] Text 3741
     PayeeIdentification <PyeeId> [1..1] ± 3741
     DraweeIdentification <DrweeId> [0..1]  3741
       Party <Pty> [1..1]  3742
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3742
Or         BICFI <BICFI> [1..1] IdentifierSet C5 3742
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3743
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3744
       LEI <LEI> [0..1] IdentifierSet 3744
     DrawerIdentification <DrwrId> [0..1] ± 3745
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  3745
     Number <Nb> [0..1] Text 3745
     PayeeIdentification <PyeeId> [1..1] ± 3745
     DraweeIdentification <DrweeId> [0..1]  3746
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3701 May 2026
```

