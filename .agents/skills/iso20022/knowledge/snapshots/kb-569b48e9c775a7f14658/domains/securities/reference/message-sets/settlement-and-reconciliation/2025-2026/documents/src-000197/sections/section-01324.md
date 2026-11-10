---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.1 SettlementDetails220", "35.1.26.1.8 CCPEligibility <CCPElgblty>"]
file_pages: [1786]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.1.8 CCPEligibility <CCPElgblty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1786 to 1786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1786

```text
35.1.26.1.8  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 1546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.26.1.9  DeliveryReturnReason <DlvryRtrRsn>
Presence: [0..1]
Definition: Reason for a delivery return.
DeliveryReturnReason <DlvryRtrRsn> contains one of the following elements (see
"DeliveryReturn3Choice" on page 1593 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1593
Or}   Proprietary <Prtry> [1..1] ± 1594
35.1.26.1.10  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem6Choice" on page 1433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1433
Or}   Proprietary <Prtry> [1..1] ± 1433
35.1.26.1.11  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType25Choice" on
page 1529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1530
Or}   Proprietary <Prtry> [1..1] ± 1531
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1786 March 2026
```

