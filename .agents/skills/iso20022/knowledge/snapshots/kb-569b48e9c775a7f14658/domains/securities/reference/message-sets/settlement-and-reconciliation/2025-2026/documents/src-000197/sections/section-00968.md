---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.17 OtherAmounts45", "35.1.3.17.14 ShippingAmount <ShppgAmt>"]
file_pages: [1404]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.17.14 ShippingAmount <ShppgAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1404 to 1404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1404

```text
RegulatoryAmount <RgltryAmt> contains the following elements (see "AmountAndDirection44" on
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
35.1.3.17.14  ShippingAmount <ShppgAmt>
Presence: [0..1]
Definition: All costs related to the physical delivery of documents such as stamps, postage, carrier fees,
insurances or messenger services.
ShippingAmount <ShppgAmt> contains the following elements (see "AmountAndDirection44" on
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
35.1.3.17.15  SpecialConcession <SpclCncssn>
Presence: [0..1]
Definition: Amount of drawdown or other reduction from or in addition to the deal price.
SpecialConcession <SpclCncssn> contains the following elements (see "AmountAndDirection44" on
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
35.1.3.17.16  StampDuty <StmpDty>
Presence: [0..1]
Definition: Amount of stamp duty.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1404 March 2026
```

