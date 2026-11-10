---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.2 Quantity48", "35.1.21.2.4 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [1722]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.2.4 QuantityBreakdown <QtyBrkdwn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1722 to 1722.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1722

```text
CertificateNumber <CertNb> contains the following elements (see "SecuritiesCertificate4" on
page 1630 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 1631
   Issuer <Issr> [0..1] Text 1631
   SchemeName <SchmeNm> [0..1] Text 1631
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
35.1.21.2.4  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown62" on
page 1733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1733
   LotQuantity <LotQty> [0..1] ± C12 1734
   LotDateTime <LotDtTm> [0..1] ± 1734
   LotPrice <LotPric> [0..1] ± 1734
   TypeOfPrice <TpOfPric> [0..1] ± 1735
35.1.21.3  QuantityBreakdown57
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1722
   LotQuantity <LotQty> [0..1] ± 1723
   LotDateTime <LotDtTm> [0..1] ± 1723
   LotPrice <LotPric> [0..1] ± 1723
   TypeOfPrice <TpOfPric> [0..1] ± 1723
35.1.21.3.1  LotNumber <LotNb>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1722 March 2026
```

