---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.013.001.01"
message_family: "reda.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.013.001.01"
source_ids: ["src-000233", "src-000378"]
source_locations: [{"source_id": "src-000233", "heading": "33 reda.013.001.01 SecurityDeletionRequestV01", "file_pages": [2039, 2042]}, {"source_id": "src-000378", "heading": "8 reda.013.001.01 SecurityDeletionRequestV01", "file_pages": [115, 118]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "March 2024"]
---

# reda.013.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 33 reda.013.001.01 SecurityDeletionRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2039–2042; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 33 reda.013.001.01 SecurityDeletionRequestV01, Functionality, file p2039.**

SCOPE
An instructing party sends a SecurityDeletionRequest message to an executing/servicing party to
advice the complete removal of a financial instrument entry from their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified that a security is wrongly created in the
securities coverage of the executing/servicing party. The instructing party needs this security to be
removed from the executing /servicing party database.
This message can be used when a security identification code was issued too quickly or if a security
identification code needs to be reused (for example, in case of money market instrument). The result of
this message is a complete removal of the security identification from the executing/servicing party's
database.
Initiator: instructing party.
Outline
The SecurityDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities 2039 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [33 reda.013.001.01 SecurityDeletionRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01429.md) | 2039–2039 |
| [33 reda.013.001.01 SecurityDeletionRequestV01 / 33.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01430.md) | 2040–2040 |
| [33 reda.013.001.01 SecurityDeletionRequestV01 / 33.4 Message Building Blocks / 33.4.2 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01431.md) | 2041–2041 |
| [33 reda.013.001.01 SecurityDeletionRequestV01 / 33.4 Message Building Blocks / 33.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01432.md) | 2042–2042 |

## src-000378 — 8 reda.013.001.01 SecurityDeletionRequestV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; file pp115–118; publication March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000378, 8 reda.013.001.01 SecurityDeletionRequestV01, Functionality, file p115.**

SCOPE
An instructing party sends a SecurityDeletionRequest message to an executing/servicing party to
advice the complete removal of a financial instrument entry from their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified that a security is wrongly created in the
securities coverage of the executing/servicing party. The instructing party needs this security to be
removed from the executing /servicing party database.
This message can be used when a security identification code was issued too quickly or if a security
identification code needs to be reused (for example, in case of money market instrument). The result of
this message is a complete removal of the security identification from the executing/servicing party's
database.
Initiator: instructing party.
Outline
The SecurityDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. FinancialInstrumentIdentification
Identification of the financial instrument.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities - Securities Reference Data 115 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 reda.013.001.01 SecurityDeletionRequestV01](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00066.md) | 115–115 |
| [8 reda.013.001.01 SecurityDeletionRequestV01 / 8.2 Structure](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00067.md) | 116–116 |
| [8 reda.013.001.01 SecurityDeletionRequestV01 / 8.4 Message Building Blocks / 8.4.2 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00068.md) | 117–117 |
| [8 reda.013.001.01 SecurityDeletionRequestV01 / 8.4 Message Building Blocks / 8.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/sections/section-00069.md) | 118–118 |

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
