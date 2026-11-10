---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>", "2.4.2.2 NewCriteria <NewCrit>", "2.4.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.3.2 CashAccountServicerIndicator <CshAcctSvcrInd>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2.2.3.2 CashAccountServicerIndicator <CshAcctSvcrInd>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
2.4.2.2.3.2  CashAccountServicerIndicator <CshAcctSvcrInd>
Presence: [0..1]
Definition: Indicates whether the cash account servicer information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.3.3  SecuritiesAccountOwnerIndicator <SctiesAcctOwnrInd>
Presence: [0..1]
Definition: Indicates whether the securities account owner information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.3.4  SecuritiesAccountServicerIndicator <SctiesAcctSvcrInd>
Presence: [0..1]
Definition: Indicates whether the securities account servicer information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.3.5  TotalCollateralValuationIndicator <TtlCollValtnInd>
Presence: [0..1]
Definition: Indicates whether the total value of the collateral valuation information is requested..
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.3.6  SecuritiesAccountIndicator <SctiesAcctInd>
Presence: [0..1]
Definition: Indicates whether the securities account information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.3.7  Securities <Scties>
Presence: [0..1]
Definition: Indicates whether the securities account information is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 81):
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
14 March 2024
```

