---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.014.001.02"
message_family: "reda.014"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.014.001.02"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "34 reda.014.001.02 PartyCreationRequestV02", "file_pages": [2043, 2054]}, {"source_id": "src-000369", "heading": "2 reda.014.001.02 PartyCreationRequestV02", "file_pages": [6, 17]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.014.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 34 reda.014.001.02 PartyCreationRequestV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2043–2054; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 34 reda.014.001.02 PartyCreationRequestV02, Functionality, file p2043.**

Scope:
The PartyCreationRequest message is sent by an instructing party to the executing party to request for
the creation of party reference data for a new party in the executing system.
Usage:
It aims at instructing the creation of a new party with corresponding details.
Processing and confirmation of the party creation request are provided via a party status advice.
Outline
The PartyCreationRequestV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Party
Specifies the details of the party to be created in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2043 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [34 reda.014.001.02 PartyCreationRequestV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01433.md) | 2043–2043 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01434.md) | 2044–2044 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01435.md) | 2045–2046 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01436.md) | 2047–2047 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.3 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01437.md) | 2048–2048 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01438.md) | 2049–2049 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.6 Type &lt;Tp&gt; / 34.4.2.6.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01439.md) | 2050–2050 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01440.md) | 2051–2051 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.9 Name &lt;Nm&gt; / 34.4.2.9.3 ShortName &lt;ShrtNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01441.md) | 2052–2052 |
| [34 reda.014.001.02 PartyCreationRequestV02 / 34.4 Message Building Blocks / 34.4.2 Party &lt;Pty&gt; / 34.4.2.11 LockStatus &lt;LckSts&gt; / 34.4.2.11.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01442.md) | 2053–2054 |

## src-000369 — 2 reda.014.001.02 PartyCreationRequestV02

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp6–17; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 2 reda.014.001.02 PartyCreationRequestV02, Functionality, file p6.**

Scope:
The PartyCreationRequest message is sent by an instructing party to the executing party to request for
the creation of party reference data for a new party in the executing system.
Usage:
It aims at instructing the creation of a new party with corresponding details.
Processing and confirmation of the party creation request are provided via a party status advice.
Outline
The PartyCreationRequestV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Party
Specifies the details of the party to be created in the system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
6 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 reda.014.001.02 PartyCreationRequestV02](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00004.md) | 6–6 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00005.md) | 7–7 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00006.md) | 8–9 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00007.md) | 10–10 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.3 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00008.md) | 11–11 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00009.md) | 12–12 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.6 Type &lt;Tp&gt; / 2.4.2.6.1 Code &lt;Cd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00010.md) | 13–13 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00011.md) | 14–14 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.9 Name &lt;Nm&gt; / 2.4.2.9.3 ShortName &lt;ShrtNm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00012.md) | 15–15 |
| [2 reda.014.001.02 PartyCreationRequestV02 / 2.4 Message Building Blocks / 2.4.2 Party &lt;Pty&gt; / 2.4.2.11 LockStatus &lt;LckSts&gt; / 2.4.2.11.3 LockReason &lt;LckRsn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00013.md) | 16–17 |

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
