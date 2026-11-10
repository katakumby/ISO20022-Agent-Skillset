---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.047.001.01"
message_family: "reda.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.047.001.01"
source_ids: ["src-000233", "src-000366"]
source_locations: [{"source_id": "src-000233", "heading": "64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "file_pages": [2359, 2368]}, {"source_id": "src-000366", "heading": "4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "file_pages": [25, 34]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2024"]
---

# reda.047.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2359–2368; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01, Functionality, file p2359.**

SCOPE
An executing/servicing party sends a SecurityCSDLinkStatusAdvice message to an instructing party to
report the status of a SecurityCSDLink Request message previously sent by the instructing party.
The SecurityCSDLinkStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCSDLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkStatus
Represents the processing status.
C. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2359 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01711.md) | 2359–2359 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01712.md) | 2360–2360 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01713.md) | 2361–2361 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.1 MessageHeader &lt;MsgHdr&gt; / 64.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01714.md) | 2362–2362 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.2 SecurityCSDLinkStatus &lt;SctyCSDLkSts&gt; / 64.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01715.md) | 2363–2363 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.2 SecurityCSDLinkStatus &lt;SctyCSDLkSts&gt; / 64.4.2.2 StatusReason &lt;StsRsn&gt; / 64.4.2.2.1 Reason &lt;Rsn&gt; / 64.4.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01716.md) | 2364–2364 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 64.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01717.md) | 2365–2365 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 64.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 64.4.3.2.1 IssuerCSD &lt;IssrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01718.md) | 2366–2366 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 64.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 64.4.3.2.2 InvestorCSD &lt;InvstrCSD&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01719.md) | 2367–2367 |
| [64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 64.4 Message Building Blocks / 64.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01720.md) | 2368–2368 |

## src-000366 — 4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01

[src-000366](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; file pp25–34; publication december-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000366, 4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01, Functionality, file p25.**

SCOPE
An executing/servicing party sends a SecurityCSDLinkStatusAdvice message to an instructing party to
report the status of a SecurityCSDLink Request message previously sent by the instructing party.
The SecurityCSDLinkStatusAdvice message may be sent as a response to the request of the
instructing party or not.
The instructing party - executing/servicing party relationship may be:
- Central Securities Depositories (CSD) who would like to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE
Initiator: executing/servicing party.
Outline
The SecurityCSDLinkStatusAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecurityCSDLinkStatus
Represents the processing status.
C. SecurityCSDLinkIdentification
Provides a unique and unambiguous identification for the Security CSD Link.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 25 December 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00023.md) | 25–25 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.2 Structure](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00024.md) | 26–26 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00025.md) | 27–27 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 MessageHeader &lt;MsgHdr&gt; / 4.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00026.md) | 28–28 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 SecurityCSDLinkStatus &lt;SctyCSDLkSts&gt; / 4.4.2.1 Status &lt;Sts&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00027.md) | 29–29 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 SecurityCSDLinkStatus &lt;SctyCSDLkSts&gt; / 4.4.2.2 StatusReason &lt;StsRsn&gt; / 4.4.2.2.1 Reason &lt;Rsn&gt; / 4.4.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00028.md) | 30–30 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 4.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00029.md) | 31–31 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 4.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 4.4.3.2.1 IssuerCSD &lt;IssrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00030.md) | 32–32 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.3 SecurityCSDLinkIdentification &lt;SctyCSDLkId&gt; / 4.4.3.2 IssuerInvestorCSD &lt;IssrInvstrCSD&gt; / 4.4.3.2.2 InvestorCSD &lt;InvstrCSD&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00031.md) | 33–33 |
| [4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-link-reference-data/december-2024/documents/src-000366/sections/section-00032.md) | 34–34 |

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
