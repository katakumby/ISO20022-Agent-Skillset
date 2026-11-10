---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.029.001.01"
message_family: "reda.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.029.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "file_pages": [2203, 2207]}, {"source_id": "src-000378", "heading": "9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "file_pages": [119, 123]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.029.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2203–2207; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01, Functionality, file p2203.**

SCOPE
An executing/servicing party sends a SecurityMaintenanceStatusAdvice message to an instructing party
to report the status of a SecurityMaintencanceRequest message previously sent by the instructing
party.
The SecurityMaintenanceStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityMaintenanceStatusAdviceV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. ProcessingStatus
Represents the processing status.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
Target2-Securities 2203 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01578.md) | 2203–2203 |
| [49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 49.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01579.md) | 2204–2204 |
| [49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 49.4 Message Building Blocks / 49.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01580.md) | 2205–2205 |
| [49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 49.4 Message Building Blocks / 49.4.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01581.md) | 2206–2206 |
| [49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 49.4 Message Building Blocks / 49.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01582.md) | 2207–2207 |

## src-000378 — 9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp119–123; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01, Functionality, file p119.**

SCOPE
An executing/servicing party sends a SecurityMaintenanceStatusAdvice message to an instructing party
to report the status of a SecurityMaintencanceRequest message previously sent by the instructing
party.
The SecurityMaintenanceStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityMaintenanceStatusAdviceV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. ProcessingStatus
Represents the processing status.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
Target2-Securities - Securities Reference Data 119 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00070.md) | 119–119 |
| [9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 9.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00071.md) | 120–120 |
| [9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 9.4 Message Building Blocks / 9.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00072.md) | 121–121 |
| [9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 9.4 Message Building Blocks / 9.4.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00073.md) | 122–122 |
| [9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01 / 9.4 Message Building Blocks / 9.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00074.md) | 123–123 |

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
