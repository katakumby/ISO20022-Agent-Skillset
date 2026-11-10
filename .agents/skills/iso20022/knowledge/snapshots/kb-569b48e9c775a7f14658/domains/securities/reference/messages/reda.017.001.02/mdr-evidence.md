---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.017.001.02"
message_family: "reda.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.017.001.02"
source_ids: ["src-000233", "src-000369"]
source_locations: [{"source_id": "src-000233", "heading": "37 reda.017.001.02 PartyReportV02", "file_pages": [2078, 2097]}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41, 60]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# reda.017.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 37 reda.017.001.02 PartyReportV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2078–2097; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 37 reda.017.001.02 PartyReportV02, Functionality, file p2078.**

Scope:
The PartyReport message is sent by the executing party to a central securities depository, a national
central bank, a central securities depository participant, a central counter party, a payment bank, a
trading party or a stock exchange to provide detailed information on the requested party reference data
of the party defined in the system.
Outline
The PartyReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the report message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2078 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [37 reda.017.001.02 PartyReportV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01464.md) | 2078–2078 |
| [37 reda.017.001.02 PartyReportV02 / 37.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01465.md) | 2079–2079 |
| [37 reda.017.001.02 PartyReportV02 / 37.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01466.md) | 2080–2080 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01467.md) | 2081–2082 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01468.md) | 2083–2084 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01469.md) | 2085–2086 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01470.md) | 2087–2088 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01471.md) | 2089–2089 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.3 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01472.md) | 2090–2090 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01473.md) | 2091–2091 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.6 Type &lt;Tp&gt; / 37.4.2.1.2.1.6.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01474.md) | 2092–2092 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01475.md) | 2093–2093 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.10 ResidenceType &lt;ResTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01476.md) | 2094–2094 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 37.4.2.1.2.1.12 Restriction &lt;Rstrctn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01477.md) | 2095–2095 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.1 PartyReport &lt;PtyRpt&gt; / 37.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 37.4.2.1.2.2 BusinessError &lt;BizErr&gt; / 37.4.2.1.2.2.1 Error &lt;Err&gt; / 37.4.2.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01478.md) | 2096–2096 |
| [37 reda.017.001.02 PartyReportV02 / 37.4 Message Building Blocks / 37.4.2 ReportOrError &lt;RptOrErr&gt; / 37.4.2.2 OperationalError &lt;OprlErr&gt; / 37.4.2.2.1 Error &lt;Err&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01479.md) | 2097–2097 |

## src-000369 — 5 reda.017.001.02 PartyReportV02

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; file pp41–60; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000369, 5 reda.017.001.02 PartyReportV02, Functionality, file p41.**

Scope:
The PartyReport message is sent by the executing party to a central securities depository, a national
central bank, a central securities depository participant, a central counter party, a payment bank, a
trading party or a stock exchange to provide detailed information on the requested party reference data
of the party defined in the system.
Outline
The PartyReportV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the report message.
B. ReportOrError
Provides information on report or error resulting from the originating query message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
41 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 reda.017.001.02 PartyReportV02](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00035.md) | 41–41 |
| [5 reda.017.001.02 PartyReportV02 / 5.2 Structure](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00036.md) | 42–42 |
| [5 reda.017.001.02 PartyReportV02 / 5.3 Constraints](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00037.md) | 43–43 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00038.md) | 44–45 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00039.md) | 46–47 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00040.md) | 48–49 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00041.md) | 50–51 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.1 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00042.md) | 52–52 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.3 ContactDetails &lt;CtctDtls&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00043.md) | 53–53 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00044.md) | 54–54 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.6 Type &lt;Tp&gt; / 5.4.2.1.2.1.6.1 Code &lt;Cd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00045.md) | 55–55 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00046.md) | 56–56 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.10 ResidenceType &lt;ResTp&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00047.md) | 57–57 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.1 SystemParty &lt;SysPty&gt; / 5.4.2.1.2.1.12 Restriction &lt;Rstrctn&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00048.md) | 58–58 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 PartyReport &lt;PtyRpt&gt; / 5.4.2.1.2 PartyOrError &lt;PtyOrErr&gt; / 5.4.2.1.2.2 BusinessError &lt;BizErr&gt; / 5.4.2.1.2.2.1 Error &lt;Err&gt; / 5.4.2.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00049.md) | 59–59 |
| [5 reda.017.001.02 PartyReportV02 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.2 OperationalError &lt;OprlErr&gt; / 5.4.2.2.1 Error &lt;Err&gt;](../../message-sets/t2s-party-reference-data/march-2024/documents/src-000369/sections/section-00050.md) | 60–60 |

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
