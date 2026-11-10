---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>"]
file_pages: [2946, 2947, 2948, 2949, 2950]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2946 to 2950.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2946

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  2995
         Party <Pty> [1..1]  2995
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2995
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2996
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2996
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2997
         LEI <LEI> [0..1] IdentifierSet 2997
       DrawerIdentification <DrwrId> [0..1] ± 2998
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2998
       AccountIdentification <AcctId> [0..1] Text 2998
       Type <Tp> [0..1] ± 2998
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  2999
       Identification <Id> [1..1] Text 2999
       Type <Tp> [0..1] ± 2999
       Name <Nm> [0..1] Text 2999
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3000
49.4.5.13.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer, direct
debit, investment account or payment card.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2946 May 2026
```

## File page 2947

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  2951
     Type <Tp> [1..1] CodeSet 2952
     Number <Nb> [1..1] Text 2952
     HolderName <HldrNm> [1..1] Text 2952
     StartDate <StartDt> [0..1] YearMonth 2952
     ExpiryDate <XpryDt> [1..1] YearMonth 2952
     CardIssuerName <CardIssrNm> [0..1] Text 2952
     CardIssuerIdentification <CardIssrId> [0..1] ± 2952
     SecurityCode <SctyCd> [0..1] Text 2953
     SequenceNumber <SeqNb> [0..1] Text 2953
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  2953
     Reference <Ref> [0..1] Text 2956
     Debtor <Dbtr> [0..1] ± 2956
     DebtorAccount <DbtrAcct> [0..1]  2956
       Identification <Id> [1..1]  2956
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2957
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2957
Or}         Other <Othr> [1..1] ± 2957
       Name <Nm> [0..1] Text 2958
     DebtorAgent <DbtrAgt> [0..1]  2958
       Party <Pty> [1..1]  2958
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2959
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2959
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2959
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2960
       LEI <LEI> [0..1] IdentifierSet 2960
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  2961
       Identification <Id> [1..1]  2961
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2961
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2962
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2947 May 2026
```

## File page 2948

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 2962
       Name <Nm> [0..1] Text 2962
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  2962
       Party <Pty> [1..1]  2963
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2963
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2963
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2964
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2965
       LEI <LEI> [0..1] IdentifierSet 2965
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2966
       Identification <Id> [1..1]  2966
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2966
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2967
Or}         Other <Othr> [1..1] ± 2967
       Name <Nm> [0..1] Text 2967
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  2967
       Party <Pty> [1..1]  2968
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2968
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2968
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2969
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2970
       LEI <LEI> [0..1] IdentifierSet 2970
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2971
       Identification <Id> [1..1]  2971
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2971
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2972
Or}         Other <Othr> [1..1] ± 2972
       Name <Nm> [0..1] Text 2972
     CreditorAgent <CdtrAgt> [1..1]  2972
       Party <Pty> [1..1]  2973
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2973
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2948 May 2026
```

## File page 2949

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2973
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2974
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2975
       LEI <LEI> [0..1] IdentifierSet 2975
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  2976
       Identification <Id> [1..1]  2976
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2976
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2977
Or}         Other <Othr> [1..1] ± 2977
       Name <Nm> [0..1] Text 2977
     Creditor <Cdtr> [0..1] ± 2977
     CreditorAccount <CdtrAcct> [1..1]  2978
       Identification <Id> [1..1]  2978
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2978
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2979
Or}         Other <Othr> [1..1] ± 2979
       Name <Nm> [0..1] Text 2979
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  2979
     DebtorAccount <DbtrAcct> [1..1]  2980
       Identification <Id> [1..1]  2981
{Or         IBAN <IBAN> [1..1] IdentifierSet C19 2981
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2981
Or}         Other <Othr> [1..1] ± 2982
       Name <Nm> [0..1] Text 2982
     Debtor <Dbtr> [0..1] ± 2982
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2982
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2983
     Creditor <Cdtr> [0..1] ± 2983
     DebtorAgent <DbtrAgt> [1..1]  2983
       Party <Pty> [1..1]  2983
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2984
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2949 May 2026
```

## File page 2950

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2984
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2984
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2985
       LEI <LEI> [0..1] IdentifierSet 2985
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2986
     CreditorAgent <CdtrAgt> [0..1]  2986
       Party <Pty> [1..1]  2986
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2987
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2987
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2987
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2988
       LEI <LEI> [0..1] IdentifierSet 2988
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2989
     RegistrationIdentification <RegnId> [0..1] Text 2989
     MandateIdentification <MndtId> [0..1] Text 2989
Or   ChequeDetails <ChqDtls> [1..1]  2989
     Number <Nb> [0..1] Text 2990
     PayeeIdentification <PyeeId> [1..1] ± 2990
     DraweeIdentification <DrweeId> [0..1]  2990
       Party <Pty> [1..1]  2991
{Or         NameAndAddress <NmAndAdr> [1..1] ± 2991
Or         BICFI <BICFI> [1..1] IdentifierSet C7 2991
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2992
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 2993
       LEI <LEI> [0..1] IdentifierSet 2993
     DrawerIdentification <DrwrId> [0..1] ± 2994
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  2994
     Number <Nb> [0..1] Text 2994
     PayeeIdentification <PyeeId> [1..1] ± 2994
     DraweeIdentification <DrweeId> [0..1]  2995
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2950 May 2026
```

