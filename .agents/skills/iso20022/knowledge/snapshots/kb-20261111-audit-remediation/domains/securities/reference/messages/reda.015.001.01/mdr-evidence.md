---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.015.001.01"
message_family: "reda.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "35 reda.015.001.01 PartyQueryV01", "file_pages": [2055, 2071]}, {"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18, 34]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.015.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 35 reda.015.001.01 PartyQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2055–2071; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 35 reda.015.001.01 PartyQueryV01, Functionality, file p2055.**

Scope:
The PartyQuery message is sent by a central securities depository, a national central bank, a central
securities depository participant, a central counter party, a payment bank, a trading party or a stock
exchange to the executing party to query for the party reference data of a party defined in the system.
Outline
The PartyQueryV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the query message.
B. SearchCriteria
Defines the criteria to be used to query the party reference data by the executing system.
C. ReturnCriteria
Defines the expected party reference data to be returned.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2055 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [35 reda.015.001.01 PartyQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01443.md) | 2055–2055 |
| [35 reda.015.001.01 PartyQueryV01 / 35.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01444.md) | 2056–2057 |
| [35 reda.015.001.01 PartyQueryV01 / 35.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01445.md) | 2058–2059 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01446.md) | 2060–2060 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.1 OpeningDate &lt;OpngDt&gt; / 35.4.2.1.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01447.md) | 2061–2061 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.2 ClosingDate &lt;ClsgDt&gt; / 35.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01448.md) | 2062–2062 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.5 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01449.md) | 2063–2063 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 35.4.2.7.1 DateTime &lt;DtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01450.md) | 2064–2064 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 35.4.2.7.1 DateTime &lt;DtTm&gt; / 35.4.2.7.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01451.md) | 2065–2065 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 35.4.2.7.2 Date &lt;Dt&gt; / 35.4.2.7.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01452.md) | 2066–2066 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.2 SearchCriteria &lt;SchCrit&gt; / 35.4.2.9 LockStatus &lt;LckSts&gt; / 35.4.2.9.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01453.md) | 2067–2067 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.3 ReturnCriteria &lt;RtrCrit&gt; / 35.4.3.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01454.md) | 2068–2068 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.3 ReturnCriteria &lt;RtrCrit&gt; / 35.4.3.4 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01455.md) | 2069–2069 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.3 ReturnCriteria &lt;RtrCrit&gt; / 35.4.3.9 ShortName &lt;ShrtNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01456.md) | 2070–2070 |
| [35 reda.015.001.01 PartyQueryV01 / 35.4 Message Building Blocks / 35.4.3 ReturnCriteria &lt;RtrCrit&gt; / 35.4.3.14 LockStatus &lt;LckSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01457.md) | 2071–2071 |

## src-000369 — 3 reda.015.001.01 PartyQueryV01

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp18–34; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 3 reda.015.001.01 PartyQueryV01, Functionality, file p18.**

Scope:
The PartyQuery message is sent by a central securities depository, a national central bank, a central
securities depository participant, a central counter party, a payment bank, a trading party or a stock
exchange to the executing party to query for the party reference data of a party defined in the system.
Outline
The PartyQueryV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the query message.
B. SearchCriteria
Defines the criteria to be used to query the party reference data by the executing system.
C. ReturnCriteria
Defines the expected party reference data to be returned.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
18 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 reda.015.001.01 PartyQueryV01](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00014.md) | 18–18 |
| [3 reda.015.001.01 PartyQueryV01 / 3.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00015.md) | 19–20 |
| [3 reda.015.001.01 PartyQueryV01 / 3.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00016.md) | 21–22 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00017.md) | 23–23 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.1 OpeningDate &lt;OpngDt&gt; / 3.4.2.1.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00018.md) | 24–24 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.2 ClosingDate &lt;ClsgDt&gt; / 3.4.2.2.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00019.md) | 25–25 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.5 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00020.md) | 26–26 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 3.4.2.7.1 DateTime &lt;DtTm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00021.md) | 27–27 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 3.4.2.7.1 DateTime &lt;DtTm&gt; / 3.4.2.7.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00022.md) | 28–28 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.7 RestrictionIssueDate &lt;RstrctnIsseDt&gt; / 3.4.2.7.2 Date &lt;Dt&gt; / 3.4.2.7.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00023.md) | 29–29 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.9 LockStatus &lt;LckSts&gt; / 3.4.2.9.1 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00024.md) | 30–30 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00025.md) | 31–31 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.4 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00026.md) | 32–32 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.9 ShortName &lt;ShrtNm&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00027.md) | 33–33 |
| [3 reda.015.001.01 PartyQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.14 LockStatus &lt;LckSts&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00028.md) | 34–34 |

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
