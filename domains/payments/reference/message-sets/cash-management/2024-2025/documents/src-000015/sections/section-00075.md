---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.1 MessageIdentification <MsgId>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.1 MessageIdentification <MsgId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
• SettlementAmountCreditDebitIndicator2Rule
If at least one occurrence of InterbankSettlementAmount/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InterbankSettlementAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not present,
then CreditDebitIndicator is optional.
On Condition
    /InterbankSettlementAmount[*]/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present
Following Must be True
    /CreditDebitIndicator Must be absent
• SettlementAmountCurrencyRule
If at least one occurrence of InterbankSettlementAmount/CurrencyAndAmountRange is present, then
no occurrence of InterbankSettlementAmountCurrency is allowed.
If InterbankSettlementAmount/CurrencyAndAmountRange is not present, then any occurrence of
InterbankSettlementAmountCurrency is optional.
On Condition
    /InterbankSettlementAmount[*]/CurrencyAndAmountRange is present
Following Must be True
    /InterbankSettlementAmountCurrency[*] Must be absent
4.4.2.2.2.2.3.1  MessageIdentification <MsgId>
Presence: [0..*]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original payment transaction message.
Usage: this is the former transaction reference.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.2  RequestedExecutionDate <ReqdExctnDt>
Presence: [0..*]
Definition: Date and time at which the cash is at the disposal of the credit account owner, or ceases to
be at the disposal of the debit account owner.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 144 February 2025
```

