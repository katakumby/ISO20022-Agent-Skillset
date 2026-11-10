---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.19 ConsumptionTax <CsmptnTax>"]
file_pages: [238]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.19 ConsumptionTax <CsmptnTax>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 238 to 238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
NetGainLoss <NetGnLoss> contains the following elements (see "AmountAndDirection29" on
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
7.1.3.3.19  ConsumptionTax <CsmptnTax>
Presence: [0..1]
Definition: A tax on spending on goods and services.
ConsumptionTax <CsmptnTax> contains the following elements (see "AmountAndDirection29" on
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
7.1.3.3.20  MatchingConfirmationFee <MtchgConfFee>
Presence: [0..1]
Definition: Amount of money charged for matching and/or confirmation.
MatchingConfirmationFee <MtchgConfFee> contains the following elements (see
"AmountAndDirection29" on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.21  ConvertedAmount <ConvtdAmt>
Presence: [0..1]
Definition: Amount following a foreign exchange conversion.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 238 February 2025
```

