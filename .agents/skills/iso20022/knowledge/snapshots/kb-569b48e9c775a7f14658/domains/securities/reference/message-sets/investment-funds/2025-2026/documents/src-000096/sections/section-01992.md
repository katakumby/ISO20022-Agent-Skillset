---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# Continuation at file page 2797

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2797 to 2804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2797

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Name <Nm> [0..1] Text 2907
           Creditor <Cdtr> [0..1] ± 2907
           CreditorAccount <CdtrAcct> [1..1]  2908
             Identification <Id> [1..1]  2908
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2908
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2909
Or}               Other <Othr> [1..1] ± 2909
             Name <Nm> [0..1] Text 2909
Or         DirectDebitDetails <DrctDbtDtls> [1..1]  2909
           DebtorAccount <DbtrAcct> [1..1]  2910
             Identification <Id> [1..1]  2911
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2911
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2911
Or}               Other <Othr> [1..1] ± 2912
             Name <Nm> [0..1] Text 2912
           Debtor <Dbtr> [0..1] ± 2912
           DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2912
           DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2913
           Creditor <Cdtr> [0..1] ± 2913
           DebtorAgent <DbtrAgt> [1..1]  2913
             Party <Pty> [1..1]  2913
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2914
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2914
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2914
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2915
             LEI <LEI> [0..1] IdentifierSet 2915
           DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2916
           CreditorAgent <CdtrAgt> [0..1]  2916
             Party <Pty> [1..1]  2916
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2917
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2917
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2797 May 2026
```

## File page 2798

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2917
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2918
             LEI <LEI> [0..1] IdentifierSet 2918
           CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2919
           RegistrationIdentification <RegnId> [0..1] Text 2919
           MandateIdentification <MndtId> [0..1] Text 2919
Or         ChequeDetails <ChqDtls> [1..1]  2919
           Number <Nb> [0..1] Text 2920
           PayeeIdentification <PyeeId> [1..1] ± 2920
           DraweeIdentification <DrweeId> [0..1]  2920
             Party <Pty> [1..1]  2921
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2921
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2921
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2922
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2923
             LEI <LEI> [0..1] IdentifierSet 2923
           DrawerIdentification <DrwrId> [0..1] ± 2924
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  2924
           Number <Nb> [0..1] Text 2924
           PayeeIdentification <PyeeId> [1..1] ± 2924
           DraweeIdentification <DrweeId> [0..1]  2925
             Party <Pty> [1..1]  2925
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2925
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2926
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2926
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2927
             LEI <LEI> [0..1] IdentifierSet 2927
           DrawerIdentification <DrwrId> [0..1] ± 2928
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 2928
           AccountIdentification <AcctId> [0..1] Text 2928
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2798 May 2026
```

## File page 2799

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [0..1] ± 2928
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  2929
           Identification <Id> [1..1] Text 2929
           Type <Tp> [0..1] ± 2929
           Name <Nm> [0..1] Text 2929
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2930
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2930
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2930
         ISIN <ISIN> [0..1] IdentifierSet 2932
         OtherIdentification <OthrId> [0..*]  2932
           Identification <Id> [1..1] Text 2932
           Suffix <Sfx> [0..1] Text 2932
           Type <Tp> [1..1]  2932
{Or             Code <Cd> [1..1] CodeSet 2933
Or}             Proprietary <Prtry> [1..1] Text 2934
         Description <Desc> [0..1] Text 2934
       Quantity <Qty> [1..1]  2935
{Or         Quantity <Qty> [1..1] ± C16 2935
Or}         ProprietaryQuantity <PrtryQty> [1..1]  2935
           Quantity <Qty> [1..1] Quantity 2936
           QuantityType <QtyTp> [1..1] Text 2936
           Issuer <Issr> [1..1] Text 2936
           SchemeName <SchmeNm> [0..1] Text 2936
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2936
     NonStandardSettlementInformation
<NonStdSttlmInf>
[0..1] Text 2936
     PartialSettlementOfUnits <PrtlSttlmOfUnits> [0..1] Rate 2936
     FinancialAdvice <FinAdvc> [0..1] CodeSet 2937
     NegotiatedTrade <NgtdTrad> [0..1] CodeSet 2937
     LateReport <LateRpt> [0..1] CodeSet 2937
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2799 May 2026
```

## File page 2800

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PartialSettlementOfCash <PrtlSttlmOfCsh> [0..1] Rate 2937
     RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 2937
     Equalisation <Equlstn> [0..1] ± 2938
     SourceOfCash <SrcOfCsh> [0..*] ± 2938
     CustomerConductClassification
<CstmrCndctClssfctn>
[0..1] ± 2939
     TransactionChannelType <TxChanlTp> [0..1] ± 2939
     SignatureType <SgntrTp> [0..1] ± 2939
     OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C40 2939
   RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 2940
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 2940
   TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 2940
   BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  2941
     PaymentInstrument <PmtInstrm> [1..1]  2946
{Or       PaymentCardDetails <PmtCardDtls> [1..1]  2951
         Type <Tp> [1..1] CodeSet 2952
         Number <Nb> [1..1] Text 2952
         HolderName <HldrNm> [1..1] Text 2952
         StartDate <StartDt> [0..1] YearMonth 2952
         ExpiryDate <XpryDt> [1..1] YearMonth 2952
         CardIssuerName <CardIssrNm> [0..1] Text 2952
         CardIssuerIdentification <CardIssrId> [0..1] ± 2952
         SecurityCode <SctyCd> [0..1] Text 2953
         SequenceNumber <SeqNb> [0..1] Text 2953
Or       CreditTransferDetails <CdtTrfDtls> [1..1]  2953
         Reference <Ref> [0..1] Text 2956
         Debtor <Dbtr> [0..1] ± 2956
         DebtorAccount <DbtrAcct> [0..1]  2956
           Identification <Id> [1..1]  2956
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2957
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2957
Or}             Other <Othr> [1..1] ± 2957
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2800 May 2026
```

## File page 2801

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Name <Nm> [0..1] Text 2958
         DebtorAgent <DbtrAgt> [0..1]  2958
           Party <Pty> [1..1]  2958
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2959
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2959
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2959
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2960
           LEI <LEI> [0..1] IdentifierSet 2960
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  2961
           Identification <Id> [1..1]  2961
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2961
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2962
Or}             Other <Othr> [1..1] ± 2962
           Name <Nm> [0..1] Text 2962
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  2962
           Party <Pty> [1..1]  2963
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2963
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2963
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2964
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2965
           LEI <LEI> [0..1] IdentifierSet 2965
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2966
           Identification <Id> [1..1]  2966
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2966
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2967
Or}             Other <Othr> [1..1] ± 2967
           Name <Nm> [0..1] Text 2967
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  2967
           Party <Pty> [1..1]  2968
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2968
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2968
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2801 May 2026
```

## File page 2802

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2969
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2970
           LEI <LEI> [0..1] IdentifierSet 2970
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2971
           Identification <Id> [1..1]  2971
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2971
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2972
Or}             Other <Othr> [1..1] ± 2972
           Name <Nm> [0..1] Text 2972
         CreditorAgent <CdtrAgt> [1..1]  2972
           Party <Pty> [1..1]  2973
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2973
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2973
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2974
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2975
           LEI <LEI> [0..1] IdentifierSet 2975
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  2976
           Identification <Id> [1..1]  2976
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2976
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2977
Or}             Other <Othr> [1..1] ± 2977
           Name <Nm> [0..1] Text 2977
         Creditor <Cdtr> [0..1] ± 2977
         CreditorAccount <CdtrAcct> [1..1]  2978
           Identification <Id> [1..1]  2978
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2978
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2979
Or}             Other <Othr> [1..1] ± 2979
           Name <Nm> [0..1] Text 2979
Or       DirectDebitDetails <DrctDbtDtls> [1..1]  2979
         DebtorAccount <DbtrAcct> [1..1]  2980
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2802 May 2026
```

## File page 2803

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  2981
{Or             IBAN <IBAN> [1..1] IdentifierSet C19 2981
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2981
Or}             Other <Othr> [1..1] ± 2982
           Name <Nm> [0..1] Text 2982
         Debtor <Dbtr> [0..1] ± 2982
         DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 2982
         DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 2983
         Creditor <Cdtr> [0..1] ± 2983
         DebtorAgent <DbtrAgt> [1..1]  2983
           Party <Pty> [1..1]  2983
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2984
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2984
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2984
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2985
           LEI <LEI> [0..1] IdentifierSet 2985
         DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 2986
         CreditorAgent <CdtrAgt> [0..1]  2986
           Party <Pty> [1..1]  2986
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2987
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2987
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2987
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2988
           LEI <LEI> [0..1] IdentifierSet 2988
         CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 2989
         RegistrationIdentification <RegnId> [0..1] Text 2989
         MandateIdentification <MndtId> [0..1] Text 2989
Or       ChequeDetails <ChqDtls> [1..1]  2989
         Number <Nb> [0..1] Text 2990
         PayeeIdentification <PyeeId> [1..1] ± 2990
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2803 May 2026
```

## File page 2804

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DraweeIdentification <DrweeId> [0..1]  2990
           Party <Pty> [1..1]  2991
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2991
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2991
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2992
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2993
           LEI <LEI> [0..1] IdentifierSet 2993
         DrawerIdentification <DrwrId> [0..1] ± 2994
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  2994
         Number <Nb> [0..1] Text 2994
         PayeeIdentification <PyeeId> [1..1] ± 2994
         DraweeIdentification <DrweeId> [0..1]  2995
           Party <Pty> [1..1]  2995
{Or             NameAndAddress <NmAndAdr> [1..1] ± 2995
Or             BICFI <BICFI> [1..1] IdentifierSet C7 2996
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2996
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2997
           LEI <LEI> [0..1] IdentifierSet 2997
         DrawerIdentification <DrwrId> [0..1] ± 2998
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 2998
         AccountIdentification <AcctId> [0..1] Text 2998
         Type <Tp> [0..1] ± 2998
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  2999
         Identification <Id> [1..1] Text 2999
         Type <Tp> [0..1] ± 2999
         Name <Nm> [0..1] Text 2999
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3000
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2804 May 2026
```

