---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.3 Transaction <Tx>", "4.4.2.14.18.2.26.3.1 Aggregated <Aggtd>", "4.4.2.14.18.2.26.3.1.5 TransactionDateRange <TxDtRg>"]
file_pages: [768, 769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.3.1.5 TransactionDateRange <TxDtRg>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 768 to 769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 768

```text
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.3.1.5  TransactionDateRange <TxDtRg>
Presence: [0..1]
Definition: Date range on which the globalisation applies.
TransactionDateRange <TxDtRg> contains one of the following elements (see
"DateOrDateTimePeriod1Choice" on page 827 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 827
Or}   DateTime <DtTm> [1..1] ± 827
4.4.2.14.18.2.26.3.2  Individual <Indv>
Presence: [1..1]
Definition: Card transaction details for the individual transaction, as recorded at the POI (point of
interaction).
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
768 March 2026
```

## File page 769

```text
Individual <Indv> contains the following CardIndividualTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ICCRelatedData <ICCRltdData> [0..1] Text 770
   PaymentContext <PmtCntxt> [0..1]  770
     CardPresent <CardPres> [0..1] Indicator 770
     CardholderPresent <CrdhldrPres> [0..1] Indicator 770
     OnLineContext <OnLineCntxt> [0..1] Indicator 771
     AttendanceContext <AttndncCntxt> [0..1] CodeSet 771
     TransactionEnvironment <TxEnvt> [0..1] CodeSet 771
     TransactionChannel <TxChanl> [0..1] CodeSet 771
     AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 772
     AttendantLanguage <AttndntLang> [0..1] CodeSet 772
     CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 772
     FallbackIndicator <FllbckInd> [0..1] Indicator 772
     AuthenticationMethod <AuthntcnMtd> [0..1]  773
       AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 773
       AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 773
   AdditionalService <AddtlSvc> [0..1] CodeSet 774
   TransactionCategory <TxCtgy> [0..1] CodeSet 774
   SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 774
   SaleReferenceNumber <SaleRefNb> [0..1] Text 775
   RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 775
   SequenceNumber <SeqNb> [0..1] Text 775
   TransactionIdentification <TxId> [0..1] ± 775
   Product <Pdct> [0..1]  775
     ProductCode <PdctCd> [1..1] Text 776
     UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 776
     ProductQuantity <PdctQty> [0..1] Quantity 777
     UnitPrice <UnitPric> [0..1] Amount 777
     ProductAmount <PdctAmt> [0..1] Amount 777
     TaxType <TaxTp> [0..1] Text 778
     AdditionalProductInformation <AddtlPdctInf> [0..1] Text 778
   ValidationDate <VldtnDt> [0..1] Date 778
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
769 March 2026
```

