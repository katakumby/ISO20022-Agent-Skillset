---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [364, 365, 366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# Continuation at file page 364

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 364 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 489
     SafekeepingAccount <SfkpgAcct> [0..1] ± 489
     UnderlyingAllocation <UndrlygAllcn> [0..*]  C31 490
       Amount <Amt> [1..1] Amount C2, C6 490
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 490
       Account <Acct> [1..1] ± C20,
C18
491
       Purpose <Purp> [1..1] ± 491
       Reference <Ref> [1..1] Text 492
       RelatedReferences <RltdRefs> [0..*] ± 492
     CashDeposit <CshDpst> [0..*] ± 492
     CardTransaction <CardTx> [0..1]  493
       Card <Card> [0..1]  496
         PlainCardData <PlainCardData> [0..1]  497
           PAN <PAN> [1..1] Text 498
           CardSequenceNumber <CardSeqNb> [0..1] Text 498
           EffectiveDate <FctvDt> [0..1] YearMonth 498
           ExpiryDate <XpryDt> [1..1] YearMonth 498
           ServiceCode <SvcCd> [0..1] Text 498
           TrackData <TrckData> [0..*]  499
             TrackNumber <TrckNb> [0..1] Text 499
             TrackValue <TrckVal> [1..1] Text 499
           CardSecurityCode <CardSctyCd> [0..1]  499
             CSCManagement <CSCMgmt> [1..1] CodeSet 499
             CSCValue <CSCVal> [0..1] Text 500
         CardCountryCode <CardCtryCd> [0..1] Text 500
         CardBrand <CardBrnd> [0..1] ± 500
         AdditionalCardData <AddtlCardData> [0..1] Text 500
       POI <POI> [0..1]  500
         Identification <Id> [1..1] ± 501
         SystemName <SysNm> [0..1] Text 502
         GroupIdentification <GrpId> [0..1] Text 502
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
364 March 2026
```

## File page 365

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Capabilities <Cpblties> [0..1]  502
           CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 502
           CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 503
           OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 503
           DisplayCapabilities <DispCpblties> [0..*]  504
             DisplayType <DispTp> [1..1] CodeSet 504
             NumberOfLines <NbOfLines> [1..1] Text 504
             LineWidth <LineWidth> [1..1] Text 504
           PrintLineWidth <PrtLineWidth> [0..1] Text 504
         Component <Cmpnt> [0..*]  504
           POIComponentType <POICmpntTp> [1..1] CodeSet 505
           ManufacturerIdentification <ManfctrId> [0..1] Text 505
           Model <Mdl> [0..1] Text 505
           VersionNumber <VrsnNb> [0..1] Text 505
           SerialNumber <SrlNb> [0..1] Text 506
           ApprovalNumber <ApprvlNb> [0..*] Text 506
       Transaction <Tx> [0..1]  506
{Or         Aggregated <Aggtd> [1..1]  508
           AdditionalService <AddtlSvc> [0..1] CodeSet 508
           TransactionCategory <TxCtgy> [0..1] CodeSet 509
           SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 509
           SequenceNumberRange <SeqNbRg> [0..1]  509
             FirstTransaction <FrstTx> [0..1] Text 509
             LastTransaction <LastTx> [0..1] Text 509
           TransactionDateRange <TxDtRg> [0..1] ± 510
Or}         Individual <Indv> [1..1]  510
           ICCRelatedData <ICCRltdData> [0..1] Text 512
           PaymentContext <PmtCntxt> [0..1]  512
             CardPresent <CardPres> [0..1] Indicator 512
             CardholderPresent <CrdhldrPres> [0..1] Indicator 512
             OnLineContext <OnLineCntxt> [0..1] Indicator 513
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
365 March 2026
```

## File page 366

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             AttendanceContext <AttndncCntxt> [0..1] CodeSet 513
             TransactionEnvironment <TxEnvt> [0..1] CodeSet 513
             TransactionChannel <TxChanl> [0..1] CodeSet 513
             AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 514
             AttendantLanguage <AttndntLang> [0..1] CodeSet 514
             CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 514
             FallbackIndicator <FllbckInd> [0..1] Indicator 514
             AuthenticationMethod <AuthntcnMtd> [0..1]  515
               AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 515
               AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 515
           AdditionalService <AddtlSvc> [0..1] CodeSet 516
           TransactionCategory <TxCtgy> [0..1] CodeSet 516
           SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 516
           SaleReferenceNumber <SaleRefNb> [0..1] Text 517
           RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 517
           SequenceNumber <SeqNb> [0..1] Text 517
           TransactionIdentification <TxId> [0..1] ± 517
           Product <Pdct> [0..1]  517
             ProductCode <PdctCd> [1..1] Text 518
             UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 518
             ProductQuantity <PdctQty> [0..1] Quantity 519
             UnitPrice <UnitPric> [0..1] Amount 519
             ProductAmount <PdctAmt> [0..1] Amount 519
             TaxType <TaxTp> [0..1] Text 520
             AdditionalProductInformation <AddtlPdctInf> [0..1] Text 520
           ValidationDate <VldtnDt> [0..1] Date 520
           ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 520
       PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
520
     InstructionCopy <InstrCpy> [0..1] Text 521
     AdditionalTransactionInformation <AddtlTxInf> [0..1] Text 521
     SupplementaryData <SplmtryData> [0..*] ± C30 521
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
366 March 2026
```

