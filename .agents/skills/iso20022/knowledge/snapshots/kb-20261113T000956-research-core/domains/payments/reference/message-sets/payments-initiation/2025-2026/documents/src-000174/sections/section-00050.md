---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.24 Tax <Tax>", "2.4.2.19.24.8 TotalTaxAmount <TtlTaxAmt>"]
file_pages: [77]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.24.8 TotalTaxAmount <TtlTaxAmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 77 to 77.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
Note: The decimal separator is a dot.
2.4.2.19.24.8  TotalTaxAmount <TtlTaxAmt>
Presence: [0..1]
Definition: Total amount of money as result of the calculation of the tax.
Impacted by: C2 "ActiveOrHistoricCurrency", C19 "CurrencyAmount"
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
2.4.2.19.24.9  Date <Dt>
Presence: [0..1]
Definition: Date by which tax is due.
Datatype: "ISODate" on page 603
2.4.2.19.24.10  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Sequential number of the tax report.
Datatype: "Number" on page 606
2.4.2.19.24.11  Record <Rcrd>
Presence: [0..*]
Definition: Record of tax details.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 77 March 2026
```

