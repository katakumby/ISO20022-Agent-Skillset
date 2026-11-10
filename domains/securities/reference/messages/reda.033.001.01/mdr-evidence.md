---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.033.001.01"
message_family: "reda.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.033.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "53 reda.033.001.01 SecuritiesAuditTrailQueryV01", "file_pages": [2219, 2223]}, {"source_id": "src-000378", "heading": "11 reda.033.001.01 SecuritiesAuditTrailQueryV01", "file_pages": [129, 133]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.033.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 53 reda.033.001.01 SecuritiesAuditTrailQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2219–2223; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 53 reda.033.001.01 SecuritiesAuditTrailQueryV01, Functionality, file p2219.**

The SecuritiesAuditTrailQuery message is sent by an instructing party to the executing party to query
for the securities audit trail recorded in the system.
Outline
The SecuritiesAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [53 reda.033.001.01 SecuritiesAuditTrailQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01592.md) | 2219–2219 |
| [53 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 53.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01593.md) | 2220–2220 |
| [53 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 53.4 Message Building Blocks / 53.4.2 SearchCriteria &lt;SchCrit&gt; / 53.4.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01594.md) | 2221–2221 |
| [53 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 53.4 Message Building Blocks / 53.4.2 SearchCriteria &lt;SchCrit&gt; / 53.4.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01595.md) | 2222–2222 |
| [53 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 53.4 Message Building Blocks / 53.4.2 SearchCriteria &lt;SchCrit&gt; / 53.4.2.2 DatePeriod &lt;DtPrd&gt; / 53.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01596.md) | 2223–2223 |

## src-000378 — 11 reda.033.001.01 SecuritiesAuditTrailQueryV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp129–133; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 11 reda.033.001.01 SecuritiesAuditTrailQueryV01, Functionality, file p129.**

The SecuritiesAuditTrailQuery message is sent by an instructing party to the executing party to query
for the securities audit trail recorded in the system.
Outline
The SecuritiesAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 reda.033.001.01 SecuritiesAuditTrailQueryV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00080.md) | 129–129 |
| [11 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 11.3 Constraints](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00081.md) | 130–130 |
| [11 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 11.4 Message Building Blocks / 11.4.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00082.md) | 131–131 |
| [11 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 11.4 Message Building Blocks / 11.4.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00083.md) | 132–132 |
| [11 reda.033.001.01 SecuritiesAuditTrailQueryV01 / 11.4 Message Building Blocks / 11.4.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2 DatePeriod &lt;DtPrd&gt; / 11.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00084.md) | 133–133 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000377-central-securities-depositories-csd.md) | participant | src-000377 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000377-corporate.md) | participant | src-000377 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | participant | src-000377 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | participant | src-000377 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000377-market-data-provider.md) | participant | src-000377 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000377-market-infrastructure.md) | participant | src-000377 |
| [Create Security](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p146-create-security.md) | business-flow | src-000377 |
| [Modify Security](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p147-modify-security.md) | business-flow | src-000377 |
| [Delete Security](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p148-delete-security.md) | business-flow | src-000377 |
| [Query](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p149-query.md) | business-flow | src-000377 |
| [General Statement](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p150-general-statement.md) | business-flow | src-000377 |
| [Creation Process](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p154-creation-process.md) | business-flow | src-000377 |
| [Modification Process](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p156-modification-process.md) | business-flow | src-000377 |
| [Deletion Process](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p159-deletion-process.md) | business-flow | src-000377 |
| [Query/Query Response Process](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p162-query-query-response-process.md) | business-flow | src-000377 |
| [Statement Process](../../message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p165-statement-process.md) | business-flow | src-000377 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
