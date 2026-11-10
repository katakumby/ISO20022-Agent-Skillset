---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.6 Price10"]
file_pages: [1712]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.6 Price10

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1712 to 1712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1712

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.20.6  Price10
Definition: Type and information about a price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1712
{Or     Yielded <Yldd> [1..1] Indicator 1712
Or}     ValueType <ValTp> [1..1] CodeSet 1712
   Value <Val> [1..1] ± 1713
35.1.20.6.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Type <Tp> contains one of the following YieldedOrValueType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 1712
Or}   ValueType <ValTp> [1..1] CodeSet 1712
35.1.20.6.1.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.20.6.1.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType12Code" on page 2111
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1712 March 2026
```

