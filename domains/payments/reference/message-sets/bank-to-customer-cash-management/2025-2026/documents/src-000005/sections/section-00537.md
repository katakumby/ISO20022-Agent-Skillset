---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.3 Transaction <Tx>", "4.4.2.14.18.2.26.3.2 Individual <Indv>", "4.4.2.14.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>"]
file_pages: [770]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 770 to 770.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 770

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 778
4.4.2.14.18.2.26.3.2.1  ICCRelatedData <ICCRltdData>
Presence: [0..1]
Definition: Data related to an integrated circuit card application.
Datatype: "Max1025Text" on page 914
4.4.2.14.18.2.26.3.2.2  PaymentContext <PmtCntxt>
Presence: [0..1]
Definition: Context of the card payment transaction.
PaymentContext <PmtCntxt> contains the following PaymentContext3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
4.4.2.14.18.2.26.3.2.2.1  CardPresent <CardPres>
Presence: [0..1]
Definition: Indicates whether the transaction has been initiated by a card physically present or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
4.4.2.14.18.2.26.3.2.2.2  CardholderPresent <CrdhldrPres>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
770 March 2026
```

