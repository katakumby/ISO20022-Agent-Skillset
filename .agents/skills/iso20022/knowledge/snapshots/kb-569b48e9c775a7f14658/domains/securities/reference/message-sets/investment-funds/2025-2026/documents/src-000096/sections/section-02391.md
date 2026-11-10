---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [3357, 3358, 3359, 3360, 3361]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3357 to 3361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3357

```text
Note: The decimal separator is a dot.
52.4.5.10.35  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3357 May 2026
```

## File page 3358

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction180 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  3362
{Or     PaymentCardDetails <PmtCardDtls> [1..1]  3367
       Type <Tp> [1..1] CodeSet 3368
       Number <Nb> [1..1] Text 3368
       HolderName <HldrNm> [1..1] Text 3368
       StartDate <StartDt> [0..1] YearMonth 3368
       ExpiryDate <XpryDt> [1..1] YearMonth 3368
       CardIssuerName <CardIssrNm> [0..1] Text 3368
       CardIssuerIdentification <CardIssrId> [0..1] ± 3368
       SecurityCode <SctyCd> [0..1] Text 3369
       SequenceNumber <SeqNb> [0..1] Text 3369
Or     CreditTransferDetails <CdtTrfDtls> [1..1]  3369
       Reference <Ref> [0..1] Text 3372
       Debtor <Dbtr> [0..1] ± 3372
       DebtorAccount <DbtrAcct> [0..1]  3372
         Identification <Id> [1..1]  3372
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3373
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3373
Or}           Other <Othr> [1..1] ± 3373
         Name <Nm> [0..1] Text 3374
       DebtorAgent <DbtrAgt> [0..1]  3374
         Party <Pty> [1..1]  3374
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3375
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3375
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3375
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3376
         LEI <LEI> [0..1] IdentifierSet 3376
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  3377
         Identification <Id> [1..1]  3377
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3377
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3358 May 2026
```

## File page 3359

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3378
Or}           Other <Othr> [1..1] ± 3378
         Name <Nm> [0..1] Text 3378
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  3378
         Party <Pty> [1..1]  3379
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3379
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3379
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3380
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3381
         LEI <LEI> [0..1] IdentifierSet 3381
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3382
         Identification <Id> [1..1]  3382
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3382
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3383
Or}           Other <Othr> [1..1] ± 3383
         Name <Nm> [0..1] Text 3383
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  3383
         Party <Pty> [1..1]  3384
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3384
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3384
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3385
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3386
         LEI <LEI> [0..1] IdentifierSet 3386
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3387
         Identification <Id> [1..1]  3387
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3387
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3388
Or}           Other <Othr> [1..1] ± 3388
         Name <Nm> [0..1] Text 3388
       CreditorAgent <CdtrAgt> [1..1]  3388
         Party <Pty> [1..1]  3389
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3359 May 2026
```

## File page 3360

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3389
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3389
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3390
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3391
         LEI <LEI> [0..1] IdentifierSet 3391
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  3392
         Identification <Id> [1..1]  3392
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3392
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3393
Or}           Other <Othr> [1..1] ± 3393
         Name <Nm> [0..1] Text 3393
       Creditor <Cdtr> [0..1] ± 3393
       CreditorAccount <CdtrAcct> [1..1]  3394
         Identification <Id> [1..1]  3394
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3394
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3395
Or}           Other <Othr> [1..1] ± 3395
         Name <Nm> [0..1] Text 3395
Or     DirectDebitDetails <DrctDbtDtls> [1..1]  3395
       DebtorAccount <DbtrAcct> [1..1]  3396
         Identification <Id> [1..1]  3397
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3397
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3397
Or}           Other <Othr> [1..1] ± 3398
         Name <Nm> [0..1] Text 3398
       Debtor <Dbtr> [0..1] ± 3398
       DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3398
       DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3399
       Creditor <Cdtr> [0..1] ± 3399
       DebtorAgent <DbtrAgt> [1..1]  3399
         Party <Pty> [1..1]  3399
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3360 May 2026
```

## File page 3361

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3400
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3400
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3400
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3401
         LEI <LEI> [0..1] IdentifierSet 3401
       DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3402
       CreditorAgent <CdtrAgt> [0..1]  3402
         Party <Pty> [1..1]  3402
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3403
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3403
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3403
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3404
         LEI <LEI> [0..1] IdentifierSet 3404
       CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3405
       RegistrationIdentification <RegnId> [0..1] Text 3405
       MandateIdentification <MndtId> [0..1] Text 3405
Or     ChequeDetails <ChqDtls> [1..1]  3405
       Number <Nb> [0..1] Text 3406
       PayeeIdentification <PyeeId> [1..1] ± 3406
       DraweeIdentification <DrweeId> [0..1]  3406
         Party <Pty> [1..1]  3407
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3407
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3407
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3408
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3409
         LEI <LEI> [0..1] IdentifierSet 3409
       DrawerIdentification <DrwrId> [0..1] ± 3410
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  3410
       Number <Nb> [0..1] Text 3410
       PayeeIdentification <PyeeId> [1..1] ± 3410
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3361 May 2026
```

