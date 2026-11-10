---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.034.001.01"
message_family: "reda.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.034.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "54 reda.034.001.01 SecuritiesAuditTrailReportV01", "file_pages": [2224, 2235]}, {"source_id": "src-000378", "heading": "12 reda.034.001.01 SecuritiesAuditTrailReportV01", "file_pages": [134, 145]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.034.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 54 reda.034.001.01 SecuritiesAuditTrailReportV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2224–2235; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 54 reda.034.001.01 SecuritiesAuditTrailReportV01, Functionality, file p2224.**

The SecuritiesAuditTrailReport message is sent by the executing party to an instructing party to provide
detailed information on the requested securities audit trail recorded in the system.
Outline
The SecuritiesAuditTrailReportV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities 2224 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01597.md) | 2224–2224 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01598.md) | 2225–2225 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01599.md) | 2226–2226 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.1 MessageHeader &lt;MsgHdr&gt; / 54.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01600.md) | 2227–2227 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01601.md) | 2228–2228 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 54.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01602.md) | 2229–2229 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 54.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 54.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01603.md) | 2230–2230 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 54.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 54.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 54.4.2.1.1.1.3 NewFieldValue &lt;NewFldVal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01604.md) | 2231–2231 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 54.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 54.4.2.1.1.2 BusinessError &lt;BizErr&gt; / 54.4.2.1.1.2.1 Error &lt;Err&gt; / 54.4.2.1.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01605.md) | 2232–2232 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 54.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 54.4.2.1.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01606.md) | 2233–2233 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01607.md) | 2234–2234 |
| [54 reda.034.001.01 SecuritiesAuditTrailReportV01 / 54.4 Message Building Blocks / 54.4.2 ReportOrError &lt;RptOrErr&gt; / 54.4.2.2 OperationalError &lt;OprlErr&gt; / 54.4.2.2.1 Error &lt;Err&gt; / 54.4.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01608.md) | 2235–2235 |

## src-000378 — 12 reda.034.001.01 SecuritiesAuditTrailReportV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp134–145; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 12 reda.034.001.01 SecuritiesAuditTrailReportV01, Functionality, file p134.**

The SecuritiesAuditTrailReport message is sent by the executing party to an instructing party to provide
detailed information on the requested securities audit trail recorded in the system.
Outline
The SecuritiesAuditTrailReportV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 134 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00085.md) | 134–134 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00086.md) | 135–135 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.3 Constraints](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00087.md) | 136–136 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.1 MessageHeader &lt;MsgHdr&gt; / 12.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00088.md) | 137–137 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00089.md) | 138–138 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 12.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00090.md) | 139–139 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 12.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 12.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00091.md) | 140–140 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 12.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 12.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 12.4.2.1.1.1.3 NewFieldValue &lt;NewFldVal&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00092.md) | 141–141 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 12.4.2.1.1 SecuritiesAuditTrailOrError &lt;SctiesAudtTrlOrErr&gt; / 12.4.2.1.1.2 BusinessError &lt;BizErr&gt; / 12.4.2.1.1.2.1 Error &lt;Err&gt; / 12.4.2.1.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00093.md) | 142–142 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.1 SecuritiesAuditTrailReport &lt;SctiesAudtTrlRpt&gt; / 12.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 12.4.2.1.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00094.md) | 143–143 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00095.md) | 144–144 |
| [12 reda.034.001.01 SecuritiesAuditTrailReportV01 / 12.4 Message Building Blocks / 12.4.2 ReportOrError &lt;RptOrErr&gt; / 12.4.2.2 OperationalError &lt;OprlErr&gt; / 12.4.2.2.1 Error &lt;Err&gt; / 12.4.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00096.md) | 145–145 |

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
