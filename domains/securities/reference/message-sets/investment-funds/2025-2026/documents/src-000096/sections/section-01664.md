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
file_pages: [2322, 2323, 2324, 2325]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# Continuation at file page 2322

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2322 to 2325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2322

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Equalisation <Equlstn> [0..1] ± C35,
C36
2467
       CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 2468
       TransactionChannelType <TxChanlTp> [0..1] ± 2469
       SignatureType <SgntrTp> [0..1] ± 2469
       OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C43 2469
       GatingOrHoldBackDetails <GtgOrHldBckDtls> [0..1]  2470
         Type <Tp> [1..1] CodeSet 2471
         Amount <Amt> [0..1] Amount C3, C10 2472
         ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 2472
         FinancialInstrumentIdentification <FinInstrmId> [0..1]  2472
{Or           ISIN <ISIN> [1..1] IdentifierSet 2473
Or           SEDOL <SEDOL> [1..1] IdentifierSet 2473
Or           CUSIP <CUSIP> [1..1] IdentifierSet 2474
Or           RIC <RIC> [1..1] IdentifierSet 2474
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 2474
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 2474
Or           CTA <CTA> [1..1] IdentifierSet 2474
Or           QUICK <QUICK> [1..1] IdentifierSet 2474
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 2474
Or           Dutch <Dtch> [1..1] IdentifierSet 2475
Or           Valoren <Vlrn> [1..1] IdentifierSet 2475
Or           Sicovam <SCVM> [1..1] IdentifierSet 2475
Or           Belgian <Belgn> [1..1] IdentifierSet 2475
Or           Common <Cmon> [1..1] IdentifierSet 2475
Or           DTI <DTI> [1..1] IdentifierSet 2475
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  2475
             Identification <Id> [1..1] Text 2476
             IdentificationSource <IdSrc> [1..1] ± 2476
         FinancialInstrumentName <FinInstrmNm> [0..1] Text 2476
         RedemptionCompletion <RedCmpltn> [0..1] CodeSet 2476
         FinalConfirmation <FnlConf> [0..1] Indicator 2476
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2322 May 2026
```

## File page 2323

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 2477
     BulkCashSettlementDetails <BlkCshSttlmDtls> [0..1]  2477
       PaymentInstrument <PmtInstrm> [1..1]  2481
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  2485
           Reference <Ref> [0..1] Text 2488
           Debtor <Dbtr> [0..1] ± 2488
           DebtorAccount <DbtrAcct> [0..1]  2488
             Identification <Id> [1..1]  2488
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2489
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2489
Or}               Other <Othr> [1..1] ± 2489
             Name <Nm> [0..1] Text 2490
           DebtorAgent <DbtrAgt> [0..1]  2490
             Party <Pty> [1..1]  2490
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2491
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2491
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2491
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2492
             LEI <LEI> [0..1] IdentifierSet 2492
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  2493
             Identification <Id> [1..1]  2493
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2493
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2494
Or}               Other <Othr> [1..1] ± 2494
             Name <Nm> [0..1] Text 2494
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  2494
             Party <Pty> [1..1]  2495
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2495
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2495
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2496
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2497
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2323 May 2026
```

## File page 2324

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             LEI <LEI> [0..1] IdentifierSet 2497
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2498
             Identification <Id> [1..1]  2498
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2498
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2499
Or}               Other <Othr> [1..1] ± 2499
             Name <Nm> [0..1] Text 2499
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  2499
             Party <Pty> [1..1]  2500
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2500
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2500
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2501
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2502
             LEI <LEI> [0..1] IdentifierSet 2502
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2503
             Identification <Id> [1..1]  2503
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2503
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2504
Or}               Other <Othr> [1..1] ± 2504
             Name <Nm> [0..1] Text 2504
           CreditorAgent <CdtrAgt> [1..1]  2504
             Party <Pty> [1..1]  2505
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2505
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2505
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2506
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2507
             LEI <LEI> [0..1] IdentifierSet 2507
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  2508
             Identification <Id> [1..1]  2508
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2508
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2509
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2324 May 2026
```

## File page 2325

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}               Other <Othr> [1..1] ± 2509
             Name <Nm> [0..1] Text 2509
           Creditor <Cdtr> [0..1] ± 2509
           CreditorAccount <CdtrAcct> [1..1]  2510
             Identification <Id> [1..1]  2510
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2510
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2511
Or}               Other <Othr> [1..1] ± 2511
             Name <Nm> [0..1] Text 2511
Or         ChequeDetails <ChqDtls> [1..1]  2511
           Number <Nb> [0..1] Text 2512
           PayeeIdentification <PyeeId> [1..1] ± 2512
           DraweeIdentification <DrweeId> [0..1]  2512
             Party <Pty> [1..1]  2513
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2513
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2513
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2514
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2515
             LEI <LEI> [0..1] IdentifierSet 2515
           DrawerIdentification <DrwrId> [0..1] ± 2516
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  2516
           Number <Nb> [0..1] Text 2516
           PayeeIdentification <PyeeId> [1..1] ± 2516
           DraweeIdentification <DrweeId> [0..1]  2517
             Party <Pty> [1..1]  2517
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2517
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2518
Or               ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 2518
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2519
             LEI <LEI> [0..1] IdentifierSet 2519
           DrawerIdentification <DrwrId> [0..1] ± 2520
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2325 May 2026
```

