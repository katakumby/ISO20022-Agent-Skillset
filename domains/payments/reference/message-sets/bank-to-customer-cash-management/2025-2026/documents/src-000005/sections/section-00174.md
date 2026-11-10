---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.3 Transaction <Tx>", "2.4.2.15.18.2.26.3.2 Individual <Indv>", "2.4.2.15.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>"]
file_pages: [252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.3.2.1 ICCRelatedData <ICCRltdData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 252 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 260
2.4.2.15.18.2.26.3.2.1  ICCRelatedData <ICCRltdData>
Presence: [0..1]
Definition: Data related to an integrated circuit card application.
Datatype: "Max1025Text" on page 914
2.4.2.15.18.2.26.3.2.2  PaymentContext <PmtCntxt>
Presence: [0..1]
Definition: Context of the card payment transaction.
PaymentContext <PmtCntxt> contains the following PaymentContext3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
2.4.2.15.18.2.26.3.2.2.1  CardPresent <CardPres>
Presence: [0..1]
Definition: Indicates whether the transaction has been initiated by a card physically present or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
2.4.2.15.18.2.26.3.2.2.2  CardholderPresent <CrdhldrPres>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
252 March 2026
```

