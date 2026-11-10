---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.036.001.01"
message_family: "reda.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "file_pages": [2241, 2244]}, {"source_id": "src-000372", "heading": "9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "file_pages": [64, 67]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.036.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2241–2244; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01, Functionality, file p2241.**

The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to
query for the securities account audit trail recorded in the system.
Outline
The SecuritiesAccountAuditTrailQueryV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities account audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01614.md) | 2241–2241 |
| [56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 56.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01615.md) | 2242–2242 |
| [56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 56.4 Message Building Blocks / 56.4.2 SearchCriteria &lt;SchCrit&gt; / 56.4.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01616.md) | 2243–2243 |
| [56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 56.4 Message Building Blocks / 56.4.2 SearchCriteria &lt;SchCrit&gt; / 56.4.2.2 DatePeriod &lt;DtPrd&gt; / 56.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01617.md) | 2244–2244 |

## src-000372 — 9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp64–67; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01, Functionality, file p64.**

The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to
query for the securities account audit trail recorded in the system.
Outline
The SecuritiesAccountAuditTrailQueryV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SearchCriteria
Defines the criteria to be used to query the securities account audit trail by the executing system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00058.md) | 64–64 |
| [9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 9.3 Constraints](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00059.md) | 65–65 |
| [9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 9.4 Message Building Blocks / 9.4.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00060.md) | 66–66 |
| [9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01 / 9.4 Message Building Blocks / 9.4.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2 DatePeriod &lt;DtPrd&gt; / 9.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00061.md) | 67–67 |

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
