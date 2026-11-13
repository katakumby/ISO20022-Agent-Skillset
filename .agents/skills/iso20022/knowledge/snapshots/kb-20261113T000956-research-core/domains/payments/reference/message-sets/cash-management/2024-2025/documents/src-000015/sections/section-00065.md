---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks"]
file_pages: [108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
preceding_topic_continuations: [{"constraint_ids": ["C13", "C14", "C15", "C16", "C17", "C18"], "until_heading": "4.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 108, "topic": "4.3 Constraints", "reference_path": "domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00064.md"}]
---

# 4.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 108 to 108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 108, C13–C18 before **4.4 Message Building Blocks** continue [4.3 Constraints](section-00064.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 108

```text
- If StatementReport is present, it indicates that a statement-type report needs to be returned.
In this case, the return message will contain information equivalent to that present in field 61
(Statement Line) of FIN standards, for example, value date, entry date, debit/credit indicator,
amount, transaction type identification code, reference for the account owner, reference of the
account servicing institution and supplementary details.
- If the StatementReportIndicator equals "false" or "0" (No), this means that the report type is
pre-defined between the transaction administrator and the member.
C13 SettlementAmountCreditDebitIndicator1Rule
If at least one occurrence of InterbankSettlementAmount/CurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InterbankSettlementAmount/CurrencyAndAmountRange/CreditDebitIndicator is not present,
then CreditDebitIndicator is optional.
C14 SettlementAmountCreditDebitIndicator2Rule
If at least one occurrence of InterbankSettlementAmount/ImpliedCurrencyAndAmountRange/
CreditDebitIndicator is present, then CreditDebitIndicator is not allowed.
If InterbankSettlementAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not
present, then CreditDebitIndicator is optional.
C15 SettlementAmountCurrencyRule
If at least one occurrence of InterbankSettlementAmount/CurrencyAndAmountRange is
present, then no occurrence of InterbankSettlementAmountCurrency is allowed.
If InterbankSettlementAmount/CurrencyAndAmountRange is not present, then any occurrence
of InterbankSettlementAmountCurrency is optional.
C16 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C17 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C18 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 108 February 2025
```

