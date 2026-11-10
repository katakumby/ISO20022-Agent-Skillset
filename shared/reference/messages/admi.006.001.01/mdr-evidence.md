---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "shared"
message_id: "admi.006.001.01"
message_family: "admi.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01"
source_ids: ["src-000233", "src-000344"]
source_locations: [{"source_id": "src-000233", "heading": "3 admi.006.001.01 ResendRequestV01", "file_pages": [57, 61]}, {"source_id": "src-000344", "heading": "3 admi.006.001.01 ResendRequestV01", "file_pages": [27, 31]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# admi.006.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 3 admi.006.001.01 ResendRequestV01

[src-000233](../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp57–61; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 3 admi.006.001.01 ResendRequestV01, Functionality, file p57.**

A system member or any parties authorised by them send a ResendRequest message to the Central
System (such as the T2S platform). The purpose of this request is, that the requesting party wants to
receive the "original" message once again. This might be caused through technical problems on the
receiving side (message could not be received or processed or is missing in the message sequencing)
or for archiving purposes.
Outline
The ResendRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the resend message.
B. ResendSearchCriteria
Defines the criteria to unambiguously identify the information to be resent.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 admi.006.001.01 ResendRequestV01](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00025.md) | 57–57 |
| [3 admi.006.001.01 ResendRequestV01 / 3.3 Constraints](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00026.md) | 58–58 |
| [3 admi.006.001.01 ResendRequestV01 / 3.4 Message Building Blocks / 3.4.2 ResendSearchCriteria &lt;RsndSchCrit&gt; / 3.4.2.1 BusinessDate &lt;BizDt&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00027.md) | 59–59 |
| [3 admi.006.001.01 ResendRequestV01 / 3.4 Message Building Blocks / 3.4.2 ResendSearchCriteria &lt;RsndSchCrit&gt; / 3.4.2.4 OriginalMessageNameIdentification &lt;OrgnlMsgNmId&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00028.md) | 60–61 |

## src-000344 — 3 admi.006.001.01 ResendRequestV01

[src-000344](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; file pp27–31; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000344, 3 admi.006.001.01 ResendRequestV01, Functionality, file p27.**

A system member or any parties authorised by them send a ResendRequest message to the Central
System (such as the T2S platform). The purpose of this request is, that the requesting party wants to
receive the "original" message once again. This might be caused through technical problems on the
receiving side (message could not be received or processed or is missing in the message sequencing)
or for archiving purposes.
Outline
The ResendRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the resend message.
B. ResendSearchCriteria
Defines the criteria to unambiguously identify the information to be resent.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-administration/march-2024/documents/src-000344/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 admi.006.001.01 ResendRequestV01](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00022.md) | 27–27 |
| [3 admi.006.001.01 ResendRequestV01 / 3.3 Constraints](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00023.md) | 28–28 |
| [3 admi.006.001.01 ResendRequestV01 / 3.4 Message Building Blocks / 3.4.2 ResendSearchCriteria &lt;RsndSchCrit&gt; / 3.4.2.1 BusinessDate &lt;BizDt&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00024.md) | 29–29 |
| [3 admi.006.001.01 ResendRequestV01 / 3.4 Message Building Blocks / 3.4.2 ResendSearchCriteria &lt;RsndSchCrit&gt; / 3.4.2.4 OriginalMessageNameIdentification &lt;OrgnlMsgNmId&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00025.md) | 30–31 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Securities Depositories (CSD)](../../participants/participant-src-000343-central-securities-depositories-csd.md) | participant | src-000343 |
| [Executing/Servicing Party](../../participants/participant-src-000343-executing-servicing-party.md) | participant | src-000343 |
| [Instructing Party](../../participants/participant-src-000343-instructing-party.md) | participant | src-000343 |
| [National Central Bank (NCB)](../../participants/participant-src-000343-national-central-bank-ncb.md) | participant | src-000343 |
| [National Central Bank](../../participants/participant-src-000343-national-central-bank.md) | participant | src-000343 |
| [Payment Bank](../../participants/participant-src-000343-payment-bank.md) | participant | src-000343 |
| [Settlement Infrastructure Direct Participant](../../participants/participant-src-000343-settlement-infrastructure-direct-participant.md) | participant | src-000343 |
| [Settlement Infrastructure](../../participants/participant-src-000343-settlement-infrastructure.md) | participant | src-000343 |
| [System Member](../../participants/participant-src-000343-system-member.md) | participant | src-000343 |
| [System Transaction Administrator](../../participants/participant-src-000343-system-transaction-administrator.md) | participant | src-000343 |
| [T2S operator](../../participants/participant-src-000343-t2s-operator.md) | participant | src-000343 |
| [t2s-administration-clearing-member-role](../../participants/t2s-administration-clearing-member-role.md) | participant | src-000345 |
| [t2s-administration-identification-issuer-role](../../participants/t2s-administration-identification-issuer-role.md) | participant | src-000345 |
| [t2s-administration-information-party-role](../../participants/t2s-administration-information-party-role.md) | participant | src-000345 |
| [t2s-administration-system-party-role](../../participants/t2s-administration-system-party-role.md) | participant | src-000345 |
| [Report query process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p126-report-query-process.md) | business-flow | src-000343 |
| [Resent Request Process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p136-resent-request-process.md) | business-flow | src-000343 |
| [Receipt Acknowledgement Process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p143-receipt-acknowledgement-process.md) | business-flow | src-000343 |
| [Report Query Request (admi.005)](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md) | business-flow | src-000343 |
| [Resend Request (admi.006)](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md) | business-flow | src-000343 |
| [Scenario 1a](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p162-scenario-1a.md) | business-flow | src-000343 |
| [Scenario 1b](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p168-scenario-1b.md) | business-flow | src-000343 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../tracking/issues.md)


<!-- ADMIN-FLOWS -->
## Administration business flows

- [Resend request activity](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md)
- [Resend an existing message or file](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p179-resend-request-business-transaction-admi-006.md)
