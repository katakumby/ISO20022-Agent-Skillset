---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.13 SettledAmount <SttldAmt>"]
file_pages: [1048]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.13 SettledAmount <SttldAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1048 to 1048.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1048

```text
29.4.13 SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount effectively settled and which will be credited to/debited from the account owner's
cash account. It may differ from the instructed settlement amount based on market tolerance level.
SettledAmount <SttldAmt> contains the following elements (see "AmountAndDirection94" on
page 1365 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1365
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1366
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1366
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1366
   Amount <Amt> [1..1] Amount C1, C9 1366
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1367
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1367
   ForeignExchangeDetails <FXDtls> [0..1] ± 1367
   ValueDate <ValDt> [0..1] ± 1368
29.4.14 OtherAmounts <OthrAmts>
Presence: [0..1]
Definition: Other amounts than the settlement amount.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1048 March 2026
```

