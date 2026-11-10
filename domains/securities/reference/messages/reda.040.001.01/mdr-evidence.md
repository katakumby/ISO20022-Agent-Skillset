---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.040.001.01"
message_family: "reda.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.040.001.01"
source_ids: ["src-000351"]
source_locations: [{"source_id": "src-000351", "heading": "6 reda.040.001.01 CashAccountAuditTrailReportV01", "file_pages": [118, 129]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["august-2026"]
---

# reda.040.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000351 — 6 reda.040.001.01 CashAccountAuditTrailReportV01

[src-000351](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`; file pp118–129; publication august-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000351, 6 reda.040.001.01 CashAccountAuditTrailReportV01, Functionality, file p118.**

The CashAccountAuditTrailReport message is sent by the executing party to an instructing party to
provide detailed information on the requested cash account audit trail recorded in the system.
Outline
The CashAccountAuditTrailReportV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.040.001.01 CashAccountAuditTrailReportV01
Target2-Securities - Cash Account Query and Report 118 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00104.md) | 118–118 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.2 Structure](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00105.md) | 119–119 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.3 Constraints](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00106.md) | 120–120 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.1 MessageHeader &lt;MsgHdr&gt; / 6.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00107.md) | 121–121 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00108.md) | 122–122 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt; / 6.4.2.1.1 CashAccountAuditTrailOrError &lt;CshAcctAudtTrlOrErr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00109.md) | 123–123 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt; / 6.4.2.1.1 CashAccountAuditTrailOrError &lt;CshAcctAudtTrlOrErr&gt; / 6.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00110.md) | 124–124 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt; / 6.4.2.1.1 CashAccountAuditTrailOrError &lt;CshAcctAudtTrlOrErr&gt; / 6.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 6.4.2.1.1.1.3 NewFieldValue &lt;NewFldVal&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00111.md) | 125–125 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt; / 6.4.2.1.1 CashAccountAuditTrailOrError &lt;CshAcctAudtTrlOrErr&gt; / 6.4.2.1.1.2 BusinessError &lt;BizErr&gt; / 6.4.2.1.1.2.1 Error &lt;Err&gt; / 6.4.2.1.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00112.md) | 126–126 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.1 CashAccountAuditTrailReport &lt;CshAcctAudtTrlRpt&gt; / 6.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 6.4.2.1.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00113.md) | 127–127 |
| [6 reda.040.001.01 CashAccountAuditTrailReportV01 / 6.4 Message Building Blocks / 6.4.2 ReportOrError &lt;RptOrErr&gt; / 6.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00114.md) | 128–129 |

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
