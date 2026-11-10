---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.2 Individual <Indv>", "3.4.2.15.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>"]
file_pages: [512]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 512 to 512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 512

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 520
3.4.2.15.18.2.26.3.2.1  ICCRelatedData <ICCRltdData>
Presence: [0..1]
Definition: Data related to an integrated circuit card application.
Datatype: "Max1025Text" on page 914
3.4.2.15.18.2.26.3.2.2  PaymentContext <PmtCntxt>
Presence: [0..1]
Definition: Context of the card payment transaction.
PaymentContext <PmtCntxt> contains the following PaymentContext3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
3.4.2.15.18.2.26.3.2.2.1  CardPresent <CardPres>
Presence: [0..1]
Definition: Indicates whether the transaction has been initiated by a card physically present or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
3.4.2.15.18.2.26.3.2.2.2  CardholderPresent <CrdhldrPres>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
512 March 2026
```

