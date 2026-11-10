---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.9 IntermediateSecurity <IntrmdtScty>", "3.4.9.3 RenounceableEntitlementStatusType <RnncblEntitlmntStsTp>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.9.3 RenounceableEntitlementStatusType <RnncblEntitlmntStsTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
Datatype: "DecimalNumber" on page 1246
3.4.9.3  RenounceableEntitlementStatusType <RnncblEntitlmntStsTp>
Presence: [0..1]
Definition: Specifies whether terms of the event allow resale of the rights.
RenounceableEntitlementStatusType <RnncblEntitlmntStsTp> contains one of the following
elements (see "RenounceableEntitlementStatusTypeFormat3Choice" on page 943 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 943
Or}   Proprietary <Prtry> [1..1] ± 943
3.4.9.4  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType25Choice" on page 920 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 920
Or}   Proprietary <Prtry> [1..1] ± 920
3.4.9.5  IntermediateSecuritiesToUnderlyingRatio <IntrmdtSctiesToUndrlygRatio>
Presence: [0..1]
Definition: Quantity of intermediate securities awarded for a given quantity of underlying security.
IntermediateSecuritiesToUnderlyingRatio <IntrmdtSctiesToUndrlygRatio> contains the following
elements (see "QuantityToQuantityRatio1" on page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
3.4.9.6  MarketPrice <MktPric>
Presence: [0..1]
Definition: Last reported/known price of a financial instrument in a market.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 89 February 2026
```

