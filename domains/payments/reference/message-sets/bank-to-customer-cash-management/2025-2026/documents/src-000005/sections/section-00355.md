---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.1 Aggregated <Aggtd>", "3.4.2.15.18.2.26.3.1.5 TransactionDateRange <TxDtRg>"]
file_pages: [510, 511]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.1.5 TransactionDateRange <TxDtRg>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 510 to 511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 510

```text
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.3.1.5  TransactionDateRange <TxDtRg>
Presence: [0..1]
Definition: Date range on which the globalisation applies.
TransactionDateRange <TxDtRg> contains one of the following elements (see
"DateOrDateTimePeriod1Choice" on page 827 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 827
Or}   DateTime <DtTm> [1..1] ± 827
3.4.2.15.18.2.26.3.2  Individual <Indv>
Presence: [1..1]
Definition: Card transaction details for the individual transaction, as recorded at the POI (point of
interaction).
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
510 March 2026
```

## File page 511

```text
Individual <Indv> contains the following CardIndividualTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ICCRelatedData <ICCRltdData> [0..1] Text 512
   PaymentContext <PmtCntxt> [0..1]  512
     CardPresent <CardPres> [0..1] Indicator 512
     CardholderPresent <CrdhldrPres> [0..1] Indicator 512
     OnLineContext <OnLineCntxt> [0..1] Indicator 513
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
511 March 2026
```

