---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.5 SecuritiesFinancingAdditionalDetails <SctiesFincgAddtlDtls>", "30.4.5.17 SecuritiesHaircut <SctiesHrcut>"]
file_pages: [1076]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.5.17 SecuritiesHaircut <SctiesHrcut>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1076 to 1076.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1076

```text
Constraints
• SignRule
When Sign is present, rate must not be zero.
30.4.5.17  SecuritiesHaircut <SctiesHrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Impacted by: C34 "SignRule"
SecuritiesHaircut <SctiesHrcut> contains the following elements (see "Rate2" on page 1748 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
30.4.5.18  ChargesRate <ChrgsRate>
Presence: [0..1]
Definition: Interest rate paid in the context of a securities financing transaction.
Impacted by: C34 "SignRule"
ChargesRate <ChrgsRate> contains the following elements (see "Rate2" on page 1748 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
30.4.5.19  PricingRate <PricgRate>
Presence: [0..1]
Definition: Interest rate to be paid on the transaction amount, as agreed between the counterparties.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1076 March 2026
```

