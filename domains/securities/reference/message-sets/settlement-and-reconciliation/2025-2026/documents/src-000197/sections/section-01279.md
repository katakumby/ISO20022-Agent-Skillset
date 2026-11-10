---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.13 BalanceQuantity14Choice", "35.1.21.13.2 Proprietary <Prtry>"]
file_pages: [1736]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.13.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1736 to 1736.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1736

```text
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.21.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 1505 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1505
   Issuer <Issr> [1..1] Text 1505
   SchemeName <SchmeNm> [0..1] Text 1505
   Balance <Bal> [1..1] Quantity 1506
35.1.21.14  QuantityBreakdown63
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1736
   LotQuantity <LotQty> [0..1] ± C12 1737
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1737
   LotDateTime <LotDtTm> [0..1] ± 1737
   LotPrice <LotPric> [0..1] ± 1738
   TypeOfPrice <TpOfPric> [0..1] ± 1738
35.1.21.14.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 1498 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1736 March 2026
```

