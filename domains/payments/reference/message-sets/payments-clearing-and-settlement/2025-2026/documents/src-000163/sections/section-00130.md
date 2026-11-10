---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.12 DirectDebitTransaction <DrctDbtTx>", "3.4.2.12.4 PreNotificationDate <PreNtfctnDt>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.12.4 PreNotificationDate <PreNtfctnDt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
Usage: The direct debit pre-notification is used to reconcile separately sent collection information with
the direct debit transaction information.
Datatype: "Max35Text" on page 1246
3.4.2.12.4  PreNotificationDate <PreNtfctnDt>
Presence: [0..1]
Definition: Date on which the creditor notifies the debtor about the amount and date on which the direct
debit instruction will be presented to the debtor's agent.
Datatype: "ISODate" on page 1239
3.4.2.13  Creditor <Cdtr>
Presence: [1..1]
Definition: Party to which an amount of money is due.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
181 March 2026
```

