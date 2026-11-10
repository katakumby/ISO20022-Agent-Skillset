---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.2 Individual <Indv>", "3.4.2.15.18.2.26.3.2.2 PaymentContext <PmtCntxt>", "3.4.2.15.18.2.26.3.2.2.3 OnLineContext <OnLineCntxt>"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.2.2.3 OnLineContext <OnLineCntxt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
Definition: Indicates whether the transaction has been initiated in presence of the cardholder or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
3.4.2.15.18.2.26.3.2.2.3  OnLineContext <OnLineCntxt>
Presence: [0..1]
Definition: On-line or off-line context of the transaction.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
3.4.2.15.18.2.26.3.2.2.4  AttendanceContext <AttndncCntxt>
Presence: [0..1]
Definition: Human attendance at the POI location during the transaction.
Datatype: "AttendanceContext1Code" on page 888
CodeName Name Definition
ATTD Attended Attended payment, with an attendant.
SATT SemiAttended Semi-attended, including self checkout.
An attendant supervises several
payment, and could be called to help the
cardholder.
UATT Unattended Unattended payment, no attendant
present.
3.4.2.15.18.2.26.3.2.2.5  TransactionEnvironment <TxEnvt>
Presence: [0..1]
Definition: Indicates the environment of the transaction.
Datatype: "TransactionEnvironment1Code" on page 906
CodeName Name Definition
MERC Merchant Merchant environment.
PRIV Private Private environment.
PUBL Public Public environment.
3.4.2.15.18.2.26.3.2.2.6  TransactionChannel <TxChanl>
Presence: [0..1]
Definition: Identifies the type of the communication channels used by the cardholder to the acceptor
system.
Datatype: "TransactionChannel1Code" on page 906
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
513 March 2026
```

