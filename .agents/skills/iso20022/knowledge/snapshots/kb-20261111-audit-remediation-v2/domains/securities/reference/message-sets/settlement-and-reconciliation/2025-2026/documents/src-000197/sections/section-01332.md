---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.2 SettlementDetails234", "35.1.26.2.6 CashClearingSystem <CshClrSys>"]
file_pages: [1794]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.2.6 CashClearingSystem <CshClrSys>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1794 to 1794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1794

```text
Definition: Specifies whether there is change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 1600 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1600
Or}   Proprietary <Prtry> [1..1] ± 1600
35.1.26.2.6  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem6Choice" on page 1433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1433
Or}   Proprietary <Prtry> [1..1] ± 1433
35.1.26.2.7  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 1525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1525
Or}   Proprietary <Prtry> [1..1] ± 1525
35.1.26.2.8  Registration <Regn>
Presence: [0..1]
Definition: Specifies whether registration should occur upon receipt.
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 1623
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1623
Or}   Proprietary <Prtry> [1..1] ± 1623
35.1.26.2.9  RepurchaseType <RpTp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1794 March 2026
```

