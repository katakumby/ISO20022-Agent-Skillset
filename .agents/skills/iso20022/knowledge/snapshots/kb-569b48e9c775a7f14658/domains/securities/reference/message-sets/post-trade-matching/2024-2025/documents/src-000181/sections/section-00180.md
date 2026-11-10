---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.3 ExecutingBrokerAmount <ExctgBrkrAmt>"]
file_pages: [233]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.3 ExecutingBrokerAmount <ExctgBrkrAmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 233 to 233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
7.1.3.3.3  ExecutingBrokerAmount <ExctgBrkrAmt>
Presence: [0..1]
Definition: Amount of money paid to an executing broker as a commission.
ExecutingBrokerAmount <ExctgBrkrAmt> contains the following elements (see
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
7.1.3.3.4  IssueDiscountAllowance <IsseDscntAllwnc>
Presence: [0..1]
Definition: Amount of money defined as a discount on a new issue or on a tranche of an existing issue.
IssueDiscountAllowance <IsseDscntAllwnc> contains the following elements (see
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
7.1.3.3.5  PaymentLevyTax <PmtLevyTax>
Presence: [0..1]
Definition: Amount of payment levy tax.
PaymentLevyTax <PmtLevyTax> contains the following elements (see "AmountAndDirection29" on
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 233 February 2025
```

