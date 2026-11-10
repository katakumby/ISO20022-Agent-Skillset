---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.043.001.02"
message_family: "reda.043"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.043.001.02"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "60 reda.043.001.02 PartyAuditTrailReportV02", "file_pages": [2292, 2334]}, {"source_id": "src-000369", "heading": "10 reda.043.001.02 PartyAuditTrailReportV02", "file_pages": [115, 157]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.043.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 60 reda.043.001.02 PartyAuditTrailReportV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2292–2334; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 60 reda.043.001.02 PartyAuditTrailReportV02, Functionality, file p2292.**

The PartyAuditTrailReport message is sent by the executing party to an instructing party to provide
detailed information on the requested party audit trail recorded in the system.
Outline
The PartyAuditTrailReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides the party audit trail data or error resulting from the audit trail query request.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2292 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [60 reda.043.001.02 PartyAuditTrailReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01657.md) | 2292–2292 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01658.md) | 2293–2295 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01659.md) | 2296–2296 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.1 MessageHeader &lt;MsgHdr&gt; / 60.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01660.md) | 2297–2300 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01661.md) | 2301–2303 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01662.md) | 2304–2306 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01663.md) | 2307–2309 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01664.md) | 2310–2312 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.1 Address &lt;Adr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01665.md) | 2313–2313 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.1 Address &lt;Adr&gt; / 60.4.2.1.1.1.1.1.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01666.md) | 2314–2314 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.2 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01667.md) | 2315–2315 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.2 ContactDetails &lt;CtctDtls&gt; / 60.4.2.1.1.1.1.2.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01668.md) | 2316–2316 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.3 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01669.md) | 2317–2317 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.4 ClosingDate &lt;ClsgDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01670.md) | 2318–2318 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.5 Type &lt;Tp&gt; / 60.4.2.1.1.1.1.5.1 Old &lt;Od&gt; / 60.4.2.1.1.1.1.5.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01671.md) | 2319–2319 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.6 TechnicalAddress &lt;TechAdr&gt; / 60.4.2.1.1.1.1.6.1 Old &lt;Od&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01672.md) | 2320–2320 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.6 TechnicalAddress &lt;TechAdr&gt; / 60.4.2.1.1.1.1.6.2 New &lt;New&gt; / 60.4.2.1.1.1.1.6.2.1 BICFI &lt;BICFI&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01673.md) | 2321–2321 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.7 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 60.4.2.1.1.1.1.7.1 Old &lt;Od&gt; / 60.4.2.1.1.1.1.7.1.1 Name &lt;Nm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01674.md) | 2322–2322 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.8 Name &lt;Nm&gt; / 60.4.2.1.1.1.1.8.1 Old &lt;Od&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01675.md) | 2323–2323 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.8 Name &lt;Nm&gt; / 60.4.2.1.1.1.1.8.2 New &lt;New&gt; / 60.4.2.1.1.1.1.8.2.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01676.md) | 2324–2324 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.9 ResidenceType &lt;ResTp&gt; / 60.4.2.1.1.1.1.9.2 New &lt;New&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01677.md) | 2325–2325 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.10 LockStatus &lt;LckSts&gt; / 60.4.2.1.1.1.1.10.1 Old &lt;Od&gt; / 60.4.2.1.1.1.1.10.1.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01678.md) | 2326–2326 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.10 LockStatus &lt;LckSts&gt; / 60.4.2.1.1.1.1.10.2 New &lt;New&gt; / 60.4.2.1.1.1.1.10.2.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01679.md) | 2327–2327 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 60.4.2.1.1.1.1.11.1 Old &lt;Od&gt; / 60.4.2.1.1.1.1.11.1.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01680.md) | 2328–2328 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 60.4.2.1.1.1.1.11.2 New &lt;New&gt; / 60.4.2.1.1.1.1.11.2.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01681.md) | 2329–2329 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 60.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 60.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 60.4.2.1.1.1.1.11.2 New &lt;New&gt; / 60.4.2.1.1.1.1.11.2.3 ValidUntil &lt;VldUntil&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01682.md) | 2330–2330 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 60.4.2.1.1.2 BusinessError &lt;BizErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01683.md) | 2331–2331 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 60.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 60.4.2.1.2.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01684.md) | 2332–2332 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.2 ReportOrError &lt;RptOrErr&gt; / 60.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01685.md) | 2333–2333 |
| [60 reda.043.001.02 PartyAuditTrailReportV02 / 60.4 Message Building Blocks / 60.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01686.md) | 2334–2334 |

## src-000369 — 10 reda.043.001.02 PartyAuditTrailReportV02

[src-000369](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp115–157; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 10 reda.043.001.02 PartyAuditTrailReportV02, Functionality, file p115.**

The PartyAuditTrailReport message is sent by the executing party to an instructing party to provide
detailed information on the requested party audit trail recorded in the system.
Outline
The PartyAuditTrailReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides the party audit trail data or error resulting from the audit trail query request.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
115 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 reda.043.001.02 PartyAuditTrailReportV02](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00094.md) | 115–115 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00095.md) | 116–118 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00096.md) | 119–119 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.1 MessageHeader &lt;MsgHdr&gt; / 10.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00097.md) | 120–123 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00098.md) | 124–126 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00099.md) | 127–129 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00100.md) | 130–132 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00101.md) | 133–135 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.1 Address &lt;Adr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00102.md) | 136–136 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.1 Address &lt;Adr&gt; / 10.4.2.1.1.1.1.1.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00103.md) | 137–137 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.2 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00104.md) | 138–138 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.2 ContactDetails &lt;CtctDtls&gt; / 10.4.2.1.1.1.1.2.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00105.md) | 139–139 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.3 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00106.md) | 140–140 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.4 ClosingDate &lt;ClsgDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00107.md) | 141–141 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.5 Type &lt;Tp&gt; / 10.4.2.1.1.1.1.5.1 Old &lt;Od&gt; / 10.4.2.1.1.1.1.5.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00108.md) | 142–142 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.6 TechnicalAddress &lt;TechAdr&gt; / 10.4.2.1.1.1.1.6.1 Old &lt;Od&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00109.md) | 143–143 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.6 TechnicalAddress &lt;TechAdr&gt; / 10.4.2.1.1.1.1.6.2 New &lt;New&gt; / 10.4.2.1.1.1.1.6.2.1 BICFI &lt;BICFI&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00110.md) | 144–144 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.7 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 10.4.2.1.1.1.1.7.1 Old &lt;Od&gt; / 10.4.2.1.1.1.1.7.1.1 Name &lt;Nm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00111.md) | 145–145 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.8 Name &lt;Nm&gt; / 10.4.2.1.1.1.1.8.1 Old &lt;Od&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00112.md) | 146–146 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.8 Name &lt;Nm&gt; / 10.4.2.1.1.1.1.8.2 New &lt;New&gt; / 10.4.2.1.1.1.1.8.2.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00113.md) | 147–147 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.9 ResidenceType &lt;ResTp&gt; / 10.4.2.1.1.1.1.9.2 New &lt;New&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00114.md) | 148–148 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.10 LockStatus &lt;LckSts&gt; / 10.4.2.1.1.1.1.10.1 Old &lt;Od&gt; / 10.4.2.1.1.1.1.10.1.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00115.md) | 149–149 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.10 LockStatus &lt;LckSts&gt; / 10.4.2.1.1.1.1.10.2 New &lt;New&gt; / 10.4.2.1.1.1.1.10.2.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00116.md) | 150–150 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 10.4.2.1.1.1.1.11.1 Old &lt;Od&gt; / 10.4.2.1.1.1.1.11.1.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00117.md) | 151–151 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 10.4.2.1.1.1.1.11.2 New &lt;New&gt; / 10.4.2.1.1.1.1.11.2.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00118.md) | 152–152 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.1 Record &lt;Rcrd&gt; / 10.4.2.1.1.1.1.11 Restriction &lt;Rstrctn&gt; / 10.4.2.1.1.1.1.11.2 New &lt;New&gt; / 10.4.2.1.1.1.1.11.2.3 ValidUntil &lt;VldUntil&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00119.md) | 153–153 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.1 PartyAuditTrailOrError &lt;PtyAudtTrlOrErr&gt; / 10.4.2.1.1.2 BusinessError &lt;BizErr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00120.md) | 154–154 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 PartyAuditTrailReport &lt;PtyAudtTrlRpt&gt; / 10.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 10.4.2.1.2.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00121.md) | 155–155 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00122.md) | 156–156 |
| [10 reda.043.001.02 PartyAuditTrailReportV02 / 10.4 Message Building Blocks / 10.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00123.md) | 157–157 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000368-bank.md) | participant | src-000368 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000368-central-securities-depositories-csd.md) | participant | src-000368 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000368-corporate.md) | participant | src-000368 |
| [CSD](../../../../../shared/reference/participants/participant-src-000368-csd.md) | participant | src-000368 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | participant | src-000368 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | participant | src-000368 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000368-market-data-provider.md) | participant | src-000368 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000368-market-infrastructure.md) | participant | src-000368 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000368-national-central-bank-ncb.md) | participant | src-000368 |
| [Create Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p120-create-party.md) | business-flow | src-000368 |
| [Modify Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md) | business-flow | src-000368 |
| [Delete Party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p124-delete-party.md) | business-flow | src-000368 |
| [Query](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p126-query.md) | business-flow | src-000368 |
| [Statement](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p128-statement.md) | business-flow | src-000368 |
| [Creation Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p133-creation-process.md) | business-flow | src-000368 |
| [Modification Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p137-modification-process.md) | business-flow | src-000368 |
| [Deletion Process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p140-deletion-process.md) | business-flow | src-000368 |
| [Query/Query Response process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p144-query-query-response-process.md) | business-flow | src-000368 |
| [Statement process](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p147-statement-process.md) | business-flow | src-000368 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)



<!-- PARTY-FLOWS -->
## Party reference data flows

- [Query party reference data or audit trail](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p126-query.md)
