---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.024.001.01"
message_family: "reda.024"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01"
source_ids: ["src-000233", "src-000354"]
source_locations: [{"source_id": "src-000233", "heading": "44 reda.024.001.01 CollateralValueCreationRequestV01", "file_pages": [2163, 2172]}, {"source_id": "src-000354", "heading": "2 reda.024.001.01 CollateralValueCreationRequestV01", "file_pages": [6, 15]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "may-2025"]
---

# reda.024.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 44 reda.024.001.01 CollateralValueCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2163–2172; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 44 reda.024.001.01 CollateralValueCreationRequestV01, Functionality, file p2163.**

The CollateralValueCreationRequest message is sent by the instructing party to the executing party to
request for the creation of a collateral value in the executing system collateral management reference
data.
Usage:
It aims at instructing the creation of a new collateral value with corresponding details.
Processing and confirmation of the collateral value creation request message are provided via a
collateral management status advice.
Outline
The CollateralValueCreationRequestV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CollateralValue
Represents the valuation of securities positions for auto-collateralisation.
C. PartyIdentification
Identifies the party for which the eligible security is defined.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2163 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [44 reda.024.001.01 CollateralValueCreationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01540.md) | 2163–2163 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01541.md) | 2164–2164 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01542.md) | 2165–2165 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01543.md) | 2166–2166 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.2 CollateralValue &lt;CollVal&gt; / 44.4.2.1 SecurityIdentification &lt;SctyId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01544.md) | 2167–2167 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.2 CollateralValue &lt;CollVal&gt; / 44.4.2.2 ValuationDate &lt;ValtnDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01545.md) | 2168–2168 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.2 CollateralValue &lt;CollVal&gt; / 44.4.2.4 ValuationPrice &lt;ValtnPric&gt; / 44.4.2.4.3 Coefficient &lt;Coeff&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01546.md) | 2169–2169 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.2 CollateralValue &lt;CollVal&gt; / 44.4.2.5 ValuationCloseLinkPrice &lt;ValtnClsLkPric&gt; / 44.4.2.5.3 Coefficient &lt;Coeff&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01547.md) | 2170–2170 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.2 CollateralValue &lt;CollVal&gt; / 44.4.2.9 CloseLinkHaircut &lt;ClsLkHrcut&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01548.md) | 2171–2171 |
| [44 reda.024.001.01 CollateralValueCreationRequestV01 / 44.4 Message Building Blocks / 44.4.3 PartyIdentification &lt;PtyId&gt; / 44.4.3.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01549.md) | 2172–2172 |

## src-000354 — 2 reda.024.001.01 CollateralValueCreationRequestV01

[src-000354](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; file pp6–15; publication may-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000354, 2 reda.024.001.01 CollateralValueCreationRequestV01, Functionality, file p6.**

The CollateralValueCreationRequest message is sent by the instructing party to the executing party to
request for the creation of a collateral value in the executing system collateral management reference
data.
Usage:
It aims at instructing the creation of a new collateral value with corresponding details.
Processing and confirmation of the collateral value creation request message are provided via a
collateral management status advice.
Outline
The CollateralValueCreationRequestV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CollateralValue
Represents the valuation of securities positions for auto-collateralisation.
C. PartyIdentification
Identifies the party for which the eligible security is defined.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 6 May 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 reda.024.001.01 CollateralValueCreationRequestV01](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00004.md) | 6–6 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.2 Structure](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00005.md) | 7–7 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00006.md) | 8–8 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00007.md) | 9–9 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 CollateralValue &lt;CollVal&gt; / 2.4.2.1 SecurityIdentification &lt;SctyId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00008.md) | 10–10 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 CollateralValue &lt;CollVal&gt; / 2.4.2.2 ValuationDate &lt;ValtnDt&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00009.md) | 11–11 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 CollateralValue &lt;CollVal&gt; / 2.4.2.4 ValuationPrice &lt;ValtnPric&gt; / 2.4.2.4.3 Coefficient &lt;Coeff&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00010.md) | 12–12 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 CollateralValue &lt;CollVal&gt; / 2.4.2.5 ValuationCloseLinkPrice &lt;ValtnClsLkPric&gt; / 2.4.2.5.3 Coefficient &lt;Coeff&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00011.md) | 13–13 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 CollateralValue &lt;CollVal&gt; / 2.4.2.9 CloseLinkHaircut &lt;ClsLkHrcut&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00012.md) | 14–14 |
| [2 reda.024.001.01 CollateralValueCreationRequestV01 / 2.4 Message Building Blocks / 2.4.3 PartyIdentification &lt;PtyId&gt; / 2.4.3.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00013.md) | 15–15 |

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
