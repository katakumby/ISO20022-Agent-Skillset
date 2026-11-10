---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.2 Structure"]
file_pages: [233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.2 Structure

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 233 to 233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
D. ReportSummary
Provides details on the valuation of the collateral on deposit.
E. ReportDetails
Provides the margin report details.
F. SupplementaryData
Additional information that can't be captured in the structured fields and/or any other specific block.
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <MrgnRpt> [1..1]  
   ReportParameters <RptParams> [1..1]  C14 237
     ReportIdentification <RptId> [1..1] Text 238
     ReportDateAndTime <RptDtAndTm> [1..1] ± 238
     ReportCurrency <RptCcy> [1..1] CodeSet C16 238
     CalculationDateAndTime <ClctnDtAndTm> [1..1] DateTime 238
     Frequency <Frqcy> [1..1] CodeSet 238
     ReportNumber <RptNb> [0..1] Text 239
   Pagination <Pgntn> [1..1] ± 239
   ClearingMember <ClrMmb> [1..1] ± 239
   ReportSummary <RptSummry> [0..1] ± 239
   ReportDetails <RptDtls> [1..*]  240
     MarginProduct <MrgnPdct> [0..*]  240
{Or       Code <Cd> [1..1] CodeSet 241
Or}       Proprietary <Prtry> [1..1] ± 241
     MarginAccount <MrgnAcct> [1..1] ± 241
     CollateralisedMarginAccountIndicator <CollsdMrgnAcctInd> [0..1] Indicator 241
     NonClearingMember <NonClrMmb> [0..*] ± 242
     MarginCalculationSummary <MrgnClctnSummry> [0..1] ± 242
     MarginCalculation <MrgnClctn> [1..*] ±   'C12 242
   SupplementaryData <SplmtryData> [0..*] ± C15 245
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 233
```

