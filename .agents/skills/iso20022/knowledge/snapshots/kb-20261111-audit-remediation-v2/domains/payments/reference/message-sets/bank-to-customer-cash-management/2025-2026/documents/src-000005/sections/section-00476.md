---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.2 ReferredDocumentAmount <RfrdDocAmt>", "4.4.2.14.18.2.15.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>", "4.4.2.14.18.2.15.2.2.1.1 Type <Tp>", "4.4.2.14.18.2.15.2.2.1.1.1 Code <Cd>"]
file_pages: [703]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.2.1.1.1 Code <Cd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 703 to 703.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 703

```text
4.4.2.14.18.2.15.2.2.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the amount type, as published in an external referred amount code set.
Datatype: "ExternalDocumentAmountType1Code" on page 896
4.4.2.14.18.2.15.2.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the amount type, in a free-text form.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.15.2.2.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.2.14.18.2.15.2.2.2  AdjustmentAmountAndReason <AdjstmntAmtAndRsn>
Presence: [0..*]
Definition: Specifies detailed information on the amount and reason of the adjustment.
AdjustmentAmountAndReason <AdjstmntAmtAndRsn> contains the following
DocumentAdjustment1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 703
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 704
   Reason <Rsn> [0..1] Text 704
   AdditionalInformation <AddtlInf> [0..1] Text 704
4.4.2.14.18.2.15.2.2.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the document adjustment.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
703 March 2026
```

