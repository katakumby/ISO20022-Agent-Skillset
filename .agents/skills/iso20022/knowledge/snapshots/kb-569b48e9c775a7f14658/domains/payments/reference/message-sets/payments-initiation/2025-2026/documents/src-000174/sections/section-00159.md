---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.2 ReferredDocumentAmount <RfrdDocAmt>", "3.4.3.7.12.11.2.2.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>", "3.4.3.7.12.11.2.2.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.2.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 235 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 235

```text
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
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
3.4.3.7.12.11.2.2.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the adjustment must be subtracted or added to the total amount.
Datatype: "CreditDebitCode" on page 590
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.3.7.12.11.2.2.2.3  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the adjustment.
Datatype: "Max4Text" on page 609
3.4.3.7.12.11.2.2.2.4  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides further details on the document adjustment.
Datatype: "Max140Text" on page 608
3.4.3.7.12.11.2.3  CreditorReferenceInformation <CdtrRefInf>
Presence: [0..1]
Definition: Reference information provided by the creditor to allow the identification of the underlying
documents.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 235 March 2026
```

