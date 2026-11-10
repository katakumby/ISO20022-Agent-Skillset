---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.016.001.01"
message_family: "reda.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.016.001.01"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "36 reda.016.001.01 PartyStatusAdviceV01", "file_pages": [2072, 2077]}, {"source_id": "src-000369", "heading": "4 reda.016.001.01 PartyStatusAdviceV01", "file_pages": [35, 40]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.016.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 36 reda.016.001.01 PartyStatusAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2072–2077; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 36 reda.016.001.01 PartyStatusAdviceV01, Functionality, file p2072.**

Scope:
The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details
about the processing of a request on party reference data (create or update).
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When processing is successfully performed, the message includes the related party identification.
Outline
The PartyStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PartyStatus
Status of the party involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities 2072 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [36 reda.016.001.01 PartyStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01458.md) | 2072–2072 |
| [36 reda.016.001.01 PartyStatusAdviceV01 / 36.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01459.md) | 2073–2073 |
| [36 reda.016.001.01 PartyStatusAdviceV01 / 36.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01460.md) | 2074–2074 |
| [36 reda.016.001.01 PartyStatusAdviceV01 / 36.4 Message Building Blocks / 36.4.2 PartyStatus &lt;PtySts&gt; / 36.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01461.md) | 2075–2075 |
| [36 reda.016.001.01 PartyStatusAdviceV01 / 36.4 Message Building Blocks / 36.4.2 PartyStatus &lt;PtySts&gt; / 36.4.2.2 StatusReason &lt;StsRsn&gt; / 36.4.2.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01462.md) | 2076–2076 |
| [36 reda.016.001.01 PartyStatusAdviceV01 / 36.4 Message Building Blocks / 36.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01463.md) | 2077–2077 |

## src-000369 — 4 reda.016.001.01 PartyStatusAdviceV01

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp35–40; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 4 reda.016.001.01 PartyStatusAdviceV01, Functionality, file p35.**

Scope:
The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details
about the processing of a request on party reference data (create or update).
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When processing is successfully performed, the message includes the related party identification.
Outline
The PartyStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PartyStatus
Status of the party involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
35 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.016.001.01 PartyStatusAdviceV01](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00029.md) | 35–35 |
| [4 reda.016.001.01 PartyStatusAdviceV01 / 4.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00030.md) | 36–36 |
| [4 reda.016.001.01 PartyStatusAdviceV01 / 4.4 Message Building Blocks](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00031.md) | 37–37 |
| [4 reda.016.001.01 PartyStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 PartyStatus &lt;PtySts&gt; / 4.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00032.md) | 38–38 |
| [4 reda.016.001.01 PartyStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 PartyStatus &lt;PtySts&gt; / 4.4.2.2 StatusReason &lt;StsRsn&gt; / 4.4.2.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00033.md) | 39–39 |
| [4 reda.016.001.01 PartyStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00034.md) | 40–40 |

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

- [Create a party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p120-create-party.md)
- [Modify or block/unblock a party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md)
- [Delete a party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p124-delete-party.md)
