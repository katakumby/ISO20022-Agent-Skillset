---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.046.001.01"
message_family: "reda.046"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.046.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "file_pages": [2351, 2358]}, {"source_id": "src-000366", "heading": "3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "file_pages": [17, 24]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.046.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2351–2358; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01, Functionality, file p2351.**

SCOPE
An instructing party sends a SecurityCSDLinkMaintenanceRequest message to an executing/servicing
party to request the maintenance of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security to be maintained at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities 2351 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01703.md) | 2351–2351 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01704.md) | 2352–2352 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01705.md) | 2353–2353 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks / 63.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 63.4.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01706.md) | 2354–2354 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks / 63.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 63.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01707.md) | 2355–2355 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks / 63.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 63.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 63.4.2.2.1 IssuerCSD &lt;IssrCSD&gt; / 63.4.2.2.1.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01708.md) | 2356–2356 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks / 63.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 63.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 63.4.2.2.2 InvestorCSD &lt;InvstrCSD&gt; / 63.4.2.2.2.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01709.md) | 2357–2357 |
| [63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 63.4 Message Building Blocks / 63.4.3 Update &lt;Upd&gt; / 63.4.3.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01710.md) | 2358–2358 |

## src-000366 — 3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01

[src-000366](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp17–24; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01, Functionality, file p17.**

SCOPE
An instructing party sends a SecurityCSDLinkMaintenanceRequest message to an executing/servicing
party to request the maintenance of the link between a financial instrument and a CSD in their system.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
The request is sent when the instructing party identified a gap in the security CSD Link coverage of the
executing/servicing party. The instructing party needs this security to be maintained at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Outline
The SecurityCSDLinkMaintenanceRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
C. Update
Provides data that needs to be maintained.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 17 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00015.md) | 17–17 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00016.md) | 18–18 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00017.md) | 19–19 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks / 3.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 3.4.2.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00018.md) | 20–20 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks / 3.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 3.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00019.md) | 21–21 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks / 3.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 3.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 3.4.2.2.1 IssuerCSD &lt;IssrCSD&gt; / 3.4.2.2.1.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00020.md) | 22–22 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks / 3.4.2 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 3.4.2.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 3.4.2.2.2 InvestorCSD &lt;InvstrCSD&gt; / 3.4.2.2.2.2 CombinedIdentification &lt;CmbndId&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00021.md) | 23–23 |
| [3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01 / 3.4 Message Building Blocks / 3.4.3 Update &lt;Upd&gt; / 3.4.3.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00022.md) | 24–24 |

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
