---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.3 Transaction <Tx>", "2.4.2.15.18.2.26.3.1 Aggregated <Aggtd>", "2.4.2.15.18.2.26.3.1.5 TransactionDateRange <TxDtRg>"]
file_pages: [250, 251]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.3.1.5 TransactionDateRange <TxDtRg>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 250 to 251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.26.3.1.5  TransactionDateRange <TxDtRg>
Presence: [0..1]
Definition: Date range on which the globalisation applies.
TransactionDateRange <TxDtRg> contains one of the following elements (see
"DateOrDateTimePeriod1Choice" on page 827 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 827
Or}   DateTime <DtTm> [1..1] ± 827
2.4.2.15.18.2.26.3.2  Individual <Indv>
Presence: [1..1]
Definition: Card transaction details for the individual transaction, as recorded at the POI (point of
interaction).
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
250 March 2026
```

## File page 251

```text
Individual <Indv> contains the following CardIndividualTransaction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ICCRelatedData <ICCRltdData> [0..1] Text 252
   PaymentContext <PmtCntxt> [0..1]  252
     CardPresent <CardPres> [0..1] Indicator 252
     CardholderPresent <CrdhldrPres> [0..1] Indicator 252
     OnLineContext <OnLineCntxt> [0..1] Indicator 253
     AttendanceContext <AttndncCntxt> [0..1] CodeSet 253
     TransactionEnvironment <TxEnvt> [0..1] CodeSet 253
     TransactionChannel <TxChanl> [0..1] CodeSet 253
     AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 254
     AttendantLanguage <AttndntLang> [0..1] CodeSet 254
     CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 254
     FallbackIndicator <FllbckInd> [0..1] Indicator 254
     AuthenticationMethod <AuthntcnMtd> [0..1]  255
       AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 255
       AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 255
   AdditionalService <AddtlSvc> [0..1] CodeSet 256
   TransactionCategory <TxCtgy> [0..1] CodeSet 256
   SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 256
   SaleReferenceNumber <SaleRefNb> [0..1] Text 257
   RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 257
   SequenceNumber <SeqNb> [0..1] Text 257
   TransactionIdentification <TxId> [0..1] ± 257
   Product <Pdct> [0..1]  257
     ProductCode <PdctCd> [1..1] Text 258
     UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 258
     ProductQuantity <PdctQty> [0..1] Quantity 259
     UnitPrice <UnitPric> [0..1] Amount 259
     ProductAmount <PdctAmt> [0..1] Amount 259
     TaxType <TaxTp> [0..1] Text 260
     AdditionalProductInformation <AddtlPdctInf> [0..1] Text 260
   ValidationDate <VldtnDt> [0..1] Date 260
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
251 March 2026
```

