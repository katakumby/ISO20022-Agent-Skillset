---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.009.001.01"
message_family: "reda.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "30 reda.009.001.01 SecurityActivityAdviceV01", "file_pages": [1758, 1763]}, {"source_id": "src-000378", "heading": "5 reda.009.001.01 SecurityActivityAdviceV01", "file_pages": [71, 76]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.009.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 30 reda.009.001.01 SecurityActivityAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp1758–1763; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 30 reda.009.001.01 SecurityActivityAdviceV01, Functionality, file p1758.**

The SecurityActivityReport message is sent by the executing party to an instructing party containing
information about changes on securities reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities reference data.
Outline
The SecurityActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecurityActivity
Activity report of changes occurred for a financial instrument defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities 1758 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [30 reda.009.001.01 SecurityActivityAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01242.md) | 1758–1758 |
| [30 reda.009.001.01 SecurityActivityAdviceV01 / 30.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01243.md) | 1759–1759 |
| [30 reda.009.001.01 SecurityActivityAdviceV01 / 30.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01244.md) | 1760–1760 |
| [30 reda.009.001.01 SecurityActivityAdviceV01 / 30.4 Message Building Blocks / 30.4.3 SecurityActivity &lt;SctyActvty&gt; / 30.4.3.1 SystemDate &lt;SysDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01245.md) | 1761–1761 |
| [30 reda.009.001.01 SecurityActivityAdviceV01 / 30.4 Message Building Blocks / 30.4.3 SecurityActivity &lt;SctyActvty&gt; / 30.4.3.2 Change &lt;Chng&gt; / 30.4.3.2.2 FieldName &lt;FldNm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01246.md) | 1762–1762 |
| [30 reda.009.001.01 SecurityActivityAdviceV01 / 30.4 Message Building Blocks / 30.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01247.md) | 1763–1763 |

## src-000378 — 5 reda.009.001.01 SecurityActivityAdviceV01

[src-000378](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp71–76; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 5 reda.009.001.01 SecurityActivityAdviceV01, Functionality, file p71.**

The SecurityActivityReport message is sent by the executing party to an instructing party containing
information about changes on securities reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities reference data.
Outline
The SecurityActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecurityActivity
Activity report of changes occurred for a financial instrument defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 71 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 reda.009.001.01 SecurityActivityAdviceV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00031.md) | 71–71 |
| [5 reda.009.001.01 SecurityActivityAdviceV01 / 5.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00032.md) | 72–72 |
| [5 reda.009.001.01 SecurityActivityAdviceV01 / 5.4 Message Building Blocks](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00033.md) | 73–73 |
| [5 reda.009.001.01 SecurityActivityAdviceV01 / 5.4 Message Building Blocks / 5.4.3 SecurityActivity &lt;SctyActvty&gt; / 5.4.3.1 SystemDate &lt;SysDt&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00034.md) | 74–74 |
| [5 reda.009.001.01 SecurityActivityAdviceV01 / 5.4 Message Building Blocks / 5.4.3 SecurityActivity &lt;SctyActvty&gt; / 5.4.3.2 Change &lt;Chng&gt; / 5.4.3.2.2 FieldName &lt;FldNm&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00035.md) | 75–75 |
| [5 reda.009.001.01 SecurityActivityAdviceV01 / 5.4 Message Building Blocks / 5.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00036.md) | 76–76 |

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
