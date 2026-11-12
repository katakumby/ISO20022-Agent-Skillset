---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.5 SettlementDetails230", "35.1.26.5.9 MarketClientSide <MktClntSd>"]
file_pages: [1813]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.5.9 MarketClientSide <MktClntSd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1813 to 1813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1813

```text
FXStandingInstruction <FxStgInstr> contains one of the following elements (see
"FXStandingInstruction4Choice" on page 1561 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1562
Or}   Proprietary <Prtry> [1..1] ± 1562
35.1.26.5.9  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 1525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1525
Or}   Proprietary <Prtry> [1..1] ± 1525
35.1.26.5.10  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 1548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1548
Or}   Proprietary <Prtry> [1..1] ± 1549
35.1.26.5.11  Registration <Regn>
Presence: [0..1]
Definition: Specifies whether registration should occur upon receipt.
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 1623
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1623
Or}   Proprietary <Prtry> [1..1] ± 1623
35.1.26.5.12  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1813 March 2026
```

