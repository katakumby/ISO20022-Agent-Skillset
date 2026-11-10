---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.077.001.01"
message_family: "reda.077"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.077.001.01"
source_ids: ["src-000233", "src-000354"]
source_locations: [{"source_id": "src-000233", "heading": "69 reda.077.001.01 CloseLinkDeletionRequestV01", "file_pages": [2395, 2400]}, {"source_id": "src-000354", "heading": "9 reda.077.001.01 CloseLinkDeletionRequestV01", "file_pages": [57, 62]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "may-2025"]
---

# reda.077.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 69 reda.077.001.01 CloseLinkDeletionRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2395–2400; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 69 reda.077.001.01 CloseLinkDeletionRequestV01, Functionality, file p2395.**

The CloseLinkDeletionRequest message is sent by an instructing party to the executing party to request
for the deletion of a close link in the executing system collateral management reference data.
Usage:
It aims at instructing the deletion of an existing close link with corresponding details.
Processing and confirmation of the close link creation request message are provided via a collateral
management status advice.
Outline
The CloseLinkDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CloseLink
Represents a linkage between issuer/debtor/guarantor and its counterparty.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.077.001.01 CloseLinkDeletionRequestV01
Target2-Securities 2395 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01744.md) | 2395–2395 |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01 / 69.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01745.md) | 2396–2396 |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01 / 69.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01746.md) | 2397–2397 |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01 / 69.4 Message Building Blocks / 69.4.2 CloseLink &lt;ClsLk&gt; / 69.4.2.2 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01747.md) | 2398–2398 |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01 / 69.4 Message Building Blocks / 69.4.2 CloseLink &lt;ClsLk&gt; / 69.4.2.2 PartyIdentification &lt;PtyId&gt; / 69.4.2.2.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01748.md) | 2399–2399 |
| [69 reda.077.001.01 CloseLinkDeletionRequestV01 / 69.4 Message Building Blocks / 69.4.2 CloseLink &lt;ClsLk&gt; / 69.4.2.3 CreditProviderIdentification &lt;CdtPrvdrId&gt; / 69.4.2.3.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01749.md) | 2400–2400 |

## src-000354 — 9 reda.077.001.01 CloseLinkDeletionRequestV01

[src-000354](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; file pp57–62; publication may-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000354, 9 reda.077.001.01 CloseLinkDeletionRequestV01, Functionality, file p57.**

The CloseLinkDeletionRequest message is sent by an instructing party to the executing party to request
for the deletion of a close link in the executing system collateral management reference data.
Usage:
It aims at instructing the deletion of an existing close link with corresponding details.
Processing and confirmation of the close link creation request message are provided via a collateral
management status advice.
Outline
The CloseLinkDeletionRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CloseLink
Represents a linkage between issuer/debtor/guarantor and its counterparty.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.077.001.01 CloseLinkDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 57 May 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00052.md) | 57–57 |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01 / 9.2 Structure](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00053.md) | 58–58 |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01 / 9.4 Message Building Blocks](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00054.md) | 59–59 |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01 / 9.4 Message Building Blocks / 9.4.2 CloseLink &lt;ClsLk&gt; / 9.4.2.2 PartyIdentification &lt;PtyId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00055.md) | 60–60 |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01 / 9.4 Message Building Blocks / 9.4.2 CloseLink &lt;ClsLk&gt; / 9.4.2.2 PartyIdentification &lt;PtyId&gt; / 9.4.2.2.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00056.md) | 61–61 |
| [9 reda.077.001.01 CloseLinkDeletionRequestV01 / 9.4 Message Building Blocks / 9.4.2 CloseLink &lt;ClsLk&gt; / 9.4.2.3 CreditProviderIdentification &lt;CdtPrvdrId&gt; / 9.4.2.3.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00057.md) | 62–62 |

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
