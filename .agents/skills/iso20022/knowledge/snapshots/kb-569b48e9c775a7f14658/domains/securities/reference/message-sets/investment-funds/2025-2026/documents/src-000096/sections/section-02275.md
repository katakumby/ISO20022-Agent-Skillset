---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.34 OrderWaiverDetails <OrdrWvrDtls>"]
file_pages: [3182, 3183, 3184, 3185, 3186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.34 OrderWaiverDetails <OrdrWvrDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3182 to 3186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3182

```text
SignatureType <SgntrTp> contains one of the following elements (see "SignatureType1Choice" on
page 4845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4845
Or}   Proprietary <Prtry> [1..1] ± 4846
50.4.4.9.34  OrderWaiverDetails <OrdrWvrDtls>
Presence: [0..1]
Definition: Information about a non-standard order.
Impacted by: C39 "WaiverElementRule"
OrderWaiverDetails <OrdrWvrDtls> contains the following elements (see "OrderWaiver1" on
page 4782 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderWaiverReason <OrdrWvrRsn> [0..*]  4782
{Or     Code <Cd> [1..1] CodeSet 4782
Or}     Proprietary <Prtry> [1..1] ± 4783
   InformationValue <InfVal> [0..1] Text 4783
Constraints
• WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
50.4.4.10  BulkCashSettlementDetails <BlkCshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3182 May 2026
```

## File page 3183

```text
BulkCashSettlementDetails <BlkCshSttlmDtls> contains the following PaymentTransaction180
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  3187
{Or     PaymentCardDetails <PmtCardDtls> [1..1]  3192
       Type <Tp> [1..1] CodeSet 3193
       Number <Nb> [1..1] Text 3193
       HolderName <HldrNm> [1..1] Text 3193
       StartDate <StartDt> [0..1] YearMonth 3193
       ExpiryDate <XpryDt> [1..1] YearMonth 3193
       CardIssuerName <CardIssrNm> [0..1] Text 3193
       CardIssuerIdentification <CardIssrId> [0..1] ± 3193
       SecurityCode <SctyCd> [0..1] Text 3194
       SequenceNumber <SeqNb> [0..1] Text 3194
Or     CreditTransferDetails <CdtTrfDtls> [1..1]  3194
       Reference <Ref> [0..1] Text 3197
       Debtor <Dbtr> [0..1] ± 3197
       DebtorAccount <DbtrAcct> [0..1]  3197
         Identification <Id> [1..1]  3197
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3198
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3198
Or}           Other <Othr> [1..1] ± 3198
         Name <Nm> [0..1] Text 3199
       DebtorAgent <DbtrAgt> [0..1]  3199
         Party <Pty> [1..1]  3199
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3200
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3200
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3200
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3201
         LEI <LEI> [0..1] IdentifierSet 3201
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  3202
         Identification <Id> [1..1]  3202
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3202
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3183 May 2026
```

## File page 3184

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3203
Or}           Other <Othr> [1..1] ± 3203
         Name <Nm> [0..1] Text 3203
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  3203
         Party <Pty> [1..1]  3204
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3204
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3204
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3205
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3206
         LEI <LEI> [0..1] IdentifierSet 3206
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3207
         Identification <Id> [1..1]  3207
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3207
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3208
Or}           Other <Othr> [1..1] ± 3208
         Name <Nm> [0..1] Text 3208
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  3208
         Party <Pty> [1..1]  3209
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3209
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3209
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3210
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3211
         LEI <LEI> [0..1] IdentifierSet 3211
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3212
         Identification <Id> [1..1]  3212
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3212
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3213
Or}           Other <Othr> [1..1] ± 3213
         Name <Nm> [0..1] Text 3213
       CreditorAgent <CdtrAgt> [1..1]  3213
         Party <Pty> [1..1]  3214
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3184 May 2026
```

## File page 3185

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3214
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3214
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3215
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3216
         LEI <LEI> [0..1] IdentifierSet 3216
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  3217
         Identification <Id> [1..1]  3217
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3217
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3218
Or}           Other <Othr> [1..1] ± 3218
         Name <Nm> [0..1] Text 3218
       Creditor <Cdtr> [0..1] ± 3218
       CreditorAccount <CdtrAcct> [1..1]  3219
         Identification <Id> [1..1]  3219
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3219
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3220
Or}           Other <Othr> [1..1] ± 3220
         Name <Nm> [0..1] Text 3220
Or     DirectDebitDetails <DrctDbtDtls> [1..1]  3220
       DebtorAccount <DbtrAcct> [1..1]  3221
         Identification <Id> [1..1]  3222
{Or           IBAN <IBAN> [1..1] IdentifierSet C20 3222
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3222
Or}           Other <Othr> [1..1] ± 3223
         Name <Nm> [0..1] Text 3223
       Debtor <Dbtr> [0..1] ± 3223
       DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3223
       DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3224
       Creditor <Cdtr> [0..1] ± 3224
       DebtorAgent <DbtrAgt> [1..1]  3224
         Party <Pty> [1..1]  3224
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3185 May 2026
```

## File page 3186

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3225
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3225
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3225
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3226
         LEI <LEI> [0..1] IdentifierSet 3226
       DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3227
       CreditorAgent <CdtrAgt> [0..1]  3227
         Party <Pty> [1..1]  3227
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3228
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3228
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3228
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3229
         LEI <LEI> [0..1] IdentifierSet 3229
       CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3230
       RegistrationIdentification <RegnId> [0..1] Text 3230
       MandateIdentification <MndtId> [0..1] Text 3230
Or     ChequeDetails <ChqDtls> [1..1]  3230
       Number <Nb> [0..1] Text 3231
       PayeeIdentification <PyeeId> [1..1] ± 3231
       DraweeIdentification <DrweeId> [0..1]  3231
         Party <Pty> [1..1]  3232
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3232
Or           BICFI <BICFI> [1..1] IdentifierSet C6 3232
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3233
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3234
         LEI <LEI> [0..1] IdentifierSet 3234
       DrawerIdentification <DrwrId> [0..1] ± 3235
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  3235
       Number <Nb> [0..1] Text 3235
       PayeeIdentification <PyeeId> [1..1] ± 3235
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3186 May 2026
```

