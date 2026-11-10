---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.4 QuantityBreakdown61", "35.1.21.4.3 SecuritiesSubBalanceType <SctiesSubBalTp>"]
file_pages: [1725]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.4.3 SecuritiesSubBalanceType <SctiesSubBalTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1725 to 1725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1725

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.21.4.3  SecuritiesSubBalanceType <SctiesSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
SecuritiesSubBalanceType <SctiesSubBalTp> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.21.5  Quantity51Choice
Definition: Choice of format for the quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
35.1.21.5.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1725 March 2026
```

