---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.042.001.01"
message_family: "reda.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.042.001.01"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "59 reda.042.001.01 PartyAuditTrailQueryV01", "file_pages": [2288, 2291]}, {"source_id": "src-000369", "heading": "9 reda.042.001.01 PartyAuditTrailQueryV01", "file_pages": [111, 114]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.042.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 59 reda.042.001.01 PartyAuditTrailQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2288–2291; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 59 reda.042.001.01 PartyAuditTrailQueryV01, Functionality, file p2288.**

The PartyAuditTrailQuery message is sent by an instructing party to the executing party to query for the
party audit trail recorded in the system.
Outline
The PartyAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the party audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [59 reda.042.001.01 PartyAuditTrailQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01653.md) | 2288–2288 |
| [59 reda.042.001.01 PartyAuditTrailQueryV01 / 59.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01654.md) | 2289–2289 |
| [59 reda.042.001.01 PartyAuditTrailQueryV01 / 59.4 Message Building Blocks / 59.4.2 SearchCriteria &lt;SchCrit&gt; / 59.4.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01655.md) | 2290–2290 |
| [59 reda.042.001.01 PartyAuditTrailQueryV01 / 59.4 Message Building Blocks / 59.4.2 SearchCriteria &lt;SchCrit&gt; / 59.4.2.2 DatePeriod &lt;DtPrd&gt; / 59.4.2.2.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01656.md) | 2291–2291 |

## src-000369 — 9 reda.042.001.01 PartyAuditTrailQueryV01

[src-000369](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp111–114; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 9 reda.042.001.01 PartyAuditTrailQueryV01, Functionality, file p111.**

The PartyAuditTrailQuery message is sent by an instructing party to the executing party to query for the
party audit trail recorded in the system.
Outline
The PartyAuditTrailQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the party audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 reda.042.001.01 PartyAuditTrailQueryV01](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00090.md) | 111–111 |
| [9 reda.042.001.01 PartyAuditTrailQueryV01 / 9.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00091.md) | 112–112 |
| [9 reda.042.001.01 PartyAuditTrailQueryV01 / 9.4 Message Building Blocks / 9.4.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00092.md) | 113–113 |
| [9 reda.042.001.01 PartyAuditTrailQueryV01 / 9.4 Message Building Blocks / 9.4.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2 DatePeriod &lt;DtPrd&gt; / 9.4.2.2.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00093.md) | 114–114 |

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
