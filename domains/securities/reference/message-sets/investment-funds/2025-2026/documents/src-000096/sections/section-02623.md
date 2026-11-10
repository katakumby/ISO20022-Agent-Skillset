---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [3681, 3682, 3683, 3684, 3685, 3686, 3687, 3688]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3681 to 3688.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3681

```text
Definition: Part of an investor's subscription amount that is held by the fund in order to pay incentive/
performance fees at the end of the fiscal year.
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
53.4.5.18  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3681 May 2026
```

## File page 3682

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction181 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInOrOut <CshInOrOut> [1..1]  3689
{Or     CashInPaymentInstrument <CshInPmtInstrm> [1..1]  3697
{Or       PaymentCardDetails <PmtCardDtls> [1..1]  3702
         Type <Tp> [1..1] CodeSet 3703
         Number <Nb> [1..1] Text 3703
         HolderName <HldrNm> [1..1] Text 3703
         StartDate <StartDt> [0..1] YearMonth 3703
         ExpiryDate <XpryDt> [1..1] YearMonth 3703
         CardIssuerName <CardIssrNm> [0..1] Text 3703
         CardIssuerIdentification <CardIssrId> [0..1] ± 3703
         SecurityCode <SctyCd> [0..1] Text 3704
         SequenceNumber <SeqNb> [0..1] Text 3704
Or       CreditTransferDetails <CdtTrfDtls> [1..1]  3704
         Reference <Ref> [0..1] Text 3707
         Debtor <Dbtr> [0..1] ± 3707
         DebtorAccount <DbtrAcct> [0..1]  3707
           Identification <Id> [1..1]  3707
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3708
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3708
Or}             Other <Othr> [1..1] ± 3708
           Name <Nm> [0..1] Text 3709
         DebtorAgent <DbtrAgt> [0..1]  3709
           Party <Pty> [1..1]  3709
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3710
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3710
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3710
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3711
           LEI <LEI> [0..1] IdentifierSet 3711
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  3712
           Identification <Id> [1..1]  3712
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3682 May 2026
```

## File page 3683

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3712
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3713
Or}             Other <Othr> [1..1] ± 3713
           Name <Nm> [0..1] Text 3713
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  3713
           Party <Pty> [1..1]  3714
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3714
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3714
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3715
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3716
           LEI <LEI> [0..1] IdentifierSet 3716
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3717
           Identification <Id> [1..1]  3717
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3717
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3718
Or}             Other <Othr> [1..1] ± 3718
           Name <Nm> [0..1] Text 3718
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  3718
           Party <Pty> [1..1]  3719
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3719
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3719
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3720
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3721
           LEI <LEI> [0..1] IdentifierSet 3721
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3722
           Identification <Id> [1..1]  3722
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3722
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3723
Or}             Other <Othr> [1..1] ± 3723
           Name <Nm> [0..1] Text 3723
         CreditorAgent <CdtrAgt> [1..1]  3723
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3683 May 2026
```

## File page 3684

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Party <Pty> [1..1]  3724
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3724
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3724
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3725
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3726
           LEI <LEI> [0..1] IdentifierSet 3726
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  3727
           Identification <Id> [1..1]  3727
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3727
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3728
Or}             Other <Othr> [1..1] ± 3728
           Name <Nm> [0..1] Text 3728
         Creditor <Cdtr> [0..1] ± 3728
         CreditorAccount <CdtrAcct> [1..1]  3729
           Identification <Id> [1..1]  3729
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3729
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3730
Or}             Other <Othr> [1..1] ± 3730
           Name <Nm> [0..1] Text 3730
Or       DirectDebitDetails <DrctDbtDtls> [1..1]  3730
         DebtorAccount <DbtrAcct> [1..1]  3731
           Identification <Id> [1..1]  3732
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3732
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3732
Or}             Other <Othr> [1..1] ± 3733
           Name <Nm> [0..1] Text 3733
         Debtor <Dbtr> [0..1] ± 3733
         DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3733
         DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3734
         Creditor <Cdtr> [0..1] ± 3734
         DebtorAgent <DbtrAgt> [1..1]  3734
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3684 May 2026
```

## File page 3685

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Party <Pty> [1..1]  3734
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3735
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3735
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3735
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3736
           LEI <LEI> [0..1] IdentifierSet 3736
         DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3737
         CreditorAgent <CdtrAgt> [0..1]  3737
           Party <Pty> [1..1]  3737
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3738
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3738
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3738
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3739
           LEI <LEI> [0..1] IdentifierSet 3739
         CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3740
         RegistrationIdentification <RegnId> [0..1] Text 3740
         MandateIdentification <MndtId> [0..1] Text 3740
Or       ChequeDetails <ChqDtls> [1..1]  3740
         Number <Nb> [0..1] Text 3741
         PayeeIdentification <PyeeId> [1..1] ± 3741
         DraweeIdentification <DrweeId> [0..1]  3741
           Party <Pty> [1..1]  3742
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3742
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3742
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3743
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3744
           LEI <LEI> [0..1] IdentifierSet 3744
         DrawerIdentification <DrwrId> [0..1] ± 3745
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  3745
         Number <Nb> [0..1] Text 3745
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3685 May 2026
```

## File page 3686

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PayeeIdentification <PyeeId> [1..1] ± 3745
         DraweeIdentification <DrweeId> [0..1]  3746
           Party <Pty> [1..1]  3746
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3746
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3747
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3747
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3748
           LEI <LEI> [0..1] IdentifierSet 3748
         DrawerIdentification <DrwrId> [0..1] ± 3749
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 3749
         AccountIdentification <AcctId> [0..1] Text 3749
         Type <Tp> [0..1] ± 3749
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  3750
         Identification <Id> [1..1] Text 3750
         Type <Tp> [0..1] ± 3750
         Name <Nm> [0..1] Text 3750
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3751
Or}     CashOutPaymentInstrument <CshOutPmtInstrm> [1..1]  3751
{Or       CreditTransferDetails <CdtTrfDtls> [1..1]  3755
         Reference <Ref> [0..1] Text 3758
         Debtor <Dbtr> [0..1] ± 3758
         DebtorAccount <DbtrAcct> [0..1]  3758
           Identification <Id> [1..1]  3758
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3759
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3759
Or}             Other <Othr> [1..1] ± 3759
           Name <Nm> [0..1] Text 3760
         DebtorAgent <DbtrAgt> [0..1]  3760
           Party <Pty> [1..1]  3760
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3761
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3761
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3686 May 2026
```

## File page 3687

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3761
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3762
           LEI <LEI> [0..1] IdentifierSet 3762
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  3763
           Identification <Id> [1..1]  3763
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3763
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3764
Or}             Other <Othr> [1..1] ± 3764
           Name <Nm> [0..1] Text 3764
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  3764
           Party <Pty> [1..1]  3765
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3765
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3765
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3766
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3767
           LEI <LEI> [0..1] IdentifierSet 3767
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3768
           Identification <Id> [1..1]  3768
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3768
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3769
Or}             Other <Othr> [1..1] ± 3769
           Name <Nm> [0..1] Text 3769
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  3769
           Party <Pty> [1..1]  3770
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3770
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3770
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3771
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3772
           LEI <LEI> [0..1] IdentifierSet 3772
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3773
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3687 May 2026
```

## File page 3688

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  3773
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3773
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3774
Or}             Other <Othr> [1..1] ± 3774
           Name <Nm> [0..1] Text 3774
         CreditorAgent <CdtrAgt> [1..1]  3774
           Party <Pty> [1..1]  3775
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3775
Or             BICFI <BICFI> [1..1] IdentifierSet C5 3775
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3776
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3777
           LEI <LEI> [0..1] IdentifierSet 3777
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  3778
           Identification <Id> [1..1]  3778
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3778
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3779
Or}             Other <Othr> [1..1] ± 3779
           Name <Nm> [0..1] Text 3779
         Creditor <Cdtr> [0..1] ± 3779
         CreditorAccount <CdtrAcct> [1..1]  3780
           Identification <Id> [1..1]  3780
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 3780
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3781
Or}             Other <Othr> [1..1] ± 3781
           Name <Nm> [0..1] Text 3781
Or       ChequeDetails <ChqDtls> [1..1]  3781
         Number <Nb> [0..1] Text 3782
         PayeeIdentification <PyeeId> [1..1] ± 3782
         DraweeIdentification <DrweeId> [0..1]  3782
           Party <Pty> [1..1]  3783
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3783
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3688 May 2026
```

