---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "colr.001.001.02"
message_family: "colr.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.001.001.02"
source_ids: ["src-000233", "src-000357"]
source_locations: [{"source_id": "src-000233", "heading": "24 colr.001.001.02 CollateralValueQueryV02", "file_pages": [578, 589]}, {"source_id": "src-000357", "heading": "2 colr.001.001.02 CollateralValueQueryV02", "file_pages": [4, 15]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# colr.001.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 24 colr.001.001.02 CollateralValueQueryV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp578–589; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 24 colr.001.001.02 CollateralValueQueryV02, Functionality, file p578.**

The CollateralValueQuery message is sent by a system member (such as a directly connected party) to
the system transaction administrator to query the current available value of securities for auto
collateralisation for one specific or several cash accounts.
Outline
The CollateralValueQueryV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the collateral value query message.
B. CollateralValueQueryDefinition
Definition of the collateral query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 578 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [24 colr.001.001.02 CollateralValueQueryV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00456.md) | 578–578 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00457.md) | 579–579 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00458.md) | 580–580 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00459.md) | 581–581 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.1 QueryName &lt;QryNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00460.md) | 582–582 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00461.md) | 583–583 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.1 CashAccountIdentification &lt;CshAcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00462.md) | 584–584 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.3 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00463.md) | 585–585 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.6 SecuritiesAccountOwner &lt;SctiesAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00464.md) | 586–586 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 24.4.2.2.2.7 SecuritiesAccountServicer &lt;SctiesAcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00465.md) | 587–587 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 24.4.2.2 NewCriteria &lt;NewCrit&gt; / 24.4.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 24.4.2.2.3.2 CashAccountServicerIndicator &lt;CshAcctSvcrInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00466.md) | 588–588 |
| [24 colr.001.001.02 CollateralValueQueryV02 / 24.4 Message Building Blocks / 24.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00467.md) | 589–589 |

## src-000357 — 2 colr.001.001.02 CollateralValueQueryV02

[src-000357](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`; file pp4–15; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000357, 2 colr.001.001.02 CollateralValueQueryV02, Functionality, file p4.**

The CollateralValueQuery message is sent by a system member (such as a directly connected party) to
the system transaction administrator to query the current available value of securities for auto
collateralisation for one specific or several cash accounts.
Outline
The CollateralValueQueryV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the collateral value query message.
B. CollateralValueQueryDefinition
Definition of the collateral query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
4 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 colr.001.001.02 CollateralValueQueryV02](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00004.md) | 4–4 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.2 Structure](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00005.md) | 5–5 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00006.md) | 6–6 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00007.md) | 7–7 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.1 QueryName &lt;QryNm&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00008.md) | 8–8 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00009.md) | 9–9 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.1 CashAccountIdentification &lt;CshAcctId&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00010.md) | 10–10 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.3 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00011.md) | 11–11 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.6 SecuritiesAccountOwner &lt;SctiesAcctOwnr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00012.md) | 12–12 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.7 SecuritiesAccountServicer &lt;SctiesAcctSvcr&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00013.md) | 13–13 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.2 CollateralValueQueryDefinition &lt;CollValQryDef&gt; / 2.4.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.3.2 CashAccountServicerIndicator &lt;CshAcctSvcrInd&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00014.md) | 14–14 |
| [2 colr.001.001.02 CollateralValueQueryV02 / 2.4 Message Building Blocks / 2.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/sections/section-00015.md) | 15–15 |

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
