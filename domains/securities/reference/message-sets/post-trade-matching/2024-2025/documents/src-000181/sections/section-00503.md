---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.10 CashClearingSystem <CshClrSys>"]
file_pages: [577]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.10 CashClearingSystem <CshClrSys>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 577 to 577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 577

```text
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 301 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 301
Or}   Proprietary <Prtry> [1..1] ± 302
7.1.27.1.10  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, eg, cheque clearing.
CashClearingSystem <CshClrSys> contains one of the following elements (see
"CashSettlementSystem4Choice" on page 247 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 247
Or}   Proprietary <Prtry> [1..1] ± 247
7.1.27.1.11  ExposureType <XpsrTp>
Presence: [0..1]
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
ExposureType <XpsrTp> contains one of the following elements (see "ExposureType18Choice" on
page 374 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 374
Or}   Proprietary <Prtry> [1..1] ± 376
7.1.27.1.12  FXStandingInstruction <FxStgInstr>
Presence: [0..1]
Definition: Specifies whether the forex standing instruction in place should apply.
FXStandingInstruction <FxStgInstr> contains one of the following elements (see
"FXStandingInstruction4Choice" on page 320 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 320
Or}   Proprietary <Prtry> [1..1] ± 320
7.1.27.1.13  CurrencyToBuyOrSell <CcyToBuyOrSell>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 577 February 2025
```

