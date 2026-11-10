---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.3 Pension <Pnsn>", "36.4.15.5.3.7 DrawdownType <DrwdwnTp>"]
file_pages: [1175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.3.7 DrawdownType <DrwdwnTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1175 to 1175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1175

```text
Definition: Drawdown status of the pension.
DrawdownStatus <DrwdwnSts> contains one of the following elements (see
"DrawdownStatus1Choice" on page 5170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5171
Or}   Proprietary <Prtry> [1..1] ± 5171
36.4.15.5.3.7  DrawdownType <DrwdwnTp>
Presence: [0..1]
Definition: Type of drawdown tranche.
DrawdownType <DrwdwnTp> contains one of the following elements (see "DrawdownType2Choice"
on page 4791 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4791
Or}   Proprietary <Prtry> [1..1] ± 4791
36.4.15.5.3.8  NumberOfDrawdownTranches <NbOfDrwdwnTrnchs>
Presence: [0..1]
Definition: Number of drawdown tranches.
Datatype: "Number" on page 5400
36.4.15.5.3.9  EstimatedValue <EstmtdVal>
Presence: [0..1]
Definition: Estimated value of the pension policy, plan or scheme.
EstimatedValue <EstmtdVal> contains the following elements (see "DateAndAmount2" on page 4343
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
36.4.15.5.3.10  BlockTransfer <BlckTrf>
Presence: [0..1]
Definition: Indicates whether the transfer forms part of a block transfer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1175 May 2026
```

