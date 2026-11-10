---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.026.001.01"
message_family: "reda.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01"
source_ids: ["src-000233", "src-000354"]
source_locations: [{"source_id": "src-000233", "heading": "46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "file_pages": [2179, 2186]}, {"source_id": "src-000354", "heading": "4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "file_pages": [22, 29]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "may-2025"]
---

# reda.026.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2179–2186; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01, Functionality, file p2179.**

The EligibleCounterpartCSDCreationRequest message is sent by an instructing party to the executing
party to request for the creation of an eligible counterpart CSD in the executing system collateral
management reference data.
Usage:
It aims at instructing the creation of a new eligible counterpart CSD with corresponding details.
Processing and confirmation of the eligible counterpart CSD creation request message are provided via
a collateral management status advice.
Outline
The EligibleCounterpartCSDCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. EligibleCounterpartCSD
Represents a party to be identified as eligible for the instructing party.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2179 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01555.md) | 2179–2179 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01556.md) | 2180–2180 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01557.md) | 2181–2181 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.4 Message Building Blocks / 46.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 46.4.2.1 IssuerIdentification &lt;IssrId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01558.md) | 2182–2182 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.4 Message Building Blocks / 46.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 46.4.2.2 EligibleCounterpartIdentification &lt;ElgblCntrptId&gt; / 46.4.2.2.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01559.md) | 2183–2183 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.4 Message Building Blocks / 46.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 46.4.2.6 EligibilityIdentification &lt;ElgbltyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01560.md) | 2184–2184 |
| [46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 46.4 Message Building Blocks / 46.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 46.4.2.6 EligibilityIdentification &lt;ElgbltyId&gt; / 46.4.2.6.3 IssuerCSDIdentification &lt;IssrCSDId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01561.md) | 2185–2186 |

## src-000354 — 4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01

[src-000354](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; file pp22–29; publication may-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000354, 4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01, Functionality, file p22.**

The EligibleCounterpartCSDCreationRequest message is sent by an instructing party to the executing
party to request for the creation of an eligible counterpart CSD in the executing system collateral
management reference data.
Usage:
It aims at instructing the creation of a new eligible counterpart CSD with corresponding details.
Processing and confirmation of the eligible counterpart CSD creation request message are provided via
a collateral management status advice.
Outline
The EligibleCounterpartCSDCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. EligibleCounterpartCSD
Represents a party to be identified as eligible for the instructing party.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities - Collateral Management Reference Data 22 May 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00019.md) | 22–22 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.2 Structure](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00020.md) | 23–23 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.4 Message Building Blocks](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00021.md) | 24–24 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.4 Message Building Blocks / 4.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 4.4.2.1 IssuerIdentification &lt;IssrId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00022.md) | 25–25 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.4 Message Building Blocks / 4.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 4.4.2.2 EligibleCounterpartIdentification &lt;ElgblCntrptId&gt; / 4.4.2.2.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00023.md) | 26–26 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.4 Message Building Blocks / 4.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 4.4.2.6 EligibilityIdentification &lt;ElgbltyId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00024.md) | 27–27 |
| [4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01 / 4.4 Message Building Blocks / 4.4.2 EligibleCounterpartCSD &lt;ElgblCntrptCSD&gt; / 4.4.2.6 EligibilityIdentification &lt;ElgbltyId&gt; / 4.4.2.6.3 IssuerCSDIdentification &lt;IssrCSDId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00025.md) | 28–29 |

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
