---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.045.001.01"
message_family: "reda.045"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "file_pages": [2340, 2350]}, {"source_id": "src-000366", "heading": "2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "file_pages": [6, 16]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.045.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 62 reda.045.001.01 SecurityCSDLinkCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2340–2350; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 62 reda.045.001.01 SecurityCSDLinkCreationRequestV01, Functionality, file p2340.**

SCOPE
An instructing party sends a SecurityCSDLinkCreationRequest message to an executing/servicing party
to request the creation of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security CSD Link to be set-up at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLink
This Securities CSD Link logical entity shall assign a security to a CSD in T2S in order to define the
eligibility of the instrument for settlement in that CSD. An attribute within this entity shall specify
which CSD is responsible for maintaining the instrument static data.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2340 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01692.md) | 2340–2340 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01693.md) | 2341–2341 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01694.md) | 2342–2342 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01695.md) | 2343–2343 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01696.md) | 2344–2344 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 62.4.2.2.1 IssuerCSD &lt;IssrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01697.md) | 2345–2345 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 62.4.2.2.2 InvestorCSD &lt;InvstrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01698.md) | 2346–2346 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.3 TechnicalIssuerCSD &lt;TechIssrCSD&gt; / 62.4.2.3.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01699.md) | 2347–2347 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.5 IssuanceAccount &lt;IssncAcct&gt; / 62.4.2.5.1 IssuanceAccount &lt;IssncAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01700.md) | 2348–2348 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 62.4.2.5 IssuanceAccount &lt;IssncAcct&gt; / 62.4.2.5.3 PrimaryAccountIndicator &lt;PmryAcctInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01701.md) | 2349–2349 |
| [62 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 62.4 Message Building Blocks / 62.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01702.md) | 2350–2350 |

## src-000366 — 2 reda.045.001.01 SecurityCSDLinkCreationRequestV01

[src-000366](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp6–16; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 2 reda.045.001.01 SecurityCSDLinkCreationRequestV01, Functionality, file p6.**

SCOPE
An instructing party sends a SecurityCSDLinkCreationRequest message to an executing/servicing party
to request the creation of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security CSD Link to be set-up at the
executing /servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLink
This Securities CSD Link logical entity shall assign a security to a CSD in T2S in order to define the
eligibility of the instrument for settlement in that CSD. An attribute within this entity shall specify
which CSD is responsible for maintaining the instrument static data.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 6 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00004.md) | 6–6 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00005.md) | 7–7 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00006.md) | 8–8 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00007.md) | 9–9 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00008.md) | 10–10 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 2.4.2.2.1 IssuerCSD &lt;IssrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00009.md) | 11–11 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 2.4.2.2.2 InvestorCSD &lt;InvstrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00010.md) | 12–12 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.3 TechnicalIssuerCSD &lt;TechIssrCSD&gt; / 2.4.2.3.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00011.md) | 13–13 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.5 IssuanceAccount &lt;IssncAcct&gt; / 2.4.2.5.1 IssuanceAccount &lt;IssncAcct&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00012.md) | 14–14 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecurityCSDLink &lt;SctyCSDLk&gt; / 2.4.2.5 IssuanceAccount &lt;IssncAcct&gt; / 2.4.2.5.3 PrimaryAccountIndicator &lt;PmryAcctInd&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00013.md) | 15–15 |
| [2 reda.045.001.01 SecurityCSDLinkCreationRequestV01 / 2.4 Message Building Blocks / 2.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00014.md) | 16–16 |

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
