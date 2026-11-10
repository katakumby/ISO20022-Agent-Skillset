---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.14 VariableRateSupport <VarblRateSpprt>"]
file_pages: [1028]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.14 VariableRateSupport <VarblRateSpprt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1028 to 1028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1028

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
29.4.7.14  VariableRateSupport <VarblRateSpprt>
Presence: [0..1]
Definition: Index or support rate used together with the spread to calculate the repurchase rate.
VariableRateSupport <VarblRateSpprt> contains the following elements (see "RateName1" on
page 1747 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 1747
   RateName <RateNm> [1..1] Text 1747
29.4.7.15  RepurchaseRate <RpRate>
Presence: [0..1]
Definition: Rate to be used to recalculate the repurchase amount.
Impacted by: C53 "SignRule"
RepurchaseRate <RpRate> contains the following elements (see "Rate2" on page 1748 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
29.4.7.16  StockLoanMargin <StockLnMrgn>
Presence: [0..1]
Definition: Percentage mark-up on a loan consideration used to reflect the lender's risk.
Impacted by: C53 "SignRule"
StockLoanMargin <StockLnMrgn> contains the following elements (see "Rate2" on page 1748 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1028 March 2026
```

