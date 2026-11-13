---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.049.001.01"
message_family: "reda.049"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.049.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "65 reda.049.001.01 AccountLinkCreationRequestV01", "file_pages": [2369, 2374]}, {"source_id": "src-000366", "heading": "5 reda.049.001.01 AccountLinkCreationRequestV01", "file_pages": [35, 40]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.049.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 65 reda.049.001.01 AccountLinkCreationRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2369–2374; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 65 reda.049.001.01 AccountLinkCreationRequestV01, Functionality, file p2369.**

SCOPE:
The AccountLinkCreationRequest message is sent by the instructing party to the executing/servicing
party to request the creation of an account link between a securities account and a cash account in their
system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be set-up at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkCreationRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLink
Defines how the securities account is linked to the cash account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2369 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [65 reda.049.001.01 AccountLinkCreationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01721.md) | 2369–2369 |
| [65 reda.049.001.01 AccountLinkCreationRequestV01 / 65.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01722.md) | 2370–2370 |
| [65 reda.049.001.01 AccountLinkCreationRequestV01 / 65.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01723.md) | 2371–2371 |
| [65 reda.049.001.01 AccountLinkCreationRequestV01 / 65.4 Message Building Blocks / 65.4.2 AccountLink &lt;AcctLk&gt; / 65.4.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01724.md) | 2372–2372 |
| [65 reda.049.001.01 AccountLinkCreationRequestV01 / 65.4 Message Building Blocks / 65.4.2 AccountLink &lt;AcctLk&gt; / 65.4.2.4 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01725.md) | 2373–2373 |
| [65 reda.049.001.01 AccountLinkCreationRequestV01 / 65.4 Message Building Blocks / 65.4.2 AccountLink &lt;AcctLk&gt; / 65.4.2.8 CashSettlementIndicator &lt;CshSttlmInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01726.md) | 2374–2374 |

## src-000366 — 5 reda.049.001.01 AccountLinkCreationRequestV01

[src-000366](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp35–40; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 5 reda.049.001.01 AccountLinkCreationRequestV01, Functionality, file p35.**

SCOPE:
The AccountLinkCreationRequest message is sent by the instructing party to the executing/servicing
party to request the creation of an account link between a securities account and a cash account in their
system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the account link coverage of the
executing/servicing party. The instructing party needs this account link to be set-up at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The AccountLinkCreationRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLink
Defines how the securities account is linked to the cash account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 35 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 reda.049.001.01 AccountLinkCreationRequestV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00033.md) | 35–35 |
| [5 reda.049.001.01 AccountLinkCreationRequestV01 / 5.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00034.md) | 36–36 |
| [5 reda.049.001.01 AccountLinkCreationRequestV01 / 5.4 Message Building Blocks](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00035.md) | 37–37 |
| [5 reda.049.001.01 AccountLinkCreationRequestV01 / 5.4 Message Building Blocks / 5.4.2 AccountLink &lt;AcctLk&gt; / 5.4.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00036.md) | 38–38 |
| [5 reda.049.001.01 AccountLinkCreationRequestV01 / 5.4 Message Building Blocks / 5.4.2 AccountLink &lt;AcctLk&gt; / 5.4.2.4 ValidFrom &lt;VldFr&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00037.md) | 39–39 |
| [5 reda.049.001.01 AccountLinkCreationRequestV01 / 5.4 Message Building Blocks / 5.4.2 AccountLink &lt;AcctLk&gt; / 5.4.2.8 CashSettlementIndicator &lt;CshSttlmInd&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00038.md) | 40–40 |

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
