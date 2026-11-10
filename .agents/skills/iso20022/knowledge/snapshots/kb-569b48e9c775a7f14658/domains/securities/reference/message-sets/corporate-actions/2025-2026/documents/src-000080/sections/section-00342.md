---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.1 SecurityDetails <SctyDtls>", "7.4.13.22.1.22 ContractSize <CtrctSz>"]
file_pages: [465]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.1.22 ContractSize <CtrctSz>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 465 to 465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 465

```text
MinimumMultipleQuantityToInstruct <MinMltplQtyToInst> contains one of the following elements
(see "FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.13.22.1.22  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a financial instrument quantity.
Impacted by: C19 "DigitalTokenUnitUsageRule"
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
7.4.13.22.1.23  IssuePrice <IssePric>
Presence: [0..1]
Definition: Initial issue/valuation price of a resulting security under a corporate action.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 465 February 2026
```

