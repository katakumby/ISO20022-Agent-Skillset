---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.010.001.01"
message_family: "reda.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "31 reda.010.001.01 SecurityQueryV01", "file_pages": [1764, 1783]}, {"source_id": "src-000378", "heading": "6 reda.010.001.01 SecurityQueryV01", "file_pages": [77, 93]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.010.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 31 reda.010.001.01 SecurityQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp1764–1783; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 31 reda.010.001.01 SecurityQueryV01, Functionality, file p1764.**

SCOPE
An instructing party sends a SecurityQuery message to an executing/servicing party to request a report
of financial instrument details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party needs to see data of a security data within the executing/
servicing party system.
Initiator: instructing party.
Outline
The SecurityQueryV01 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. RequestType
Defines the type of action to be performed in the request.
C. SearchCriteria
Defines the criteria to be used to query the securities reference data by the executing system.
D. SmallSetReturnCriteria
Defines the expected securities reference data to be returned.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1764 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [31 reda.010.001.01 SecurityQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01248.md) | 1764–1764 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01249.md) | 1765–1766 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01250.md) | 1767–1767 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.2 RequestType &lt;ReqTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01251.md) | 1768–1769 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01252.md) | 1770–1770 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.2 ClassificationFinancialInstrument &lt;ClssfctnFinInstrm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01253.md) | 1771–1771 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.3 MaturityDate &lt;MtrtyDt&gt; / 31.4.3.3.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01254.md) | 1772–1772 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.4 IssueDate &lt;IsseDt&gt; / 31.4.3.4.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01255.md) | 1773–1773 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.7 SecurityStatus &lt;SctySts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01256.md) | 1774–1774 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.8 MaintainingCSD &lt;MntngCSD&gt; / 31.4.3.8.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01257.md) | 1775–1775 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.9 InvestorCSD &lt;InvstrCSD&gt; / 31.4.3.9.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01258.md) | 1776–1776 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.11 TechnicalIssuerCSD &lt;TechIssrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01259.md) | 1777–1777 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.3 SearchCriteria &lt;SchCrit&gt; / 31.4.3.12 CSD &lt;CSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01260.md) | 1778–1778 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 31.4.4.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01261.md) | 1779–1779 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 31.4.4.3 ISOSecurityShortName &lt;ISOSctyShrtNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01262.md) | 1780–1780 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 31.4.4.9 SecurityStatus &lt;SctySts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01263.md) | 1781–1781 |
| [31 reda.010.001.01 SecurityQueryV01 / 31.4 Message Building Blocks / 31.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 31.4.4.14 SecuritiesQuantityType &lt;SctiesQtyTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01264.md) | 1782–1783 |

## src-000378 — 6 reda.010.001.01 SecurityQueryV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp77–93; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 6 reda.010.001.01 SecurityQueryV01, Functionality, file p77.**

SCOPE
An instructing party sends a SecurityQuery message to an executing/servicing party to request a report
of financial instrument details in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party needs to see data of a security data within the executing/
servicing party system.
Initiator: instructing party.
Outline
The SecurityQueryV01 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. RequestType
Defines the type of action to be performed in the request.
C. SearchCriteria
Defines the criteria to be used to query the securities reference data by the executing system.
D. SmallSetReturnCriteria
Defines the expected securities reference data to be returned.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 77 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.010.001.01 SecurityQueryV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00037.md) | 77–77 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00038.md) | 78–78 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.3 Constraints](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00039.md) | 79–79 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00040.md) | 80–80 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00041.md) | 81–81 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00042.md) | 82–82 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.2 ClassificationFinancialInstrument &lt;ClssfctnFinInstrm&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00043.md) | 83–83 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.3 MaturityDate &lt;MtrtyDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00044.md) | 84–84 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.4 IssueDate &lt;IsseDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00045.md) | 85–85 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.4 IssueDate &lt;IsseDt&gt; / 6.4.3.4.5 NotEqualDate &lt;NEQDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00046.md) | 86–86 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.7 SecurityStatus &lt;SctySts&gt; / 6.4.3.7.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00047.md) | 87–87 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.3 SearchCriteria &lt;SchCrit&gt; / 6.4.3.11 TechnicalIssuerCSD &lt;TechIssrCSD&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00048.md) | 88–88 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 6.4.4.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00049.md) | 89–89 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 6.4.4.3 ISOSecurityShortName &lt;ISOSctyShrtNm&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00050.md) | 90–90 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 6.4.4.9 SecurityStatus &lt;SctySts&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00051.md) | 91–91 |
| [6 reda.010.001.01 SecurityQueryV01 / 6.4 Message Building Blocks / 6.4.4 SmallSetReturnCriteria &lt;SmlSetRtrCrit&gt; / 6.4.4.14 SecuritiesQuantityType &lt;SctiesQtyTp&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00052.md) | 92–93 |

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
