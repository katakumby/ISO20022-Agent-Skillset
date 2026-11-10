---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.18 OtherAmounts <OthrAmts>", "31.4.6.18.6 Other <Othr>"]
file_pages: [1124]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.18.6 Other <Othr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1124 to 1124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1124

```text
LocalTax <LclTax> contains the following elements (see "AmountAndDirection44" on page 1375 for
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
31.4.6.18.6  Other <Othr>
Presence: [0..1]
Definition: An amount that is not indicated by a known business denomination.
Other <Othr> contains the following elements (see "AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
31.4.6.18.7  RegulatoryAmount <RgltryAmt>
Presence: [0..1]
Definition: Amount of money charged by a regulatory authority, for example, Securities and Exchange
fees.
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
31.4.6.18.8  ShippingAmount <ShppgAmt>
Presence: [0..1]
Definition: All costs related to the physical delivery of documents such as stamps, postage, carrier fees,
insurances or messenger services.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1124 March 2026
```

