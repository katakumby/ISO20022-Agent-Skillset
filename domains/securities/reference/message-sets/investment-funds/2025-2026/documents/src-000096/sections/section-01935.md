---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "47.4.4.12.1 PaymentInstrument <PmtInstrm>"]
file_pages: [2706, 2707, 2708, 2709, 2710]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.12.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2706 to 2710.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2706

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  2755
         Party <Pty> [1..1]  2755
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2755
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2756
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2756
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2757
         LEI <LEI> [0..1] IdentifierSet 2757
       DrawerIdentification <DrwrId> [0..1] ± 2758
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2758
       AccountIdentification <AcctId> [0..1] Text 2758
       Type <Tp> [0..1] ± 2758
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  2759
       Identification <Id> [1..1] Text 2759
       Type <Tp> [0..1] ± 2759
       Name <Nm> [0..1] Text 2759
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2760
47.4.4.12.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer, direct
debit, investment account or payment card.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2706 May 2026
```

## File page 2707

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  2711
     Type <Tp> [1..1] CodeSet 2712
     Number <Nb> [1..1] Text 2712
     HolderName <HldrNm> [1..1] Text 2712
     StartDate <StartDt> [0..1] YearMonth 2712
     ExpiryDate <XpryDt> [1..1] YearMonth 2712
     CardIssuerName <CardIssrNm> [0..1] Text 2712
     CardIssuerIdentification <CardIssrId> [0..1] ± 2712
     SecurityCode <SctyCd> [0..1] Text 2713
     SequenceNumber <SeqNb> [0..1] Text 2713
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  2713
     Reference <Ref> [0..1] Text 2716
     Debtor <Dbtr> [0..1] ± 2716
     DebtorAccount <DbtrAcct> [0..1]  2716
       Identification <Id> [1..1]  2716
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2717
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2717
Or}         Other <Othr> [1..1] ± 2717
       Name <Nm> [0..1] Text 2718
     DebtorAgent <DbtrAgt> [0..1]  2718
       Party <Pty> [1..1]  2718
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2719
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2719
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2719
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2720
       LEI <LEI> [0..1] IdentifierSet 2720
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  2721
       Identification <Id> [1..1]  2721
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2721
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2722
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2707 May 2026
```

## File page 2708

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 2722
       Name <Nm> [0..1] Text 2722
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  2722
       Party <Pty> [1..1]  2723
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2723
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2723
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2724
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2725
       LEI <LEI> [0..1] IdentifierSet 2725
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2726
       Identification <Id> [1..1]  2726
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2726
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2727
Or}         Other <Othr> [1..1] ± 2727
       Name <Nm> [0..1] Text 2727
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  2727
       Party <Pty> [1..1]  2728
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2728
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2728
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2729
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2730
       LEI <LEI> [0..1] IdentifierSet 2730
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2731
       Identification <Id> [1..1]  2731
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2731
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2732
Or}         Other <Othr> [1..1] ± 2732
       Name <Nm> [0..1] Text 2732
     CreditorAgent <CdtrAgt> [1..1]  2732
       Party <Pty> [1..1]  2733
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2733
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2708 May 2026
```

## File page 2709

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2733
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2734
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2735
       LEI <LEI> [0..1] IdentifierSet 2735
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  2736
       Identification <Id> [1..1]  2736
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2736
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2737
Or}         Other <Othr> [1..1] ± 2737
       Name <Nm> [0..1] Text 2737
     Creditor <Cdtr> [0..1] ± 2737
     CreditorAccount <CdtrAcct> [1..1]  2738
       Identification <Id> [1..1]  2738
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2738
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2739
Or}         Other <Othr> [1..1] ± 2739
       Name <Nm> [0..1] Text 2739
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  2739
     DebtorAccount <DbtrAcct> [1..1]  2740
       Identification <Id> [1..1]  2741
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2741
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2741
Or}         Other <Othr> [1..1] ± 2742
       Name <Nm> [0..1] Text 2742
     Debtor <Dbtr> [0..1] ± 2742
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2742
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2743
     Creditor <Cdtr> [0..1] ± 2743
     DebtorAgent <DbtrAgt> [1..1]  2743
       Party <Pty> [1..1]  2743
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2744
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2709 May 2026
```

## File page 2710

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2744
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2744
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2745
       LEI <LEI> [0..1] IdentifierSet 2745
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2746
     CreditorAgent <CdtrAgt> [0..1]  2746
       Party <Pty> [1..1]  2746
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2747
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2747
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2747
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2748
       LEI <LEI> [0..1] IdentifierSet 2748
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2749
     RegistrationIdentification <RegnId> [0..1] Text 2749
     MandateIdentification <MndtId> [0..1] Text 2749
Or   ChequeDetails <ChqDtls> [1..1]  2749
     Number <Nb> [0..1] Text 2750
     PayeeIdentification <PyeeId> [1..1] ± 2750
     DraweeIdentification <DrweeId> [0..1]  2750
       Party <Pty> [1..1]  2751
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2751
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2751
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2752
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2753
       LEI <LEI> [0..1] IdentifierSet 2753
     DrawerIdentification <DrwrId> [0..1] ± 2754
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  2754
     Number <Nb> [0..1] Text 2754
     PayeeIdentification <PyeeId> [1..1] ± 2754
     DraweeIdentification <DrweeId> [0..1]  2755
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2710 May 2026
```

