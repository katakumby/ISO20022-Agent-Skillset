---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.075.001.01"
message_family: "reda.075"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.075.001.01"
source_ids: ["src-000233", "src-000354"]
source_locations: [{"source_id": "src-000233", "heading": "68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "file_pages": [2389, 2394]}, {"source_id": "src-000354", "heading": "8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "file_pages": [51, 56]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "may-2025"]
---

# reda.075.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2389–2394; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01, Functionality, file p2389.**

The EligibleSecuritiesDeletionRequest message is exchanged between an instructing party and the
executing party to request for the deletion of an eligible securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the deletion of a existing eligible securities with corresponding details.
Processing and confirmation of the eligible securities deletion request message are provided via a
collateral management status advice.
Outline
The EligibleSecuritiesDeletionRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. EligibleSecurity
Represents securities defined eligible for auto-collateralisation.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities 2389 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01739.md) | 2389–2389 |
| [68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 68.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01740.md) | 2390–2390 |
| [68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 68.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01741.md) | 2391–2392 |
| [68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 68.4 Message Building Blocks / 68.4.2 EligibleSecurity &lt;ElgblScty&gt; / 68.4.2.2 CollateralisationCurrency &lt;CollstnCcy&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01742.md) | 2393–2393 |
| [68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 68.4 Message Building Blocks / 68.4.2 EligibleSecurity &lt;ElgblScty&gt; / 68.4.2.4 PartyIdentification &lt;PtyId&gt; / 68.4.2.4.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01743.md) | 2394–2394 |

## src-000354 — 8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01

[src-000354](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; file pp51–56; publication may-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000354, 8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01, Functionality, file p51.**

The EligibleSecuritiesDeletionRequest message is exchanged between an instructing party and the
executing party to request for the deletion of an eligible securities in the executing system collateral
management reference data.
Usage:
It aims at instructing the deletion of a existing eligible securities with corresponding details.
Processing and confirmation of the eligible securities deletion request message are provided via a
collateral management status advice.
Outline
The EligibleSecuritiesDeletionRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. EligibleSecurity
Represents securities defined eligible for auto-collateralisation.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 51 May 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00047.md) | 51–51 |
| [8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 8.2 Structure](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00048.md) | 52–52 |
| [8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 8.4 Message Building Blocks](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00049.md) | 53–54 |
| [8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 8.4 Message Building Blocks / 8.4.2 EligibleSecurity &lt;ElgblScty&gt; / 8.4.2.2 CollateralisationCurrency &lt;CollstnCcy&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00050.md) | 55–55 |
| [8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01 / 8.4 Message Building Blocks / 8.4.2 EligibleSecurity &lt;ElgblScty&gt; / 8.4.2.4 PartyIdentification &lt;PtyId&gt; / 8.4.2.4.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00051.md) | 56–56 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000353-account-owner.md) | participant | src-000353 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000353-account-servicer.md) | participant | src-000353 |
| [Central Database System](../../../../../shared/reference/participants/participant-src-000353-central-database-system.md) | participant | src-000353 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000353-central-securities-depository-csd.md) | participant | src-000353 |
| [Collateral Management System](../../../../../shared/reference/participants/participant-src-000353-collateral-management-system.md) | participant | src-000353 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | participant | src-000353 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | participant | src-000353 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000353-market-infrastructure.md) | participant | src-000353 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000353-national-central-bank.md) | participant | src-000353 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000353-payment-bank.md) | participant | src-000353 |
| [Collateral Reference Data creation](../../message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p104-collateral-reference-data-creation.md) | business-flow | src-000353 |
| [Collateral Reference Data deletion](../../message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p105-collateral-reference-data-deletion.md) | business-flow | src-000353 |
| [Collateral Reference Data creation](../../message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p110-collateral-reference-data-creation.md) | business-flow | src-000353 |
| [Collateral Reference Data deletion](../../message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p115-collateral-reference-data-deletion.md) | business-flow | src-000353 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
