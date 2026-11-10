---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.24 AccruedInterestAmount <AcrdIntrstAmt>"]
file_pages: [1031]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.24 AccruedInterestAmount <AcrdIntrstAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1031 to 1031.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1031

```text
DealAmount <DealAmt> contains the following elements (see "AmountAndDirection21" on page 1377
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
29.4.7.24  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
29.4.7.25  ForfeitAmount <FrftAmt>
Presence: [0..1]
Definition: Fixed amount of money that has to be paid (instead of interest) in the case of a recall or at
the closing date.
ForfeitAmount <FrftAmt> contains the following elements (see "AmountAndDirection21" on
page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
29.4.7.26  PremiumAmount <PrmAmt>
Presence: [0..1]
Definition: Difference between the amount of money of the first leg and the amount of the second leg of
the transaction.
PremiumAmount <PrmAmt> contains the following elements (see "AmountAndDirection21" on
page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1031 March 2026
```

