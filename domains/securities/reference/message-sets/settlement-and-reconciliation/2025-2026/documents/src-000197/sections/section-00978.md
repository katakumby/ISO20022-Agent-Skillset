---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.4 ClosingBalance6Choice"]
file_pages: [1414]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.4 ClosingBalance6Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1414 to 1414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1414

```text
35.1.4.4  ClosingBalance6Choice
Definition: Choice of closing balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Final <Fnl> [1..1] ± 1414
Or}   Intermediary <Intrmy> [1..1] ± 1414
35.1.4.4.1  Final <Fnl>
Presence: [1..1]
Definition: Sum of the opening balance and all entries booked to the account at the close of the
statement period.
Final <Fnl> contains one of the following elements (see "BalanceQuantity14Choice" on page 1735 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.4.4.2  Intermediary <Intrmy>
Presence: [1..1]
Definition: Closing balance of this page only. This balance must be the intermediary opening balance of
the next page of the same statement.
Intermediary <Intrmy> contains one of the following elements (see "BalanceQuantity14Choice" on
page 1735 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1735
Or}   Proprietary <Prtry> [1..1] ± 1736
35.1.4.5  SubBalanceInformation20
Definition: Net position of a segregated holding of a single security within the overall position held in the
securities account, for example, sub-balance per status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SubBalanceType <SubBalTp> [1..1] ± 1415
   Quantity <Qty> [1..1] ± 1415
   SubBalanceAdditionalDetails <SubBalAddtlDtls> [0..1] Text 1415
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1415
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± C19,
C40
1416
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1414 March 2026
```

