---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.2 POI <POI>", "4.4.2.14.18.2.26.2.5 Component <Cmpnt>", "4.4.2.14.18.2.26.2.5.5 SerialNumber <SrlNb>"]
file_pages: [764, 765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.2.5.5 SerialNumber <SrlNb>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 764 to 765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 764

```text
Datatype: "Max16Text" on page 915
4.4.2.14.18.2.26.2.5.5  SerialNumber <SrlNb>
Presence: [0..1]
Definition: Serial number of a component.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.2.5.6  ApprovalNumber <ApprvlNb>
Presence: [0..*]
Definition: Unique approval number for a component, delivered by a certification body.
Usage: More than one approval number could be present, when assigned by different bodies. The
certification body identification must be provided within the approval number (for example at the
beginning of the value).
Datatype: "Max70Text" on page 917
4.4.2.14.18.2.26.3  Transaction <Tx>
Presence: [0..1]
Definition: Card transaction details, which can be either globalised by the acquirer or individual
transaction.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
764 March 2026
```

## File page 765

```text
Transaction <Tx> contains one of the following CardTransaction3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Aggregated <Aggtd> [1..1]  766
     AdditionalService <AddtlSvc> [0..1] CodeSet 766
     TransactionCategory <TxCtgy> [0..1] CodeSet 767
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 767
     SequenceNumberRange <SeqNbRg> [0..1]  767
       FirstTransaction <FrstTx> [0..1] Text 767
       LastTransaction <LastTx> [0..1] Text 767
     TransactionDateRange <TxDtRg> [0..1] ± 768
Or}   Individual <Indv> [1..1]  768
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
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
765 March 2026
```

