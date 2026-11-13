---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>"]
file_pages: [3187, 3188, 3189, 3190, 3191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1 PaymentInstrument <PmtInstrm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3187 to 3191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3187

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DraweeIdentification <DrweeId> [0..1]  3236
         Party <Pty> [1..1]  3236
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3236
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3237
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3237
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3238
         LEI <LEI> [0..1] IdentifierSet 3238
       DrawerIdentification <DrwrId> [0..1] ± 3239
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 3239
       AccountIdentification <AcctId> [0..1] Text 3239
       Type <Tp> [0..1] ± 3239
Or}     BlockChainCashWallet <BlckChainCshWllt> [1..1]  3240
       Identification <Id> [1..1] Text 3240
       Type <Tp> [0..1] ± 3240
       Name <Nm> [0..1] Text 3240
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3241
50.4.4.10.1  PaymentInstrument <PmtInstrm>
Presence: [1..1]
Definition: Choice between types of payment instrument, for example, cheque, credit transfer, direct
debit, investment account or payment card.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3187 May 2026
```

## File page 3188

```text
PaymentInstrument <PmtInstrm> contains one of the following PaymentInstrument29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentCardDetails <PmtCardDtls> [1..1]  3192
     Type <Tp> [1..1] CodeSet 3193
     Number <Nb> [1..1] Text 3193
     HolderName <HldrNm> [1..1] Text 3193
     StartDate <StartDt> [0..1] YearMonth 3193
     ExpiryDate <XpryDt> [1..1] YearMonth 3193
     CardIssuerName <CardIssrNm> [0..1] Text 3193
     CardIssuerIdentification <CardIssrId> [0..1] ± 3193
     SecurityCode <SctyCd> [0..1] Text 3194
     SequenceNumber <SeqNb> [0..1] Text 3194
Or   CreditTransferDetails <CdtTrfDtls> [1..1]  3194
     Reference <Ref> [0..1] Text 3197
     Debtor <Dbtr> [0..1] ± 3197
     DebtorAccount <DbtrAcct> [0..1]  3197
       Identification <Id> [1..1]  3197
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3198
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3198
Or}         Other <Othr> [1..1] ± 3198
       Name <Nm> [0..1] Text 3199
     DebtorAgent <DbtrAgt> [0..1]  3199
       Party <Pty> [1..1]  3199
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3200
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3200
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3200
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3201
       LEI <LEI> [0..1] IdentifierSet 3201
     DebtorAgentAccount <DbtrAgtAcct> [0..1]  3202
       Identification <Id> [1..1]  3202
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3202
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3203
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3188 May 2026
```

## File page 3189

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Other <Othr> [1..1] ± 3203
       Name <Nm> [0..1] Text 3203
     IntermediaryAgent1 <IntrmyAgt1> [0..1]  3203
       Party <Pty> [1..1]  3204
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3204
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3204
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3205
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3206
       LEI <LEI> [0..1] IdentifierSet 3206
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3207
       Identification <Id> [1..1]  3207
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3207
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3208
Or}         Other <Othr> [1..1] ± 3208
       Name <Nm> [0..1] Text 3208
     IntermediaryAgent2 <IntrmyAgt2> [0..1]  3208
       Party <Pty> [1..1]  3209
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3209
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3209
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3210
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3211
       LEI <LEI> [0..1] IdentifierSet 3211
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3212
       Identification <Id> [1..1]  3212
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3212
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3213
Or}         Other <Othr> [1..1] ± 3213
       Name <Nm> [0..1] Text 3213
     CreditorAgent <CdtrAgt> [1..1]  3213
       Party <Pty> [1..1]  3214
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3214
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3189 May 2026
```

## File page 3190

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3215
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3216
       LEI <LEI> [0..1] IdentifierSet 3216
     CreditorAgentAccount <CdtrAgtAcct> [0..1]  3217
       Identification <Id> [1..1]  3217
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3217
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3218
Or}         Other <Othr> [1..1] ± 3218
       Name <Nm> [0..1] Text 3218
     Creditor <Cdtr> [0..1] ± 3218
     CreditorAccount <CdtrAcct> [1..1]  3219
       Identification <Id> [1..1]  3219
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3219
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3220
Or}         Other <Othr> [1..1] ± 3220
       Name <Nm> [0..1] Text 3220
Or   DirectDebitDetails <DrctDbtDtls> [1..1]  3220
     DebtorAccount <DbtrAcct> [1..1]  3221
       Identification <Id> [1..1]  3222
{Or         IBAN <IBAN> [1..1] IdentifierSet C20 3222
Or         BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3222
Or}         Other <Othr> [1..1] ± 3223
       Name <Nm> [0..1] Text 3223
     Debtor <Dbtr> [0..1] ± 3223
     DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3223
     DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3224
     Creditor <Cdtr> [0..1] ± 3224
     DebtorAgent <DbtrAgt> [1..1]  3224
       Party <Pty> [1..1]  3224
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3225
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3190 May 2026
```

## File page 3191

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3225
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3225
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3226
       LEI <LEI> [0..1] IdentifierSet 3226
     DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3227
     CreditorAgent <CdtrAgt> [0..1]  3227
       Party <Pty> [1..1]  3227
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3228
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3228
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3228
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3229
       LEI <LEI> [0..1] IdentifierSet 3229
     CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3230
     RegistrationIdentification <RegnId> [0..1] Text 3230
     MandateIdentification <MndtId> [0..1] Text 3230
Or   ChequeDetails <ChqDtls> [1..1]  3230
     Number <Nb> [0..1] Text 3231
     PayeeIdentification <PyeeId> [1..1] ± 3231
     DraweeIdentification <DrweeId> [0..1]  3231
       Party <Pty> [1..1]  3232
{Or         NameAndAddress <NmAndAdr> [1..1] ± 3232
Or         BICFI <BICFI> [1..1] IdentifierSet C6 3232
Or         ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3233
Or}         ProprietaryIdentification <PrtryId> [1..1] Text 3234
       LEI <LEI> [0..1] IdentifierSet 3234
     DrawerIdentification <DrwrId> [0..1] ± 3235
Or   BankersDraftDetails <BkrsDrftDtls> [1..1]  3235
     Number <Nb> [0..1] Text 3235
     PayeeIdentification <PyeeId> [1..1] ± 3235
     DraweeIdentification <DrweeId> [0..1]  3236
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3191 May 2026
```

