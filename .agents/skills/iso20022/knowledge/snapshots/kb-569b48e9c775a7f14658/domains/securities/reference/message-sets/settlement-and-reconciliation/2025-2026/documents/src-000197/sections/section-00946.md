---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.14 OtherAmounts39", "35.1.3.14.11 Margin <Mrgn>"]
file_pages: [1382]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.14.11 Margin <Mrgn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1382 to 1382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1382

```text
LocalBrokerCommission <LclBrkrComssn> contains the following elements (see
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
35.1.3.14.11  Margin <Mrgn>
Presence: [0..1]
Definition: Amount of money deposited by the trading party in a margin account.
Margin <Mrgn> contains the following elements (see "AmountAndDirection44" on page 1375 for
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
35.1.3.14.12  Other <Othr>
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
35.1.3.14.13  RegulatoryAmount <RgltryAmt>
Presence: [0..1]
Definition: Amount of money charged by a regulatory authority, for example, Securities and Exchange
fees.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1382 March 2026
```

