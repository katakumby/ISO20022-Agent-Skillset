---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [2413, 2414, 2415, 2416]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2413 to 2416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2413

```text
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C4 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
46.4.5.10.33  CashSettlementDetails <CshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2413 May 2026
```

## File page 2414

```text
CashSettlementDetails <CshSttlmDtls> contains the following PaymentTransaction167 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  2417
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  2421
       Reference <Ref> [0..1] Text 2424
       Debtor <Dbtr> [0..1] ± 2424
       DebtorAccount <DbtrAcct> [0..1]  2424
         Identification <Id> [1..1]  2424
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2425
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2425
Or}           Other <Othr> [1..1] ± 2425
         Name <Nm> [0..1] Text 2426
       DebtorAgent <DbtrAgt> [0..1]  2426
         Party <Pty> [1..1]  2426
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2427
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2427
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2427
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2428
         LEI <LEI> [0..1] IdentifierSet 2428
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  2429
         Identification <Id> [1..1]  2429
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2429
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2430
Or}           Other <Othr> [1..1] ± 2430
         Name <Nm> [0..1] Text 2430
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  2430
         Party <Pty> [1..1]  2431
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2431
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2431
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2432
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2433
         LEI <LEI> [0..1] IdentifierSet 2433
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2414 May 2026
```

## File page 2415

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2434
         Identification <Id> [1..1]  2434
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2434
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2435
Or}           Other <Othr> [1..1] ± 2435
         Name <Nm> [0..1] Text 2435
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  2435
         Party <Pty> [1..1]  2436
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2436
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2436
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2437
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2438
         LEI <LEI> [0..1] IdentifierSet 2438
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2439
         Identification <Id> [1..1]  2439
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2439
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2440
Or}           Other <Othr> [1..1] ± 2440
         Name <Nm> [0..1] Text 2440
       CreditorAgent <CdtrAgt> [1..1]  2440
         Party <Pty> [1..1]  2441
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2441
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2441
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2442
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2443
         LEI <LEI> [0..1] IdentifierSet 2443
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  2444
         Identification <Id> [1..1]  2444
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2444
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2445
Or}           Other <Othr> [1..1] ± 2445
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2415 May 2026
```

## File page 2416

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 2445
       Creditor <Cdtr> [0..1] ± 2445
       CreditorAccount <CdtrAcct> [1..1]  2446
         Identification <Id> [1..1]  2446
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2446
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2447
Or}           Other <Othr> [1..1] ± 2447
         Name <Nm> [0..1] Text 2447
Or     ChequeDetails <ChqDtls> [1..1]  2447
       Number <Nb> [0..1] Text 2448
       PayeeIdentification <PyeeId> [1..1] ± 2448
       DraweeIdentification <DrweeId> [0..1]  2448
         Party <Pty> [1..1]  2449
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2449
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2449
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2450
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2451
         LEI <LEI> [0..1] IdentifierSet 2451
       DrawerIdentification <DrwrId> [0..1] ± 2452
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  2452
       Number <Nb> [0..1] Text 2452
       PayeeIdentification <PyeeId> [1..1] ± 2452
       DraweeIdentification <DrweeId> [0..1]  2453
         Party <Pty> [1..1]  2453
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2453
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2454
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2454
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2455
         LEI <LEI> [0..1] IdentifierSet 2455
       DrawerIdentification <DrwrId> [0..1] ± 2456
Or     CashAccountDetails <CshAcctDtls> [1..1]  C1 2456
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2416 May 2026
```

