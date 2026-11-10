---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.039.001.01"
message_family: "reda.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.039.001.01"
source_ids: ["src-000351"]
source_locations: [{"source_id": "src-000351", "heading": "5 reda.039.001.01 CashAccountAuditTrailQueryV01", "file_pages": [113, 117]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["august-2026"]
---

# reda.039.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000351 — 5 reda.039.001.01 CashAccountAuditTrailQueryV01

[src-000351](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`; file pp113–117; publication august-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000351, 5 reda.039.001.01 CashAccountAuditTrailQueryV01, Functionality, file p113.**

The CashAccountAuditTrailQuery message is sent by an instructing party to the executing party to
query for the cash account audit trail recorded in the system.
Outline
The CashAccountAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the cash account audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 reda.039.001.01 CashAccountAuditTrailQueryV01](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00099.md) | 113–113 |
| [5 reda.039.001.01 CashAccountAuditTrailQueryV01 / 5.3 Constraints](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00100.md) | 114–114 |
| [5 reda.039.001.01 CashAccountAuditTrailQueryV01 / 5.4 Message Building Blocks / 5.4.2 SearchCriteria &lt;SchCrit&gt; / 5.4.2.1 CashAccountIdentification &lt;CshAcctId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00101.md) | 115–115 |
| [5 reda.039.001.01 CashAccountAuditTrailQueryV01 / 5.4 Message Building Blocks / 5.4.2 SearchCriteria &lt;SchCrit&gt; / 5.4.2.2 DatePeriod &lt;DtPrd&gt; / 5.4.2.2.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00102.md) | 116–116 |
| [5 reda.039.001.01 CashAccountAuditTrailQueryV01 / 5.4 Message Building Blocks / 5.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00103.md) | 117–117 |

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
