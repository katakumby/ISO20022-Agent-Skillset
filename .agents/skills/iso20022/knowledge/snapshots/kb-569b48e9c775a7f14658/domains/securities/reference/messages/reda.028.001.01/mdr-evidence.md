---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.028.001.01"
message_family: "reda.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"
source_ids: ["src-000233", "src-000354"]
source_locations: [{"source_id": "src-000233", "heading": "48 reda.028.001.01 CollateralDataStatusAdviceV01", "file_pages": [2193, 2202]}, {"source_id": "src-000354", "heading": "6 reda.028.001.01 CollateralDataStatusAdviceV01", "file_pages": [36, 45]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "may-2025"]
---

# reda.028.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 48 reda.028.001.01 CollateralDataStatusAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2193–2202; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 48 reda.028.001.01 CollateralDataStatusAdviceV01, Functionality, file p2193.**

The CollateralDataStatusAdvice message is sent by the executing party to an instructing party (the
requestor) to provide information of a request on collateral management reference data.
Usage:
It aims at informing about the status of the request.
Outline
The CollateralDataStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StatusReason
Specifies the reason for the status report.
C. StatusReasonAndFinancialInstrument
Specifies the reason for the status report per financial instrument and eligibility set.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2193 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01568.md) | 2193–2193 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01569.md) | 2194–2194 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01570.md) | 2195–2195 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.1 MessageHeader &lt;MsgHdr&gt; / 48.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01571.md) | 2196–2196 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.2 StatusReason &lt;StsRsn&gt; / 48.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01572.md) | 2197–2197 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.2 StatusReason &lt;StsRsn&gt; / 48.4.2.2 Reason &lt;Rsn&gt; / 48.4.2.2.1 Reason &lt;Rsn&gt; / 48.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01573.md) | 2198–2198 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 48.4.3.1 Status &lt;Sts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01574.md) | 2199–2199 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 48.4.3.2 Reason &lt;Rsn&gt; / 48.4.3.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01575.md) | 2200–2200 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 48.4.3.2 Reason &lt;Rsn&gt; / 48.4.3.2.3 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01576.md) | 2201–2201 |
| [48 reda.028.001.01 CollateralDataStatusAdviceV01 / 48.4 Message Building Blocks / 48.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 48.4.3.3 EligibilitySetProfile &lt;ElgbltySetPrfl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01577.md) | 2202–2202 |

## src-000354 — 6 reda.028.001.01 CollateralDataStatusAdviceV01

[src-000354](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; file pp36–45; publication may-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000354, 6 reda.028.001.01 CollateralDataStatusAdviceV01, Functionality, file p36.**

The CollateralDataStatusAdvice message is sent by the executing party to an instructing party (the
requestor) to provide information of a request on collateral management reference data.
Usage:
It aims at informing about the status of the request.
Outline
The CollateralDataStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StatusReason
Specifies the reason for the status report.
C. StatusReasonAndFinancialInstrument
Specifies the reason for the status report per financial instrument and eligibility set.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 36 May 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00032.md) | 36–36 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.2 Structure](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00033.md) | 37–37 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00034.md) | 38–38 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.1 MessageHeader &lt;MsgHdr&gt; / 6.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00035.md) | 39–39 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.2 StatusReason &lt;StsRsn&gt; / 6.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00036.md) | 40–40 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.2 StatusReason &lt;StsRsn&gt; / 6.4.2.2 Reason &lt;Rsn&gt; / 6.4.2.2.1 Reason &lt;Rsn&gt; / 6.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00037.md) | 41–41 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 6.4.3.1 Status &lt;Sts&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00038.md) | 42–42 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 6.4.3.2 Reason &lt;Rsn&gt; / 6.4.3.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00039.md) | 43–43 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 6.4.3.2 Reason &lt;Rsn&gt; / 6.4.3.2.3 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00040.md) | 44–44 |
| [6 reda.028.001.01 CollateralDataStatusAdviceV01 / 6.4 Message Building Blocks / 6.4.3 StatusReasonAndFinancialInstrument &lt;StsRsnAndFinInstrm&gt; / 6.4.3.3 EligibilitySetProfile &lt;ElgbltySetPrfl&gt;](../../message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/sections/section-00041.md) | 45–45 |

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
