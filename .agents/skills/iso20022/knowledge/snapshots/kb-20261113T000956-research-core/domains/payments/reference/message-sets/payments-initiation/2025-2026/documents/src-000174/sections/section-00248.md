---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.3.8.9.11.2.1.4 LineDetails <LineDtls>", "4.4.3.8.9.11.2.1.4.3 Amount <Amt>", "4.4.3.8.9.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>", "4.4.3.8.9.11.2.1.4.3.1.1 Type <Tp>", "4.4.3.8.9.11.2.1.4.3.1.1.1 Code <Cd>"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.1.4.3.1.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
4.4.3.8.9.11.2.1.4.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the amount type, as published in an external referred amount code set.
Datatype: "ExternalDocumentAmountType1Code" on page 593
4.4.3.8.9.11.2.1.4.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the amount type, in a free-text form.
Datatype: "Max35Text" on page 609
4.4.3.8.9.11.2.1.4.3.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
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
4.4.3.8.9.11.2.1.4.3.2  AdjustmentAmountAndReason <AdjstmntAmtAndRsn>
Presence: [0..*]
Definition: Specifies detailed information on the amount and reason of the adjustment.
AdjustmentAmountAndReason <AdjstmntAmtAndRsn> contains the following
DocumentAdjustment1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C9 362
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 363
   Reason <Rsn> [0..1] Text 363
   AdditionalInformation <AddtlInf> [0..1] Text 363
4.4.3.8.9.11.2.1.4.3.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the document adjustment.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 362 March 2026
```

