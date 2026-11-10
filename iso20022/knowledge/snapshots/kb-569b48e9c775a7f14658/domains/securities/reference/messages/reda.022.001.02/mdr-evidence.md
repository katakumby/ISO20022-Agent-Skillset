---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.022.001.02"
message_family: "reda.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.022.001.02"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "42 reda.022.001.02 PartyModificationRequestV02", "file_pages": [2140, 2154]}, {"source_id": "src-000369", "heading": "6 reda.022.001.02 PartyModificationRequestV02", "file_pages": [61, 75]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.022.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 42 reda.022.001.02 PartyModificationRequestV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2140–2154; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 42 reda.022.001.02 PartyModificationRequestV02, Functionality, file p2140.**

Scope:
The PartyModificationRequest message is sent by the instructing party to the executing party to request
for an update of the party reference data of a party defined in the executing system.
Usage:
It aims at instructing the update of an existing party by amending its existing details or by providing
additional details.
Processing and confirmation of the party modification request message are provided via a party status
advice.
Outline
The PartyModificationRequestV02 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SystemPartyIdentification
Unique identification, as assigned by the executing system, to unambiguously identify the party to
be modified.
C. Modification
Identifies the list of requested modifications to be executed by the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2140 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [42 reda.022.001.02 PartyModificationRequestV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01520.md) | 2140–2140 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01521.md) | 2141–2141 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01522.md) | 2142–2142 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01523.md) | 2143–2144 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.1 ScopeIndication &lt;ScpIndctn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01524.md) | 2145–2145 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.1 SystemPartyDate &lt;SysPtyDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01525.md) | 2146–2146 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.1 SystemPartyDate &lt;SysPtyDt&gt; / 42.4.3.2.1.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01526.md) | 2147–2147 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.3 PartyName &lt;PtyNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01527.md) | 2148–2148 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.5 TechnicalAddress &lt;TechAdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01528.md) | 2149–2149 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.5 TechnicalAddress &lt;TechAdr&gt; / 42.4.3.2.5.2 TechnicalAddress &lt;TechAdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01529.md) | 2150–2150 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.7 ResidenceType &lt;ResTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01530.md) | 2151–2151 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.8 LockStatus &lt;LckSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01531.md) | 2152–2152 |
| [42 reda.022.001.02 PartyModificationRequestV02 / 42.4 Message Building Blocks / 42.4.3 Modification &lt;Mod&gt; / 42.4.3.2 RequestedModification &lt;ReqdMod&gt; / 42.4.3.2.9 SystemRestriction &lt;SysRstrctn&gt; / 42.4.3.2.9.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01532.md) | 2153–2154 |

## src-000369 — 6 reda.022.001.02 PartyModificationRequestV02

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp61–75; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 6 reda.022.001.02 PartyModificationRequestV02, Functionality, file p61.**

Scope:
The PartyModificationRequest message is sent by the instructing party to the executing party to request
for an update of the party reference data of a party defined in the executing system.
Usage:
It aims at instructing the update of an existing party by amending its existing details or by providing
additional details.
Processing and confirmation of the party modification request message are provided via a party status
advice.
Outline
The PartyModificationRequestV02 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SystemPartyIdentification
Unique identification, as assigned by the executing system, to unambiguously identify the party to
be modified.
C. Modification
Identifies the list of requested modifications to be executed by the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
61 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.022.001.02 PartyModificationRequestV02](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00051.md) | 61–61 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00052.md) | 62–62 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00053.md) | 63–63 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00054.md) | 64–65 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.1 ScopeIndication &lt;ScpIndctn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00055.md) | 66–66 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.1 SystemPartyDate &lt;SysPtyDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00056.md) | 67–67 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.1 SystemPartyDate &lt;SysPtyDt&gt; / 6.4.3.2.1.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00057.md) | 68–68 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.3 PartyName &lt;PtyNm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00058.md) | 69–69 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.5 TechnicalAddress &lt;TechAdr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00059.md) | 70–70 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.5 TechnicalAddress &lt;TechAdr&gt; / 6.4.3.2.5.2 TechnicalAddress &lt;TechAdr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00060.md) | 71–71 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.7 ResidenceType &lt;ResTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00061.md) | 72–72 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.8 LockStatus &lt;LckSts&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00062.md) | 73–73 |
| [6 reda.022.001.02 PartyModificationRequestV02 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.9 SystemRestriction &lt;SysRstrctn&gt; / 6.4.3.2.9.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00063.md) | 74–75 |

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

- [Modify or block/unblock a party](../../message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md)
