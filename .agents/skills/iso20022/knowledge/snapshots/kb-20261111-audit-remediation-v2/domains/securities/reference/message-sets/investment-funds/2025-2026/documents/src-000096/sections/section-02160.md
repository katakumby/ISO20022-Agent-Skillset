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
file_pages: [3032, 3033, 3034, 3035, 3036, 3037, 3038]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# Continuation at file page 3032

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3032 to 3038.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3032

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3155
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3156
             LEI <LEI> [0..1] IdentifierSet 3156
           DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3157
           CreditorAgent <CdtrAgt> [0..1]  3157
             Party <Pty> [1..1]  3157
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3158
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3158
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3158
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3159
             LEI <LEI> [0..1] IdentifierSet 3159
           CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3160
           RegistrationIdentification <RegnId> [0..1] Text 3160
           MandateIdentification <MndtId> [0..1] Text 3160
Or         ChequeDetails <ChqDtls> [1..1]  3160
           Number <Nb> [0..1] Text 3161
           PayeeIdentification <PyeeId> [1..1] ± 3161
           DraweeIdentification <DrweeId> [0..1]  3161
             Party <Pty> [1..1]  3162
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3162
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3162
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3163
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3164
             LEI <LEI> [0..1] IdentifierSet 3164
           DrawerIdentification <DrwrId> [0..1] ± 3165
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  3165
           Number <Nb> [0..1] Text 3165
           PayeeIdentification <PyeeId> [1..1] ± 3165
           DraweeIdentification <DrweeId> [0..1]  3166
             Party <Pty> [1..1]  3166
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3032 May 2026
```

## File page 3033

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3166
Or               BICFI <BICFI> [1..1] IdentifierSet C6 3167
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3167
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3168
             LEI <LEI> [0..1] IdentifierSet 3168
           DrawerIdentification <DrwrId> [0..1] ± 3169
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 3169
           AccountIdentification <AcctId> [0..1] Text 3169
           Type <Tp> [0..1] ± 3169
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  3170
           Identification <Id> [1..1] Text 3170
           Type <Tp> [0..1] ± 3170
           Name <Nm> [0..1] Text 3170
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3171
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3171
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
3171
         ISIN <ISIN> [0..1] IdentifierSet 3173
         OtherIdentification <OthrId> [0..*]  3173
           Identification <Id> [1..1] Text 3173
           Suffix <Sfx> [0..1] Text 3173
           Type <Tp> [1..1]  3173
{Or             Code <Cd> [1..1] CodeSet 3174
Or}             Proprietary <Prtry> [1..1] Text 3175
         Description <Desc> [0..1] Text 3175
       Quantity <Qty> [1..1]  3176
{Or         Quantity <Qty> [1..1] ± C15 3176
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3176
           Quantity <Qty> [1..1] Quantity 3177
           QuantityType <QtyTp> [1..1] Text 3177
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3033 May 2026
```

## File page 3034

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Issuer <Issr> [1..1] Text 3177
           SchemeName <SchmeNm> [0..1] Text 3177
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3177
     NonStandardSettlementInformation
<NonStdSttlmInf>
[0..1] Text 3177
     StaffClientBreakdown <StffClntBrkdwn> [0..4] ± 3177
     FinancialAdvice <FinAdvc> [0..1] CodeSet 3178
     NegotiatedTrade <NgtdTrad> [0..1] CodeSet 3178
     RelatedPartyDetails <RltdPtyDtls> [0..10]  C24 3178
       Identification <Id> [1..1] ± 3179
       Account <Acct> [0..1]  3179
         Identification <Id> [1..1] Text 3179
         AccountServicer <AcctSvcr> [0..1] ± 3180
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3180
       Role <Role> [0..1] ± 3180
     Equalisation <Equlstn> [0..1] ± 3180
     SourceOfCash <SrcOfCsh> [0..*] ± 3181
     CustomerConductClassification
<CstmrCndctClssfctn>
[0..1] ± 3181
     TransactionChannelType <TxChanlTp> [0..1] ± 3181
     SignatureType <SgntrTp> [0..1] ± 3181
     OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C39 3182
   BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  3182
     PaymentInstrument <PmtInstrm> [1..1]  3187
{Or       PaymentCardDetails <PmtCardDtls> [1..1]  3192
         Type <Tp> [1..1] CodeSet 3193
         Number <Nb> [1..1] Text 3193
         HolderName <HldrNm> [1..1] Text 3193
         StartDate <StartDt> [0..1] YearMonth 3193
         ExpiryDate <XpryDt> [1..1] YearMonth 3193
         CardIssuerName <CardIssrNm> [0..1] Text 3193
         CardIssuerIdentification <CardIssrId> [0..1] ± 3193
         SecurityCode <SctyCd> [0..1] Text 3194
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3034 May 2026
```

## File page 3035

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SequenceNumber <SeqNb> [0..1] Text 3194
Or       CreditTransferDetails <CdtTrfDtls> [1..1]  3194
         Reference <Ref> [0..1] Text 3197
         Debtor <Dbtr> [0..1] ± 3197
         DebtorAccount <DbtrAcct> [0..1]  3197
           Identification <Id> [1..1]  3197
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3198
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3198
Or}             Other <Othr> [1..1] ± 3198
           Name <Nm> [0..1] Text 3199
         DebtorAgent <DbtrAgt> [0..1]  3199
           Party <Pty> [1..1]  3199
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3200
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3200
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3200
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3201
           LEI <LEI> [0..1] IdentifierSet 3201
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  3202
           Identification <Id> [1..1]  3202
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3202
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3203
Or}             Other <Othr> [1..1] ± 3203
           Name <Nm> [0..1] Text 3203
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  3203
           Party <Pty> [1..1]  3204
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3204
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3204
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3205
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3206
           LEI <LEI> [0..1] IdentifierSet 3206
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3207
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3035 May 2026
```

## File page 3036

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  3207
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3207
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3208
Or}             Other <Othr> [1..1] ± 3208
           Name <Nm> [0..1] Text 3208
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  3208
           Party <Pty> [1..1]  3209
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3209
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3209
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3210
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3211
           LEI <LEI> [0..1] IdentifierSet 3211
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3212
           Identification <Id> [1..1]  3212
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3212
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3213
Or}             Other <Othr> [1..1] ± 3213
           Name <Nm> [0..1] Text 3213
         CreditorAgent <CdtrAgt> [1..1]  3213
           Party <Pty> [1..1]  3214
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3214
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3215
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3216
           LEI <LEI> [0..1] IdentifierSet 3216
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  3217
           Identification <Id> [1..1]  3217
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3217
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3218
Or}             Other <Othr> [1..1] ± 3218
           Name <Nm> [0..1] Text 3218
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3036 May 2026
```

## File page 3037

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Creditor <Cdtr> [0..1] ± 3218
         CreditorAccount <CdtrAcct> [1..1]  3219
           Identification <Id> [1..1]  3219
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3219
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3220
Or}             Other <Othr> [1..1] ± 3220
           Name <Nm> [0..1] Text 3220
Or       DirectDebitDetails <DrctDbtDtls> [1..1]  3220
         DebtorAccount <DbtrAcct> [1..1]  3221
           Identification <Id> [1..1]  3222
{Or             IBAN <IBAN> [1..1] IdentifierSet C20 3222
Or             BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3222
Or}             Other <Othr> [1..1] ± 3223
           Name <Nm> [0..1] Text 3223
         Debtor <Dbtr> [0..1] ± 3223
         DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3223
         DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3224
         Creditor <Cdtr> [0..1] ± 3224
         DebtorAgent <DbtrAgt> [1..1]  3224
           Party <Pty> [1..1]  3224
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3225
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3225
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3225
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3226
           LEI <LEI> [0..1] IdentifierSet 3226
         DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3227
         CreditorAgent <CdtrAgt> [0..1]  3227
           Party <Pty> [1..1]  3227
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3228
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3228
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3037 May 2026
```

## File page 3038

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3228
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3229
           LEI <LEI> [0..1] IdentifierSet 3229
         CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3230
         RegistrationIdentification <RegnId> [0..1] Text 3230
         MandateIdentification <MndtId> [0..1] Text 3230
Or       ChequeDetails <ChqDtls> [1..1]  3230
         Number <Nb> [0..1] Text 3231
         PayeeIdentification <PyeeId> [1..1] ± 3231
         DraweeIdentification <DrweeId> [0..1]  3231
           Party <Pty> [1..1]  3232
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3232
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3232
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3233
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3234
           LEI <LEI> [0..1] IdentifierSet 3234
         DrawerIdentification <DrwrId> [0..1] ± 3235
Or       BankersDraftDetails <BkrsDrftDtls> [1..1]  3235
         Number <Nb> [0..1] Text 3235
         PayeeIdentification <PyeeId> [1..1] ± 3235
         DraweeIdentification <DrweeId> [0..1]  3236
           Party <Pty> [1..1]  3236
{Or             NameAndAddress <NmAndAdr> [1..1] ± 3236
Or             BICFI <BICFI> [1..1] IdentifierSet C6 3237
Or             ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3237
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 3238
           LEI <LEI> [0..1] IdentifierSet 3238
         DrawerIdentification <DrwrId> [0..1] ± 3239
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 3239
         AccountIdentification <AcctId> [0..1] Text 3239
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3038 May 2026
```

