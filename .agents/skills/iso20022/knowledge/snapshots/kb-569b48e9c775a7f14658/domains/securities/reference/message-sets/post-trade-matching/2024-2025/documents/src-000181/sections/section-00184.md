---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.16 ValueAddedTax <ValAddedTax>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.16 ValueAddedTax <ValAddedTax>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
TransactionTax <TxTax> contains the following elements (see "AmountAndDirection29" on page 228
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.16  ValueAddedTax <ValAddedTax>
Presence: [0..1]
Definition: Amount of value-added tax.
ValueAddedTax <ValAddedTax> contains the following elements (see "AmountAndDirection29" on
page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.17  WithholdingTax <WhldgTax>
Presence: [0..1]
Definition: Amount of money that will be withheld by a tax authority.
WithholdingTax <WhldgTax> contains the following elements (see "AmountAndDirection29" on
page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.18  NetGainLoss <NetGnLoss>
Presence: [0..1]
Definition: Amount representing the difference between the cost and the current price of a security. In
the context of securities settlement, it is the amount paid or received when the instructions are netted or
paired off.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 237 February 2025
```

