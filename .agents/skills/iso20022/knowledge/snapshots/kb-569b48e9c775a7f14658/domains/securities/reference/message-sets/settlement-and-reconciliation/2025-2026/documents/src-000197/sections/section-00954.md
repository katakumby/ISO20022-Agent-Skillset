---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.16 OtherAmounts47", "35.1.3.16.2 ChargesFees <ChrgsFees>"]
file_pages: [1390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.16.2 ChargesFees <ChrgsFees>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1390 to 1390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1390

```text
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.16.2  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Amount of money paid for the provision of financial services that cannot be categorised by
another qualifier.
ChargesFees <ChrgsFees> contains the following elements (see "AmountAndDirection44" on
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
35.1.3.16.3  CountryNationalFederalTax <CtryNtlFdrlTax>
Presence: [0..1]
Definition: Amount of country, national or federal tax charged by the jurisdiction in which the account
servicer is located.
CountryNationalFederalTax <CtryNtlFdrlTax> contains the following elements (see
"AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
35.1.3.16.4  TradeAmount <TradAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1390 March 2026
```

