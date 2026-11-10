---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.14 AdditionalBalanceInformation22", "35.1.4.14.3 SubBalanceAdditionalDetails <SubBalAddtlDtls>"]
file_pages: [1426]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.14.3 SubBalanceAdditionalDetails <SubBalAddtlDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1426 to 1426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1426

```text
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity8Choice" on
page 1730 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1730
Or   Proprietary <Prtry> [1..1] ± 1731
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1] ± 1731
35.1.4.14.3  SubBalanceAdditionalDetails <SubBalAddtlDtls>
Presence: [0..1]
Definition: Provides additional subbalance information.
Datatype: "Max140Text" on page 2191
35.1.4.15  Balance21
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 1426
   Quantity <Qty> [1..1] ± 1426
35.1.4.15.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 2171
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
35.1.4.15.2  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1426 March 2026
```

