---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.1 Batch <Btch>"]
file_pages: [625]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.1 Batch <Btch>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 625 to 625.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 625

```text
4.4.2.14.18.1  Batch <Btch>
Presence: [0..1]
Definition: Provides details on batched transactions.
Batch <Btch> contains the following BatchInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [0..1] Text 625
   PaymentInformationIdentification <PmtInfId> [0..1] Text 625
   NumberOfTransactions <NbOfTxs> [0..1] Text 625
   TotalAmount <TtlAmt> [0..1] Amount C2, C6 625
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 626
4.4.2.14.18.1.1  MessageIdentification <MsgId>
Presence: [0..1]
Definition: Point to point reference, as assigned by the sending party, to unambiguously identify the
batch of transactions.
Datatype: "Max35Text" on page 916
4.4.2.14.18.1.2  PaymentInformationIdentification <PmtInfId>
Presence: [0..1]
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.
Datatype: "Max35Text" on page 916
4.4.2.14.18.1.3  NumberOfTransactions <NbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions included in the batch.
Datatype: "Max15NumericText" on page 915
4.4.2.14.18.1.4  TotalAmount <TtlAmt>
Presence: [0..1]
Definition: Total amount of money reported in the batch entry.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
625 March 2026
```

