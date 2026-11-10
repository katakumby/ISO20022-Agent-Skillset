---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.14 QuantityBreakdown63", "35.1.21.14.2 LotQuantity <LotQty>"]
file_pages: [1737]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.14.2 LotQuantity <LotQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1737 to 1737.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1737

```text
35.1.21.14.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
Impacted by: C12 "DigitalTokenUnitUsageRule"
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.21.14.3  SecuritiesSubBalanceType <SctiesSubBalTp>
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
35.1.21.14.4  LotDateTime <LotDtTm>
Presence: [0..1]
Definition: Date/time at which the lot was purchased.
LotDateTime <LotDtTm> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1737 March 2026
```

