---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.10 SettlementDetails222", "35.1.26.10.9 ExposureType <XpsrTp>"]
file_pages: [1847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.10.9 ExposureType <XpsrTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1847 to 1847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1847

```text
35.1.26.10.9  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 1529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1530
Or}   Proprietary <Prtry> [1..1] ± 1531
35.1.26.10.10  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem6Choice" on page 1433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1433
Or}   Proprietary <Prtry> [1..1] ± 1433
35.1.26.10.11  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1564
Or}   Proprietary <Prtry> [1..1] ± 1564
35.1.26.10.12  RepurchaseType <RpTp>
Presence: [0..1]
Definition: Specifies whether the rate is fixed, variable or a forfeit.
RepurchaseType <RpTp> contains one of the following elements (see "RepurchaseType22Choice" on
page 1579 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1580
Or}   Proprietary <Prtry> [1..1] ± 1580
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1847 March 2026
```

