---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.17 RateDetails <RateDtls>", "7.4.13.22.17.2 AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties>"]
file_pages: [475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.17.2 AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 475 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 475

```text
AdditionalQuantityForSubscribedResultantSecurities <AddtlQtyForSbcbdRsltntScties> contains
one of the following elements (see "RatioFormat17Choice" on page 935 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 935
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 935
Or}   AmountToAmount <AmtToAmt> [1..1]  936
     Amount1 <Amt1> [1..1] Amount C1 936
     Amount2 <Amt2> [1..1] Amount C1 936
7.4.13.22.17.2  AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties>
Presence: [0..1]
Definition: Quantity of additional securities for a given quantity of underlying securities where underlying
securities are not exchanged or debited, for example, 1 for 1: 1 new equity credited for every 1
underlying equity = 2 resulting equities.
AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties> contains one of the following
elements (see "RatioFormat17Choice" on page 935 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 935
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 935
Or}   AmountToAmount <AmtToAmt> [1..1]  936
     Amount1 <Amt1> [1..1] Amount C1 936
     Amount2 <Amt2> [1..1] Amount C1 936
7.4.13.22.17.3  NewToOld <NewToOd>
Presence: [0..1]
Definition: Quantity of new securities for a given quantity of underlying securities, where the underlying
securities will be exchanged or debited, for example, 2 for 1: 2 new equities credited for every 1
underlying equity debited = 2 resulting equities.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 475 February 2026
```

