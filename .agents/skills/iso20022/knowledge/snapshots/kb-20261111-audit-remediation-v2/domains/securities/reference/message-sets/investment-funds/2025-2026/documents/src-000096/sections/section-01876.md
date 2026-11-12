---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>"]
file_pages: [2636, 2637, 2638, 2639, 2640]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2636 to 2640.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2636

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  2685
         Party <Pty> [1..1]  2685
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2685
Or           BICFI <BICFI> [1..1] IdentifierSet C6 2686
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2686
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2687
         LEI <LEI> [0..1] IdentifierSet 2687
       DrawerIdentification <DrwrId> [0..1] ± 2688
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2688
       AccountIdentification <AcctId> [0..1] Text 2688
       Type <Tp> [0..1] ± 2688
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  2689
       Identification <Id> [1..1] Text 2689
       Type <Tp> [0..1] ± 2689
       Name <Nm> [0..1] Text 2689
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2690
47.4.4.8.20.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer, direct
debit, investment account or payment card.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2636 May 2026
```

## File page 2637

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  2641
     Type <Tp> [1..1] CodeSet 2642
     Number <Nb> [1..1] Text 2642
     HolderName <HldrNm> [1..1] Text 2642
     StartDate <StartDt> [0..1] YearMonth 2642
     ExpiryDate <XpryDt> [1..1] YearMonth 2642
     CardIssuerName <CardIssrNm> [0..1] Text 2642
     CardIssuerIdentification <CardIssrId> [0..1] ± 2642
     SecurityCode <SctyCd> [0..1] Text 2643
     SequenceNumber <SeqNb> [0..1] Text 2643
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  2643
     Reference <Ref> [0..1] Text 2646
     Debtor <Dbtr> [0..1] ± 2646
     DebtorAccount <DbtrAcct> [0..1]  2646
       Identification <Id> [1..1]  2646
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2647
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2647
Or}         Other <Othr> [1..1] ± 2647
       Name <Nm> [0..1] Text 2648
     DebtorAgent <DbtrAgt> [0..1]  2648
       Party <Pty> [1..1]  2648
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2649
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2649
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2649
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2650
       LEI <LEI> [0..1] IdentifierSet 2650
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  2651
       Identification <Id> [1..1]  2651
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2651
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2652
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2637 May 2026
```

## File page 2638

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 2652
       Name <Nm> [0..1] Text 2652
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  2652
       Party <Pty> [1..1]  2653
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2653
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2653
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2654
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2655
       LEI <LEI> [0..1] IdentifierSet 2655
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2656
       Identification <Id> [1..1]  2656
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2656
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2657
Or}         Other <Othr> [1..1] ± 2657
       Name <Nm> [0..1] Text 2657
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  2657
       Party <Pty> [1..1]  2658
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2658
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2658
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2659
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2660
       LEI <LEI> [0..1] IdentifierSet 2660
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2661
       Identification <Id> [1..1]  2661
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2661
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2662
Or}         Other <Othr> [1..1] ± 2662
       Name <Nm> [0..1] Text 2662
     CreditorAgent <CdtrAgt> [1..1]  2662
       Party <Pty> [1..1]  2663
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2663
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2638 May 2026
```

## File page 2639

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2663
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2664
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2665
       LEI <LEI> [0..1] IdentifierSet 2665
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  2666
       Identification <Id> [1..1]  2666
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2666
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2667
Or}         Other <Othr> [1..1] ± 2667
       Name <Nm> [0..1] Text 2667
     Creditor <Cdtr> [0..1] ± 2667
     CreditorAccount <CdtrAcct> [1..1]  2668
       Identification <Id> [1..1]  2668
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2668
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2669
Or}         Other <Othr> [1..1] ± 2669
       Name <Nm> [0..1] Text 2669
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  2669
     DebtorAccount <DbtrAcct> [1..1]  2670
       Identification <Id> [1..1]  2671
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 2671
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2671
Or}         Other <Othr> [1..1] ± 2672
       Name <Nm> [0..1] Text 2672
     Debtor <Dbtr> [0..1] ± 2672
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2672
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2673
     Creditor <Cdtr> [0..1] ± 2673
     DebtorAgent <DbtrAgt> [1..1]  2673
       Party <Pty> [1..1]  2673
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2674
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2639 May 2026
```

## File page 2640

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2674
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2674
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2675
       LEI <LEI> [0..1] IdentifierSet 2675
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2676
     CreditorAgent <CdtrAgt> [0..1]  2676
       Party <Pty> [1..1]  2676
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2677
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2677
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2677
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2678
       LEI <LEI> [0..1] IdentifierSet 2678
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2679
     RegistrationIdentification <RegnId> [0..1] Text 2679
     MandateIdentification <MndtId> [0..1] Text 2679
Or   ChequeDetails <ChqDtls> [1..1]  2679
     Number <Nb> [0..1] Text 2680
     PayeeIdentification <PyeeId> [1..1] ± 2680
     DraweeIdentification <DrweeId> [0..1]  2680
       Party <Pty> [1..1]  2681
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2681
Or         BICFI <BICFI> [1..1] IdentifierSet C6 2681
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2682
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2683
       LEI <LEI> [0..1] IdentifierSet 2683
     DrawerIdentification <DrwrId> [0..1] ± 2684
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  2684
     Number <Nb> [0..1] Text 2684
     PayeeIdentification <PyeeId> [1..1] ± 2684
     DraweeIdentification <DrweeId> [0..1]  2685
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2640 May 2026
```

