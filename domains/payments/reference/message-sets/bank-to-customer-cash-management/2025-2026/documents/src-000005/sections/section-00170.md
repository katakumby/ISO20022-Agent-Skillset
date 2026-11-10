---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.2 POI <POI>", "2.4.2.15.18.2.26.2.5 Component <Cmpnt>", "2.4.2.15.18.2.26.2.5.5 SerialNumber <SrlNb>"]
file_pages: [246, 247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.2.5.5 SerialNumber <SrlNb>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 246 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
Datatype: "Max16Text" on page 915
2.4.2.15.18.2.26.2.5.5  SerialNumber <SrlNb>
Presence: [0..1]
Definition: Serial number of a component.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.26.2.5.6  ApprovalNumber <ApprvlNb>
Presence: [0..*]
Definition: Unique approval number for a component, delivered by a certification body.
Usage: More than one approval number could be present, when assigned by different bodies. The
certification body identification must be provided within the approval number (for example at the
beginning of the value).
Datatype: "Max70Text" on page 917
2.4.2.15.18.2.26.3  Transaction <Tx>
Presence: [0..1]
Definition: Card transaction details, which can be either globalised by the acquirer or individual
transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
246 March 2026
```

## File page 247

```text
Transaction <Tx> contains one of the following CardTransaction3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Aggregated <Aggtd> [1..1]  248
     AdditionalService <AddtlSvc> [0..1] CodeSet 248
     TransactionCategory <TxCtgy> [0..1] CodeSet 249
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 249
     SequenceNumberRange <SeqNbRg> [0..1]  249
       FirstTransaction <FrstTx> [0..1] Text 249
       LastTransaction <LastTx> [0..1] Text 249
     TransactionDateRange <TxDtRg> [0..1] ± 250
Or}   Individual <Indv> [1..1]  250
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
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
247 March 2026
```

