---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.18 OtherAmounts <OthrAmts>", "31.4.6.18.3 CountryNationalFederalTax <CtryNtlFdrlTax>"]
file_pages: [1123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.18.3 CountryNationalFederalTax <CtryNtlFdrlTax>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1123 to 1123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1123

```text
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
31.4.6.18.3  CountryNationalFederalTax <CtryNtlFdrlTax>
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
31.4.6.18.4  PaymentLevyTax <PmtLevyTax>
Presence: [0..1]
Definition: Amount of payment levy tax.
PaymentLevyTax <PmtLevyTax> contains the following elements (see "AmountAndDirection44" on
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
31.4.6.18.5  LocalTax <LclTax>
Presence: [0..1]
Definition: Tax charged by the jurisdiction in which the financial instrument settles.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1123 March 2026
```

