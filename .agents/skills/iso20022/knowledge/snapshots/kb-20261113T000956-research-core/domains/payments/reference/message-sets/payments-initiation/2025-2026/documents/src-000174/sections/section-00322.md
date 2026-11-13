---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>", "5.4.2.18.5.4 PreNotificationDate <PreNtfctnDt>"]
file_pages: [462]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5.4 PreNotificationDate <PreNtfctnDt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 462 to 462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 462

```text
Usage: The direct debit pre-notification is used to reconcile separately sent collection information with
the direct debit transaction information.
Datatype: "Max35Text" on page 609
5.4.2.18.5.4  PreNotificationDate <PreNtfctnDt>
Presence: [0..1]
Definition: Date on which the creditor notifies the debtor about the amount and date on which the direct
debit instruction will be presented to the debtor's agent.
Datatype: "ISODate" on page 603
5.4.2.18.6  UltimateCreditor <UltmtCdtr>
Presence: [0..1]
Definition: Ultimate party to which an amount of money is due.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 462 March 2026
```

