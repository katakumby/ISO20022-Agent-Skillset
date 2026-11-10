---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.037.001.01"
message_family: "reda.037"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "file_pages": [2245, 2255]}, {"source_id": "src-000372", "heading": "10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "file_pages": [68, 78]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.037.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2245–2255; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01, Functionality, file p2245.**

The SecuritiesAccountAuditTrailReport message is sent by the executing party to an instructing party to
provide detailed information on the requested securities account audit trail recorded in the system.
Outline
The SecuritiesAccountAuditTrailReportV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
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
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2245 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01618.md) | 2245–2245 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01619.md) | 2246–2246 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01620.md) | 2247–2247 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.1 MessageHeader &lt;MsgHdr&gt; / 57.4.1.3 OriginalBusinessInstruction &lt;OrgnlBizInstr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01621.md) | 2248–2248 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01622.md) | 2249–2249 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 57.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01623.md) | 2250–2250 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 57.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 57.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01624.md) | 2251–2251 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 57.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 57.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 57.4.2.1.1.1.3 NewFieldValue &lt;NewFldVal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01625.md) | 2252–2252 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 57.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 57.4.2.1.1.2 BusinessError &lt;BizErr&gt; / 57.4.2.1.1.2.1 Error &lt;Err&gt; / 57.4.2.1.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01626.md) | 2253–2253 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 57.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 57.4.2.1.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01627.md) | 2254–2254 |
| [57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 57.4 Message Building Blocks / 57.4.2 ReportOrError &lt;RptOrErr&gt; / 57.4.2.2 OperationalError &lt;OprlErr&gt; / 57.4.2.2.1 Error &lt;Err&gt; / 57.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01628.md) | 2255–2255 |

## src-000372 — 10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01

[src-000372](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp68–78; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01, Functionality, file p68.**

The SecuritiesAccountAuditTrailReport message is sent by the executing party to an instructing party to
provide detailed information on the requested securities account audit trail recorded in the system.
Outline
The SecuritiesAccountAuditTrailReportV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities - Securities Account Reference Data 68 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00062.md) | 68–68 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00063.md) | 69–69 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.3 Constraints](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00064.md) | 70–70 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.1 MessageHeader &lt;MsgHdr&gt; / 10.4.1.3 OriginalBusinessInstruction &lt;OrgnlBizInstr&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00065.md) | 71–71 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00066.md) | 72–72 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 10.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00067.md) | 73–73 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 10.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00068.md) | 74–74 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 10.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 10.4.2.1.1.1 AuditTrail &lt;AudtTrl&gt; / 10.4.2.1.1.1.3 NewFieldValue &lt;NewFldVal&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00069.md) | 75–75 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 10.4.2.1.1 SecuritiesAccountAuditTrailOrError &lt;SctiesAcctAudtTrlOrErr&gt; / 10.4.2.1.1.2 BusinessError &lt;BizErr&gt; / 10.4.2.1.1.2.1 Error &lt;Err&gt; / 10.4.2.1.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00070.md) | 76–76 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.1 SecuritiesAccountAuditTrailReport &lt;SctiesAcctAudtTrlRpt&gt; / 10.4.2.1.2 DatePeriod &lt;DtPrd&gt; / 10.4.2.1.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00071.md) | 77–77 |
| [10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01 / 10.4 Message Building Blocks / 10.4.2 ReportOrError &lt;RptOrErr&gt; / 10.4.2.2 OperationalError &lt;OprlErr&gt; / 10.4.2.2.1 Error &lt;Err&gt; / 10.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00072.md) | 78–78 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000371-bank.md) | participant | src-000371 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000371-central-securities-depositories-csd.md) | participant | src-000371 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000371-corporate.md) | participant | src-000371 |
| [CSD](../../../../../shared/reference/participants/participant-src-000371-csd.md) | participant | src-000371 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | participant | src-000371 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | participant | src-000371 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000371-market-data-provider.md) | participant | src-000371 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000371-market-infrastructure.md) | participant | src-000371 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000371-national-central-bank-ncb.md) | participant | src-000371 |
| [Create Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md) | business-flow | src-000371 |
| [Delete Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md) | business-flow | src-000371 |
| [Query](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md) | business-flow | src-000371 |
| [Generate Statement](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md) | business-flow | src-000371 |
| [Creation Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p162-creation-process.md) | business-flow | src-000371 |
| [Modification Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p164-modification-process.md) | business-flow | src-000371 |
| [Deletion Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p166-deletion-process.md) | business-flow | src-000371 |
| [Query/Query Response process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p169-query-query-response-process.md) | business-flow | src-000371 |
| [Statement process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p172-statement-process.md) | business-flow | src-000371 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- SECACCOUNT-FLOWS -->
## Securities account reference flows

- [Query securities account data or audit trail](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
