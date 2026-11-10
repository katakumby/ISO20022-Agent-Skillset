---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.008.001.01"
message_family: "reda.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.008.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "29 reda.008.001.01 SecurityCreationStatusAdviceV01", "file_pages": [1753, 1757]}, {"source_id": "src-000378", "heading": "4 reda.008.001.01 SecurityCreationStatusAdviceV01", "file_pages": [66, 70]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.008.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 29 reda.008.001.01 SecurityCreationStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp1753–1757; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 29 reda.008.001.01 SecurityCreationStatusAdviceV01, Functionality, file p1753.**

SCOPE
An executing/servicing party sends a SecurityCreationStatusAdvice message to an instructing party to
report the status of a SecurityCreationRequest message previously sent by the instructing party.
The SecurityCreationStatusAdvice message may be sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCreationStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
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
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities 1753 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [29 reda.008.001.01 SecurityCreationStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01237.md) | 1753–1753 |
| [29 reda.008.001.01 SecurityCreationStatusAdviceV01 / 29.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01238.md) | 1754–1754 |
| [29 reda.008.001.01 SecurityCreationStatusAdviceV01 / 29.4 Message Building Blocks / 29.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01239.md) | 1755–1755 |
| [29 reda.008.001.01 SecurityCreationStatusAdviceV01 / 29.4 Message Building Blocks / 29.4.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01240.md) | 1756–1756 |
| [29 reda.008.001.01 SecurityCreationStatusAdviceV01 / 29.4 Message Building Blocks / 29.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01241.md) | 1757–1757 |

## src-000378 — 4 reda.008.001.01 SecurityCreationStatusAdviceV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp66–70; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 4 reda.008.001.01 SecurityCreationStatusAdviceV01, Functionality, file p66.**

SCOPE
An executing/servicing party sends a SecurityCreationStatusAdvice message to an instructing party to
report the status of a SecurityCreationRequest message previously sent by the instructing party.
The SecurityCreationStatusAdvice message may be sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCreationStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
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
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities - Securities Reference Data 66 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.008.001.01 SecurityCreationStatusAdviceV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00026.md) | 66–66 |
| [4 reda.008.001.01 SecurityCreationStatusAdviceV01 / 4.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00027.md) | 67–67 |
| [4 reda.008.001.01 SecurityCreationStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00028.md) | 68–68 |
| [4 reda.008.001.01 SecurityCreationStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00029.md) | 69–69 |
| [4 reda.008.001.01 SecurityCreationStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00030.md) | 70–70 |

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
