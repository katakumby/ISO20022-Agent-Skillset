---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.2 Quantity48"]
file_pages: [1721]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.2 Quantity48

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1721 to 1721.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1721

```text
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
35.1.21.2  Quantity48
Definition: Details on the quantity, account and other related information involved in a transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1721
   DenominationChoice <DnmtnChc> [0..1] Text 1721
   CertificateNumber <CertNb> [0..*] ± C19 1721
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1722
35.1.21.2.1  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
SettlementQuantity <SttlmQty> contains one of the following elements (see
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
35.1.21.2.2  DenominationChoice <DnmtnChc>
Presence: [0..1]
Definition: Denomination of the security to be received or delivered.
Datatype: "Max210Text" on page 2191
35.1.21.2.3  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Impacted by: C19 "ISO8532AndIssuerSchemeNameRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1721 March 2026
```

