---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.2 ReferredDocumentAmount <RfrdDocAmt>", "6.4.2.47.2.2.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>", "6.4.2.47.2.2.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [807]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.2.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 807 to 807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 807

```text
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.2.47.2.2.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the adjustment must be subtracted or added to the total amount.
Datatype: "CreditDebitCode" on page 1227
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.4.2.47.2.2.2.3  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the adjustment.
Datatype: "Max4Text" on page 1246
6.4.2.47.2.2.2.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides further details on the document adjustment.
Datatype: "Max140Text" on page 1244
6.4.2.47.2.3  CreditorReferenceInformation <CdtrRefInf>
Presence: [0..1]
Definition: Reference information provided by the creditor to allow the identification of the underlying
documents.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
807 March 2026
```

