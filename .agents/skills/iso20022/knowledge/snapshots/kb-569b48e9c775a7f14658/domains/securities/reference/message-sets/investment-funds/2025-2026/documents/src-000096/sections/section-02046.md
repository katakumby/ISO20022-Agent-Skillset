---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>"]
file_pages: [2876, 2877, 2878, 2879, 2880]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2876 to 2880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2876

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  2925
         Party <Pty> [1..1]  2925
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2925
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2926
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2926
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2927
         LEI <LEI> [0..1] IdentifierSet 2927
       DrawerIdentification <DrwrId> [0..1] ± 2928
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2928
       AccountIdentification <AcctId> [0..1] Text 2928
       Type <Tp> [0..1] ± 2928
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  2929
       Identification <Id> [1..1] Text 2929
       Type <Tp> [0..1] ± 2929
       Name <Nm> [0..1] Text 2929
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2930
49.4.5.9.34.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer, direct
debit, investment account or payment card.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2876 May 2026
```

## File page 2877

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  2881
     Type <Tp> [1..1] CodeSet 2882
     Number <Nb> [1..1] Text 2882
     HolderName <HldrNm> [1..1] Text 2882
     StartDate <StartDt> [0..1] YearMonth 2882
     ExpiryDate <XpryDt> [1..1] YearMonth 2882
     CardIssuerName <CardIssrNm> [0..1] Text 2882
     CardIssuerIdentification <CardIssrId> [0..1] ± 2882
     SecurityCode <SctyCd> [0..1] Text 2883
     SequenceNumber <SeqNb> [0..1] Text 2883
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  2883
     Reference <Ref> [0..1] Text 2886
     Debtor <Dbtr> [0..1] ± 2886
     DebtorAccount <DbtrAcct> [0..1]  2886
       Identification <Id> [1..1]  2886
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2887
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2887
Or}         Other <Othr> [1..1] ± 2887
       Name <Nm> [0..1] Text 2888
     DebtorAgent <DbtrAgt> [0..1]  2888
       Party <Pty> [1..1]  2888
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2889
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2889
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2889
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2890
       LEI <LEI> [0..1] IdentifierSet 2890
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  2891
       Identification <Id> [1..1]  2891
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2891
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2892
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2877 May 2026
```

## File page 2878

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 2892
       Name <Nm> [0..1] Text 2892
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  2892
       Party <Pty> [1..1]  2893
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2893
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2893
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2894
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2895
       LEI <LEI> [0..1] IdentifierSet 2895
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2896
       Identification <Id> [1..1]  2896
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2896
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2897
Or}         Other <Othr> [1..1] ± 2897
       Name <Nm> [0..1] Text 2897
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  2897
       Party <Pty> [1..1]  2898
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2898
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2898
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2899
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2900
       LEI <LEI> [0..1] IdentifierSet 2900
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2901
       Identification <Id> [1..1]  2901
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2901
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2902
Or}         Other <Othr> [1..1] ± 2902
       Name <Nm> [0..1] Text 2902
     CreditorAgent <CdtrAgt> [1..1]  2902
       Party <Pty> [1..1]  2903
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2903
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2878 May 2026
```

## File page 2879

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2903
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2904
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2905
       LEI <LEI> [0..1] IdentifierSet 2905
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  2906
       Identification <Id> [1..1]  2906
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2906
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2907
Or}         Other <Othr> [1..1] ± 2907
       Name <Nm> [0..1] Text 2907
     Creditor <Cdtr> [0..1] ± 2907
     CreditorAccount <CdtrAcct> [1..1]  2908
       Identification <Id> [1..1]  2908
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2908
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2909
Or}         Other <Othr> [1..1] ± 2909
       Name <Nm> [0..1] Text 2909
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  2909
     DebtorAccount <DbtrAcct> [1..1]  2910
       Identification <Id> [1..1]  2911
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2911
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2911
Or}         Other <Othr> [1..1] ± 2912
       Name <Nm> [0..1] Text 2912
     Debtor <Dbtr> [0..1] ± 2912
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2912
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2913
     Creditor <Cdtr> [0..1] ± 2913
     DebtorAgent <DbtrAgt> [1..1]  2913
       Party <Pty> [1..1]  2913
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2914
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2879 May 2026
```

## File page 2880

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2914
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2914
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2915
       LEI <LEI> [0..1] IdentifierSet 2915
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2916
     CreditorAgent <CdtrAgt> [0..1]  2916
       Party <Pty> [1..1]  2916
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2917
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2917
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2917
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2918
       LEI <LEI> [0..1] IdentifierSet 2918
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2919
     RegistrationIdentification <RegnId> [0..1] Text 2919
     MandateIdentification <MndtId> [0..1] Text 2919
Or   ChequeDetails <ChqDtls> [1..1]  2919
     Number <Nb> [0..1] Text 2920
     PayeeIdentification <PyeeId> [1..1] ± 2920
     DraweeIdentification <DrweeId> [0..1]  2920
       Party <Pty> [1..1]  2921
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2921
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2921
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2922
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2923
       LEI <LEI> [0..1] IdentifierSet 2923
     DrawerIdentification <DrwrId> [0..1] ± 2924
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  2924
     Number <Nb> [0..1] Text 2924
     PayeeIdentification <PyeeId> [1..1] ± 2924
     DraweeIdentification <DrweeId> [0..1]  2925
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2880 May 2026
```

