---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.14 OtherAmounts39", "35.1.3.14.20 ValueAddedTax <ValAddedTax>"]
file_pages: [1385]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.14.20 ValueAddedTax <ValAddedTax>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1385 to 1385.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1385

```text
TransactionTax <TxTax> contains the following elements (see "AmountAndDirection44" on page 1375
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
35.1.3.14.20  ValueAddedTax <ValAddedTax>
Presence: [0..1]
Definition: Amount of value-added tax.
ValueAddedTax <ValAddedTax> contains the following elements (see "AmountAndDirection44" on
page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.14.21  WithholdingTax <WhldgTax>
Presence: [0..1]
Definition: Amount of money that will be withheld by a tax authority.
WithholdingTax <WhldgTax> contains the following elements (see "AmountAndDirection44" on
page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.14.22  NetGainLoss <NetGnLoss>
Presence: [0..1]
Definition: Amount representing the difference between the cost and the current price of a security. In
the context of securities settlement, it is the amount paid or received when the instructions are netted or
paired off.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1385 March 2026
```

