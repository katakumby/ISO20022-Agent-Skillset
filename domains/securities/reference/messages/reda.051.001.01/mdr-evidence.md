---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.051.001.01"
message_family: "reda.051"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "67 reda.051.001.01 AccountLinkStatusAdviceV01", "file_pages": [2381, 2388]}, {"source_id": "src-000366", "heading": "7 reda.051.001.01 AccountLinkStatusAdviceV01", "file_pages": [47, 54]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.051.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 67 reda.051.001.01 AccountLinkStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2381–2388; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 67 reda.051.001.01 AccountLinkStatusAdviceV01, Functionality, file p2381.**

SCOPE:
The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party
to provide details about the processing of a request on account link reference data (create or update).
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is successfully performed, the message includes the related account link
identification.
Outline
The AccountLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkStatus
Represents the processing status.
C. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2381 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01732.md) | 2381–2381 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01733.md) | 2382–2382 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01734.md) | 2383–2383 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.4 Message Building Blocks / 67.4.2 AccountLinkStatus &lt;AcctLkSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01735.md) | 2384–2384 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.4 Message Building Blocks / 67.4.2 AccountLinkStatus &lt;AcctLkSts&gt; / 67.4.2.2 StatusReason &lt;StsRsn&gt; / 67.4.2.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01736.md) | 2385–2385 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.4 Message Building Blocks / 67.4.3 AccountLinkIdentification &lt;AcctLkId&gt; / 67.4.3.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01737.md) | 2386–2386 |
| [67 reda.051.001.01 AccountLinkStatusAdviceV01 / 67.4 Message Building Blocks / 67.4.3 AccountLinkIdentification &lt;AcctLkId&gt; / 67.4.3.3 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01738.md) | 2387–2388 |

## src-000366 — 7 reda.051.001.01 AccountLinkStatusAdviceV01

[src-000366](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp47–54; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 7 reda.051.001.01 AccountLinkStatusAdviceV01, Functionality, file p47.**

SCOPE:
The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party
to provide details about the processing of a request on account link reference data (create or update).
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is successfully performed, the message includes the related account link
identification.
Outline
The AccountLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountLinkStatus
Represents the processing status.
C. AccountLinkIdentification
Provides a unique and unambiguous identification for the account link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 47 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00044.md) | 47–47 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00045.md) | 48–48 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.4 Message Building Blocks](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00046.md) | 49–49 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.4 Message Building Blocks / 7.4.2 AccountLinkStatus &lt;AcctLkSts&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00047.md) | 50–50 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.4 Message Building Blocks / 7.4.2 AccountLinkStatus &lt;AcctLkSts&gt; / 7.4.2.2 StatusReason &lt;StsRsn&gt; / 7.4.2.2.1 Reason &lt;Rsn&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00048.md) | 51–51 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.4 Message Building Blocks / 7.4.3 AccountLinkIdentification &lt;AcctLkId&gt; / 7.4.3.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00049.md) | 52–52 |
| [7 reda.051.001.01 AccountLinkStatusAdviceV01 / 7.4 Message Building Blocks / 7.4.3 AccountLinkIdentification &lt;AcctLkId&gt; / 7.4.3.3 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00050.md) | 53–54 |

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
