---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.15.18.2.15.2.1.4 LineDetails <LineDtls>", "3.4.2.15.18.2.15.2.1.4.3 Amount <Amt>", "3.4.2.15.18.2.15.2.1.4.3.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>", "3.4.2.15.18.2.15.2.1.4.3.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.1.4.3.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 443 to 443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 443

```text
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
3.4.2.15.18.2.15.2.1.4.3.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the adjustment must be subtracted or added to the total amount.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.15.18.2.15.2.1.4.3.2.3  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the adjustment.
Datatype: "Max4Text" on page 917
3.4.2.15.18.2.15.2.1.4.3.2.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides further details on the document adjustment.
Datatype: "Max140Text" on page 914
3.4.2.15.18.2.15.2.2  ReferredDocumentAmount <RfrdDocAmt>
Presence: [0..1]
Definition: Provides details on the amounts of the referred document.
Impacted by: C27 "RemittanceAmountAndTypeGuideline"
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
443 March 2026
```

