---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.11 TotalSettlementAmount <TtlSttlmAmt>"]
file_pages: [2477, 2478, 2479, 2480]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.11 TotalSettlementAmount <TtlSttlmAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2477 to 2480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2477

```text
46.4.5.11  TotalSettlementAmount <TtlSttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the multiple order.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
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
46.4.5.12  BulkCashSettlementDetails <BlkCshSttlmDtls>
Presence: [0..1]
Definition: Payment process for the transfer of cash from the debtor to the creditor.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2477 May 2026
```

## File page 2478

```text
BulkCashSettlementDetails <BlkCshSttlmDtls> contains the following PaymentTransaction167
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstrument <PmtInstrm> [1..1]  2481
{Or     CreditTransferDetails <CdtTrfDtls> [1..1]  2485
       Reference <Ref> [0..1] Text 2488
       Debtor <Dbtr> [0..1] ± 2488
       DebtorAccount <DbtrAcct> [0..1]  2488
         Identification <Id> [1..1]  2488
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2489
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2489
Or}           Other <Othr> [1..1] ± 2489
         Name <Nm> [0..1] Text 2490
       DebtorAgent <DbtrAgt> [0..1]  2490
         Party <Pty> [1..1]  2490
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2491
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2491
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2491
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2492
         LEI <LEI> [0..1] IdentifierSet 2492
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  2493
         Identification <Id> [1..1]  2493
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2493
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2494
Or}           Other <Othr> [1..1] ± 2494
         Name <Nm> [0..1] Text 2494
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  2494
         Party <Pty> [1..1]  2495
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2495
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2495
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2496
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2497
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2478 May 2026
```

## File page 2479

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         LEI <LEI> [0..1] IdentifierSet 2497
       IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2498
         Identification <Id> [1..1]  2498
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2498
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2499
Or}           Other <Othr> [1..1] ± 2499
         Name <Nm> [0..1] Text 2499
       IntermediaryAgent2 <IntrmyAgt2> [0..1]  2499
         Party <Pty> [1..1]  2500
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2500
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2500
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2501
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2502
         LEI <LEI> [0..1] IdentifierSet 2502
       IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2503
         Identification <Id> [1..1]  2503
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2503
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2504
Or}           Other <Othr> [1..1] ± 2504
         Name <Nm> [0..1] Text 2504
       CreditorAgent <CdtrAgt> [1..1]  2504
         Party <Pty> [1..1]  2505
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2505
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2505
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2506
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2507
         LEI <LEI> [0..1] IdentifierSet 2507
       CreditorAgentAccount <CdtrAgtAcct> [0..1]  2508
         Identification <Id> [1..1]  2508
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2508
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2509
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2479 May 2026
```

## File page 2480

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Other <Othr> [1..1] ± 2509
         Name <Nm> [0..1] Text 2509
       Creditor <Cdtr> [0..1] ± 2509
       CreditorAccount <CdtrAcct> [1..1]  2510
         Identification <Id> [1..1]  2510
{Or           IBAN <IBAN> [1..1] IdentifierSet C19 2510
Or           BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2511
Or}           Other <Othr> [1..1] ± 2511
         Name <Nm> [0..1] Text 2511
Or     ChequeDetails <ChqDtls> [1..1]  2511
       Number <Nb> [0..1] Text 2512
       PayeeIdentification <PyeeId> [1..1] ± 2512
       DraweeIdentification <DrweeId> [0..1]  2512
         Party <Pty> [1..1]  2513
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2513
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2513
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2514
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2515
         LEI <LEI> [0..1] IdentifierSet 2515
       DrawerIdentification <DrwrId> [0..1] ± 2516
Or     BankersDraftDetails <BkrsDrftDtls> [1..1]  2516
       Number <Nb> [0..1] Text 2516
       PayeeIdentification <PyeeId> [1..1] ± 2516
       DraweeIdentification <DrweeId> [0..1]  2517
         Party <Pty> [1..1]  2517
{Or           NameAndAddress <NmAndAdr> [1..1] ± 2517
Or           BICFI <BICFI> [1..1] IdentifierSet C7 2518
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2518
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 2519
         LEI <LEI> [0..1] IdentifierSet 2519
       DrawerIdentification <DrwrId> [0..1] ± 2520
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2480 May 2026
```

