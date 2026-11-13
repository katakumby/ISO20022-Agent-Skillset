---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.15 Tax <Tax>", "5.4.2.18.15.8 TotalTaxAmount <TtlTaxAmt>"]
file_pages: [474]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.15.8 TotalTaxAmount <TtlTaxAmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 474 to 474.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 474

```text
Note: The decimal separator is a dot.
5.4.2.18.15.8  TotalTaxAmount <TtlTaxAmt>
Presence: [0..1]
Definition: Total amount of money as result of the calculation of the tax.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.18.15.9  Date <Dt>
Presence: [0..1]
Definition: Date by which tax is due.
Datatype: "ISODate" on page 603
5.4.2.18.15.10  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Sequential number of the tax report.
Datatype: "Number" on page 606
5.4.2.18.15.11  Record <Rcrd>
Presence: [0..*]
Definition: Record of tax details.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 474 March 2026
```

