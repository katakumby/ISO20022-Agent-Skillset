---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.2 ReferredDocumentAmount <RfrdDocAmt>", "5.4.2.18.17.2.2.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>", "5.4.2.18.17.2.2.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [504]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.2.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 504 to 504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 504

```text
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
5.4.2.18.17.2.2.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the adjustment must be subtracted or added to the total amount.
Datatype: "CreditDebitCode" on page 590
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
5.4.2.18.17.2.2.2.3  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the adjustment.
Datatype: "Max4Text" on page 609
5.4.2.18.17.2.2.2.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides further details on the document adjustment.
Datatype: "Max140Text" on page 608
5.4.2.18.17.2.3  CreditorReferenceInformation <CdtrRefInf>
Presence: [0..1]
Definition: Reference information provided by the creditor to allow the identification of the underlying
documents.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 504 March 2026
```

