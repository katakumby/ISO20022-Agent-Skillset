---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.038.001.01"
message_family: "reda.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.038.001.01"
source_ids: ["src-000351"]
source_locations: [{"source_id": "src-000351", "heading": "4 reda.038.001.01 CashAccountActivityAdviceV01", "file_pages": [108, 112]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["august-2026"]
---

# reda.038.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000351 — 4 reda.038.001.01 CashAccountActivityAdviceV01

[src-000351](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`; file pp108–112; publication august-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000351, 4 reda.038.001.01 CashAccountActivityAdviceV01, Functionality, file p108.**

The CashAccountActivityReport message is sent by the executing party to an instructing party
containing information about changes on cash account reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for cash account reference
data.
Outline
The CashAccountActivityAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CashAccountActivity
Activity report of changes occurred for a cash account defined in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.038.001.01 CashAccountActivityAdviceV01](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00094.md) | 108–108 |
| [4 reda.038.001.01 CashAccountActivityAdviceV01 / 4.3 Constraints](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00095.md) | 109–109 |
| [4 reda.038.001.01 CashAccountActivityAdviceV01 / 4.4 Message Building Blocks / 4.4.2 CashAccountActivity &lt;CshAcctActvty&gt; / 4.4.2.1 SystemDate &lt;SysDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00096.md) | 110–110 |
| [4 reda.038.001.01 CashAccountActivityAdviceV01 / 4.4 Message Building Blocks / 4.4.2 CashAccountActivity &lt;CshAcctActvty&gt; / 4.4.2.2 Change &lt;Chng&gt; / 4.4.2.2.2 FieldName &lt;FldNm&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00097.md) | 111–111 |
| [4 reda.038.001.01 CashAccountActivityAdviceV01 / 4.4 Message Building Blocks / 4.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00098.md) | 112–112 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000350-account-owner.md) | participant | src-000350 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000350-account-servicer.md) | participant | src-000350 |
| [Central Database System](../../../../../shared/reference/participants/participant-src-000350-central-database-system.md) | participant | src-000350 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000350-central-securities-depository-csd.md) | participant | src-000350 |
| [Central Security Depository (CSD)](../../../../../shared/reference/participants/participant-src-000350-central-security-depository-csd.md) | participant | src-000350 |
| [Collateral Management System](../../../../../shared/reference/participants/participant-src-000350-collateral-management-system.md) | participant | src-000350 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | participant | src-000350 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | participant | src-000350 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000350-market-infrastructure.md) | participant | src-000350 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000350-national-central-bank.md) | participant | src-000350 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000350-payment-bank.md) | participant | src-000350 |
| [Account Query List](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p123-account-query-list.md) | business-flow | src-000350 |
| [Cash Account Audit Trail Query](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p124-cash-account-audit-trail-query.md) | business-flow | src-000350 |
| [Cash Account Activity Advice](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p125-cash-account-activity-advice.md) | business-flow | src-000350 |
| [Account Query List - Account List Response process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p130-account-query-list-account-list-response-process.md) | business-flow | src-000350 |
| [Cash Account Activity Advice process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p135-cash-account-activity-advice-process.md) | business-flow | src-000350 |
| [Cash Account Audit Trail Query/Response process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p140-cash-account-audit-trail-query-response-process.md) | business-flow | src-000350 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
