---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.2 POI <POI>", "3.4.2.15.18.2.26.2.5 Component <Cmpnt>", "3.4.2.15.18.2.26.2.5.5 SerialNumber <SrlNb>"]
file_pages: [506, 507]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.2.5.5 SerialNumber <SrlNb>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 506 to 507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 506

```text
Datatype: "Max16Text" on page 915
3.4.2.15.18.2.26.2.5.5  SerialNumber <SrlNb>
Presence: [0..1]
Definition: Serial number of a component.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.26.2.5.6  ApprovalNumber <ApprvlNb>
Presence: [0..*]
Definition: Unique approval number for a component, delivered by a certification body.
Usage: More than one approval number could be present, when assigned by different bodies. The
certification body identification must be provided within the approval number (for example at the
beginning of the value).
Datatype: "Max70Text" on page 917
3.4.2.15.18.2.26.3  Transaction <Tx>
Presence: [0..1]
Definition: Card transaction details, which can be either globalised by the acquirer or individual
transaction.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
506 March 2026
```

## File page 507

```text
Transaction <Tx> contains one of the following CardTransaction3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Aggregated <Aggtd> [1..1]  508
     AdditionalService <AddtlSvc> [0..1] CodeSet 508
     TransactionCategory <TxCtgy> [0..1] CodeSet 509
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 509
     SequenceNumberRange <SeqNbRg> [0..1]  509
       FirstTransaction <FrstTx> [0..1] Text 509
       LastTransaction <LastTx> [0..1] Text 509
     TransactionDateRange <TxDtRg> [0..1] ± 510
Or}   Individual <Indv> [1..1]  510
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
507 March 2026
```

