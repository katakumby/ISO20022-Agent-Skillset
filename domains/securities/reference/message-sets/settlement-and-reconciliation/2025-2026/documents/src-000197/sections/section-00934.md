---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.9 OtherAmounts32", "35.1.3.9.3 TradeAmount <TradAmt>"]
file_pages: [1370]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.9.3 TradeAmount <TradAmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1370 to 1370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1370

```text
ChargesFees <ChrgsFees> contains the following elements (see "AmountAndDirection47" on
page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.3  TradeAmount <TradAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
TradeAmount <TradAmt> contains the following elements (see "AmountAndDirection47" on
page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.4  ExecutingBrokerAmount <ExctgBrkrAmt>
Presence: [0..1]
Definition: Amount of money paid to an executing broker as a commission.
ExecutingBrokerAmount <ExctgBrkrAmt> contains the following elements (see
"AmountAndDirection47" on page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.5  LocalTax <LclTax>
Presence: [0..1]
Definition: Tax charged by the jurisdiction in which the financial instrument settles.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1370 March 2026
```

