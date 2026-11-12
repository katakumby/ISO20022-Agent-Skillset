---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks", "6.4.5 ReportDetails <RptDtls>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4.5 ReportDetails <RptDtls>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
ReportSummary <RptSummry> contains the following elements (see MarginCalculation1 on
page 430 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalMarginAmount <TtlMrgnAmt> [1..1] ± 431
   CollateralOnDeposit <CollOnDpst> [0..*] ± 431
   MinimumRequirementDeposit <MinRqrmntDpst> [0..1] Amount   'C1,
  'C7
431
   MarginResult <MrgnRslt> [0..1]  432
{Or     ExcessAmount <XcssAmt> [1..1] Amount   'C1,
  'C7
432
Or}     DeficitAmount <DfcitAmt> [1..1] Amount   'C1,
  'C7
433
6.4.5 ReportDetails <RptDtls>
Presence: [1..*]
Definition: Provides the margin report details.
ReportDetails <RptDtls> contains the following MarginReport2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarginProduct <MrgnPdct> [0..*]  240
{Or     Code <Cd> [1..1] CodeSet 241
Or}     Proprietary <Prtry> [1..1] ± 241
   MarginAccount <MrgnAcct> [1..1] ± 241
   CollateralisedMarginAccountIndicator
<CollsdMrgnAcctInd>
[0..1] Indicator 241
   NonClearingMember <NonClrMmb> [0..*] ± 242
   MarginCalculationSummary <MrgnClctnSummry> [0..1] ± 242
   MarginCalculation <MrgnClctn> [1..*] ±   'C12 242
6.4.5.1  MarginProduct <MrgnPdct>
Presence: [0..*]
Definition: Specifies if the margin is related to equities or fixed income.
MarginProduct <MrgnPdct> contains one of the following MarginProductType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 241
Or}   Proprietary <Prtry> [1..1] ± 241
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 240
```

