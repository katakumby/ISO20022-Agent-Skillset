---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "colr.002.001.02"
message_family: "colr.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.002.001.02"
source_ids: ["src-000233", "src-000357"]
source_locations: [{"source_id": "src-000233", "heading": "25 colr.002.001.02 CollateralValueReportV02", "file_pages": [590, 613]}, {"source_id": "src-000357", "heading": "3 colr.002.001.02 CollateralValueReportV02", "file_pages": [16, 39]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# colr.002.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 25 colr.002.001.02 CollateralValueReportV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp590–613; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 25 colr.002.001.02 CollateralValueReportV02, Functionality, file p590.**

The CollateralValueReport message is sent by the system transaction administrator to a system
member (such as a directly connected party) to provide further information the current available value of
securities for auto collateralisation for one specific or several cash accounts.
Outline
The CollateralValueReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the collateral value report message.
B. ReportOrError
Report on collateral value information or operational error.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 590 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [25 colr.002.001.02 CollateralValueReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00468.md) | 590–590 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00469.md) | 591–591 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00470.md) | 592–593 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00471.md) | 594–595 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00472.md) | 596–597 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00473.md) | 598–598 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00474.md) | 599–599 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.4 SecuritiesAccountOwner &lt;SctiesAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00475.md) | 600–600 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00476.md) | 601–602 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.1 BusinessError &lt;BizErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00477.md) | 603–603 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.1 DataAccessTime &lt;DataAccsTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00478.md) | 604–604 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.3 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00479.md) | 605–605 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00480.md) | 606–606 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.2 Position &lt;Pos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00481.md) | 607–607 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 25.4.2.1.6.2.4.2.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00482.md) | 608–608 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 25.4.2.1.6.2.4.2.2 Quantity &lt;Qty&gt; / 25.4.2.1.6.2.4.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00483.md) | 609–609 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 25.4.2.1.6.2.4.2.2 Quantity &lt;Qty&gt; / 25.4.2.1.6.2.4.2.2.3 QuantityAndAvailability &lt;QtyAndAvlbty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00484.md) | 610–610 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.3 ValuationPrice &lt;ValtnPric&gt; / 25.4.2.1.6.2.4.3.1 AmountPriceType &lt;AmtPricTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00485.md) | 611–611 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.1 BusinessReport &lt;BizRpt&gt; / 25.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 25.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 25.4.2.1.6.2.4 Securities &lt;Scties&gt; / 25.4.2.1.6.2.4.3 ValuationPrice &lt;ValtnPric&gt; / 25.4.2.1.6.2.4.3.4 PriceFixingDate &lt;PricFxgDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00486.md) | 612–612 |
| [25 colr.002.001.02 CollateralValueReportV02 / 25.4 Message Building Blocks / 25.4.2 ReportOrError &lt;RptOrErr&gt; / 25.4.2.2 OperationalError &lt;OprlErr&gt; / 25.4.2.2.1 Error &lt;Err&gt; / 25.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00487.md) | 613–613 |

## src-000357 — 3 colr.002.001.02 CollateralValueReportV02

[src-000357](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`; file pp16–39; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000357, 3 colr.002.001.02 CollateralValueReportV02, Functionality, file p16.**

The CollateralValueReport message is sent by the system transaction administrator to a system
member (such as a directly connected party) to provide further information the current available value of
securities for auto collateralisation for one specific or several cash accounts.
Outline
The CollateralValueReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the collateral value report message.
B. ReportOrError
Report on collateral value information or operational error.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
16 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 colr.002.001.02 CollateralValueReportV02](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00016.md) | 16–16 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.2 Structure](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00017.md) | 17–17 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.3 Constraints](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00018.md) | 18–19 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00019.md) | 20–21 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00020.md) | 22–23 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00021.md) | 24–24 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00022.md) | 25–25 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.4 SecuritiesAccountOwner &lt;SctiesAcctOwnr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00023.md) | 26–26 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00024.md) | 27–28 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.1 BusinessError &lt;BizErr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00025.md) | 29–29 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.1 DataAccessTime &lt;DataAccsTm&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00026.md) | 30–30 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.3 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00027.md) | 31–31 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.1 Identification &lt;Id&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00028.md) | 32–32 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.2 Position &lt;Pos&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00029.md) | 33–33 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 3.4.2.1.6.2.4.2.1 Type &lt;Tp&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00030.md) | 34–34 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 3.4.2.1.6.2.4.2.2 Quantity &lt;Qty&gt; / 3.4.2.1.6.2.4.2.2.1 Quantity &lt;Qty&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00031.md) | 35–35 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.2 Position &lt;Pos&gt; / 3.4.2.1.6.2.4.2.2 Quantity &lt;Qty&gt; / 3.4.2.1.6.2.4.2.2.3 QuantityAndAvailability &lt;QtyAndAvlbty&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00032.md) | 36–36 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.3 ValuationPrice &lt;ValtnPric&gt; / 3.4.2.1.6.2.4.3.1 AmountPriceType &lt;AmtPricTp&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00033.md) | 37–37 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 BusinessReport &lt;BizRpt&gt; / 3.4.2.1.6 CollateralValueReport &lt;CollValRpt&gt; / 3.4.2.1.6.2 CollateralValue &lt;CollVal&gt; / 3.4.2.1.6.2.4 Securities &lt;Scties&gt; / 3.4.2.1.6.2.4.3 ValuationPrice &lt;ValtnPric&gt; / 3.4.2.1.6.2.4.3.4 PriceFixingDate &lt;PricFxgDt&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00034.md) | 38–38 |
| [3 colr.002.001.02 CollateralValueReportV02 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.2 OperationalError &lt;OprlErr&gt; / 3.4.2.2.1 Error &lt;Err&gt; / 3.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00035.md) | 39–39 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000356-central-securities-depositories-csd.md) | participant | src-000356 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000356-executing-servicing-party.md) | participant | src-000356 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000356-instructing-party.md) | participant | src-000356 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000356-national-central-bank-ncb.md) | participant | src-000356 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000356-national-central-bank.md) | participant | src-000356 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000356-payment-bank.md) | participant | src-000356 |
| [Settlement Infrastructure Direct Participant](../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure-direct-participant.md) | participant | src-000356 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000356-settlement-infrastructure.md) | participant | src-000356 |
| [System Member](../../../../../shared/reference/participants/participant-src-000356-system-member.md) | participant | src-000356 |
| [System Transaction Administrator](../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md) | participant | src-000356 |
| [T2S operator](../../../../../shared/reference/participants/participant-src-000356-t2s-operator.md) | participant | src-000356 |
| [Query Management Process](../../message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md) | business-flow | src-000356 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
