---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.1 SettlementDetails220", "35.1.26.1.16 RepurchaseType <RpTp>"]
file_pages: [1788]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.1.16 RepurchaseType <RpTp>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1788 to 1788.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1788

```text
35.1.26.1.16  RepurchaseType <RpTp>
Presence: [0..1]
Definition: Specifies the type of repurchase transaction.
RepurchaseType <RpTp> contains one of the following elements (see "RepurchaseType23Choice" on
page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1573
Or}   Proprietary <Prtry> [1..1] ± 1573
35.1.26.1.17  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 1551 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
35.1.26.1.18  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 1554 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1554
Or}   Proprietary <Prtry> [1..1] ± 1554
35.1.26.1.19  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Definition: Role of a party in the settlement of the transaction.
SettlingCapacity <SttlgCpcty> contains one of the following elements (see "SettlingCapacity7Choice"
on page 1631 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1631
Or}   Proprietary <Prtry> [1..1] ± 1632
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1788 March 2026
```

