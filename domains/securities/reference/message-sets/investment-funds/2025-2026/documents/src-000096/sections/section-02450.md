---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.11 TotalSettlementAmount <TtlSttlmAmt>"]
file_pages: [3427, 3428, 3429, 3430, 3431]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.11 TotalSettlementAmount <TtlSttlmAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3427 to 3431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3427

```text
Impacted by: C44 "WaiverElementRule"
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
52.4.5.11  TotalSettlementAmount <TtlSttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the multiple order.
Impacted by: C3 "ActiveCurrency", C11 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
52.4.5.12  BulkCashSettlementDetails <BlkCshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3427 May 2026
```

## File page 3428

```text
BulkCashSettlementDetails <BlkCshSttlmDtls> contains the following PaymentTransaction180
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  3432
{Or     PaymentCardDetails <PmtCardDtls> [1..1]  3437
       Type <Tp> [1..1] CodeSet 3438
       Number <Nb> [1..1] Text 3438
       HolderName <HldrNm> [1..1] Text 3438
       StartDate <StartDt> [0..1] YearMonth 3438
       ExpiryDate <XpryDt> [1..1] YearMonth 3438
       CardIssuerName <CardIssrNm> [0..1] Text 3438
       CardIssuerIdentification <CardIssrId> [0..1] ± 3438
       SecurityCode <SctyCd> [0..1] Text 3439
       SequenceNumber <SeqNb> [0..1] Text 3439
Or     CreditTransferDetails <CdtTrfDtls> [1..1]  3439
       Reference <Ref> [0..1] Text 3442
       Debtor <Dbtr> [0..1] ± 3442
       DebtorAccount <DbtrAcct> [0..1]  3442
         Identification <Id> [1..1]  3442
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3443
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3443
Or}           Other <Othr> [1..1] ± 3443
         Name <Nm> [0..1] Text 3444
       DebtorAgent <DbtrAgt> [0..1]  3444
         Party <Pty> [1..1]  3444
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3445
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3445
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3445
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3446
         LEI <LEI> [0..1] IdentifierSet 3446
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  3447
         Identification <Id> [1..1]  3447
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3447
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3428 May 2026
```

## File page 3429

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3448
Or}           Other <Othr> [1..1] ± 3448
         Name <Nm> [0..1] Text 3448
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  3448
         Party <Pty> [1..1]  3449
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3449
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3449
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3450
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3451
         LEI <LEI> [0..1] IdentifierSet 3451
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3452
         Identification <Id> [1..1]  3452
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3452
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3453
Or}           Other <Othr> [1..1] ± 3453
         Name <Nm> [0..1] Text 3453
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  3453
         Party <Pty> [1..1]  3454
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3454
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3454
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3455
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3456
         LEI <LEI> [0..1] IdentifierSet 3456
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3457
         Identification <Id> [1..1]  3457
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3457
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3458
Or}           Other <Othr> [1..1] ± 3458
         Name <Nm> [0..1] Text 3458
       CreditorAgent <CdtrAgt> [1..1]  3458
         Party <Pty> [1..1]  3459
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3429 May 2026
```

## File page 3430

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3459
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3459
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3460
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3461
         LEI <LEI> [0..1] IdentifierSet 3461
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  3462
         Identification <Id> [1..1]  3462
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3462
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3463
Or}           Other <Othr> [1..1] ± 3463
         Name <Nm> [0..1] Text 3463
       Creditor <Cdtr> [0..1] ± 3463
       CreditorAccount <CdtrAcct> [1..1]  3464
         Identification <Id> [1..1]  3464
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3464
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3465
Or}           Other <Othr> [1..1] ± 3465
         Name <Nm> [0..1] Text 3465
Or     DirectDebitDetails <DrctDbtDtls> [1..1]  3465
       DebtorAccount <DbtrAcct> [1..1]  3466
         Identification <Id> [1..1]  3467
{Or           IBAN <IBAN> [1..1] IdentifierSet C22 3467
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3467
Or}           Other <Othr> [1..1] ± 3468
         Name <Nm> [0..1] Text 3468
       Debtor <Dbtr> [0..1] ± 3468
       DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3468
       DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3469
       Creditor <Cdtr> [0..1] ± 3469
       DebtorAgent <DbtrAgt> [1..1]  3469
         Party <Pty> [1..1]  3469
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3430 May 2026
```

## File page 3431

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3470
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3470
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3470
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3471
         LEI <LEI> [0..1] IdentifierSet 3471
       DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3472
       CreditorAgent <CdtrAgt> [0..1]  3472
         Party <Pty> [1..1]  3472
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3473
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3473
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3473
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3474
         LEI <LEI> [0..1] IdentifierSet 3474
       CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 3475
       RegistrationIdentification <RegnId> [0..1] Text 3475
       MandateIdentification <MndtId> [0..1] Text 3475
Or     ChequeDetails <ChqDtls> [1..1]  3475
       Number <Nb> [0..1] Text 3476
       PayeeIdentification <PyeeId> [1..1] ± 3476
       DraweeIdentification <DrweeId> [0..1]  3476
         Party <Pty> [1..1]  3477
{Or           NameAndAddress <NmAndAdr> [1..1] ± 3477
Or           BICFI <BICFI> [1..1] IdentifierSet C7 3477
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3478
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 3479
         LEI <LEI> [0..1] IdentifierSet 3479
       DrawerIdentification <DrwrId> [0..1] ± 3480
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  3480
       Number <Nb> [0..1] Text 3480
       PayeeIdentification <PyeeId> [1..1] ± 3480
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3431 May 2026
```

