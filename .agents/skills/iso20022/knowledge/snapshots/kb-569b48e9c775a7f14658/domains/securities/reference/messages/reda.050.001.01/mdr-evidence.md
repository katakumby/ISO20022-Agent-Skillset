---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.050.001.01"
message_family: "reda.050"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.050.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "66 reda.050.001.01 AccountLinkMaintenanceRequestV01", "file_pages": [2375, 2380]}, {"source_id": "src-000366", "heading": "6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "file_pages": [41, 46]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.050.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 66 reda.050.001.01 AccountLinkMaintenanceRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2375–2380; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 66 reda.050.001.01 AccountLinkMaintenanceRequestV01, Functionality, file p2375.**

SCOPE:
The AccountLinkMaintenanceRequest message is sent by the instructing party to the executing/
servicing party to request for the maintenance of an account link in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be maintained at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2375 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [66 reda.050.001.01 AccountLinkMaintenanceRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01727.md) | 2375–2375 |
| [66 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 66.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01728.md) | 2376–2376 |
| [66 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 66.4 Message Building Blocks / 66.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01729.md) | 2377–2377 |
| [66 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 66.4 Message Building Blocks / 66.4.2 AccountLinkIdentification &lt;AcctLkId&gt; / 66.4.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01730.md) | 2378–2378 |
| [66 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 66.4 Message Building Blocks / 66.4.3 Update &lt;Upd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01731.md) | 2379–2380 |

## src-000366 — 6 reda.050.001.01 AccountLinkMaintenanceRequestV01

[src-000366](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp41–46; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 6 reda.050.001.01 AccountLinkMaintenanceRequestV01, Functionality, file p41.**

SCOPE:
The AccountLinkMaintenanceRequest message is sent by the instructing party to the executing/
servicing party to request for the maintenance of an account link in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be maintained at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 41 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.050.001.01 AccountLinkMaintenanceRequestV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00039.md) | 41–41 |
| [6 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 6.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00040.md) | 42–42 |
| [6 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 6.4 Message Building Blocks / 6.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00041.md) | 43–43 |
| [6 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 6.4 Message Building Blocks / 6.4.2 AccountLinkIdentification &lt;AcctLkId&gt; / 6.4.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00042.md) | 44–44 |
| [6 reda.050.001.01 AccountLinkMaintenanceRequestV01 / 6.4 Message Building Blocks / 6.4.3 Update &lt;Upd&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00043.md) | 45–46 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000365-bank.md) | participant | src-000365 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000365-central-securities-depositories-csd.md) | participant | src-000365 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000365-corporate.md) | participant | src-000365 |
| [CSD](../../../../../shared/reference/participants/participant-src-000365-csd.md) | participant | src-000365 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | participant | src-000365 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | participant | src-000365 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000365-market-data-provider.md) | participant | src-000365 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000365-market-infrastructure.md) | participant | src-000365 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000365-national-central-bank-ncb.md) | participant | src-000365 |
| [NCB](../../../../../shared/reference/participants/participant-src-000365-ncb.md) | participant | src-000365 |
| [Link Creation Process](../../message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md) | business-flow | src-000365 |
| [Link Modification Process](../../message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md) | business-flow | src-000365 |
| [Link Creation Process](../../message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p128-link-creation-process.md) | business-flow | src-000365 |
| [Link Modification Process](../../message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p132-link-modification-process.md) | business-flow | src-000365 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
