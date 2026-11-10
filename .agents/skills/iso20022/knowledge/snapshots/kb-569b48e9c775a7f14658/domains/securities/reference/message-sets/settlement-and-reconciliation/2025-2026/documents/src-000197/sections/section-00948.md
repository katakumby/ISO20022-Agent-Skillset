---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.14 OtherAmounts39", "35.1.3.14.17 StockExchangeTax <StockXchgTax>"]
file_pages: [1384]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.14.17 StockExchangeTax <StockXchgTax>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1384 to 1384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1384

```text
StampDuty <StmpDty> contains the following elements (see "AmountAndDirection44" on page 1375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.14.17  StockExchangeTax <StockXchgTax>
Presence: [0..1]
Definition: Amount of stock exchange tax.
StockExchangeTax <StockXchgTax> contains the following elements (see "AmountAndDirection44"
on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.14.18  TransferTax <TrfTax>
Presence: [0..1]
Definition: Amount of tax levied on a transfer of ownership of financial instrument.
TransferTax <TrfTax> contains the following elements (see "AmountAndDirection44" on page 1375 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.14.19  TransactionTax <TxTax>
Presence: [0..1]
Definition: Amount of transaction tax.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1384 March 2026
```

