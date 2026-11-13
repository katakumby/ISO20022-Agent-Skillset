---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "shared"
message_id: "admi.007.001.01"
message_family: "admi.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.007.001.01"
source_ids: ["src-000233", "src-000344"]
source_locations: [{"source_id": "src-000233", "heading": "4 admi.007.001.01 ReceiptAcknowledgementV01", "file_pages": [62, 67]}, {"source_id": "src-000344", "heading": "4 admi.007.001.01 ReceiptAcknowledgementV01", "file_pages": [32, 37]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# admi.007.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 4 admi.007.001.01 ReceiptAcknowledgementV01

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp62–67; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 4 admi.007.001.01 ReceiptAcknowledgementV01, Functionality, file p62.**

The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the
system and vice versa. It is sent to acknowledge the receipt of one or multiple messages sent
previously. The Acknowledgement message is 1) an application receipt acknowledgement and 2)
conveys information about the processing of the original message(s). In case of 2) the
ReceiptAcknowledgement can be used as a Generic error message, which provides information about
the status (e.g. rejection, acceptance) of an instruction.
Outline
The ReceiptAcknowledgementV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageIdentification
Specifies the identification the message.
B. Report
Provides report details on the request.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 62 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 admi.007.001.01 ReceiptAcknowledgementV01](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00029.md) | 62–62 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.2 Structure](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00030.md) | 63–63 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.1 MessageIdentification &lt;MsgId&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00031.md) | 64–64 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.2 Report &lt;Rpt&gt; / 4.4.2.1 RelatedReference &lt;RltdRef&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00032.md) | 65–65 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.2 Report &lt;Rpt&gt; / 4.4.2.2 RequestHandling &lt;ReqHdlg&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00033.md) | 66–67 |

## src-000344 — 4 admi.007.001.01 ReceiptAcknowledgementV01

[src-000344](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; file pp32–37; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000344, 4 admi.007.001.01 ReceiptAcknowledgementV01, Functionality, file p32.**

The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the
system and vice versa. It is sent to acknowledge the receipt of one or multiple messages sent
previously. The Acknowledgement message is 1) an application receipt acknowledgement and 2)
conveys information about the processing of the original message(s). In case of 2) the
ReceiptAcknowledgement can be used as a Generic error message, which provides information about
the status (e.g. rejection, acceptance) of an instruction.
Outline
The ReceiptAcknowledgementV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageIdentification
Specifies the identification the message.
B. Report
Provides report details on the request.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities - Administration - Maintenance 2023 -
2024
32 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-administration/march-2024/documents/src-000344/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 admi.007.001.01 ReceiptAcknowledgementV01](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00026.md) | 32–32 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.2 Structure](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00027.md) | 33–33 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00028.md) | 34–34 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.2 Report &lt;Rpt&gt; / 4.4.2.1 RelatedReference &lt;RltdRef&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00029.md) | 35–35 |
| [4 admi.007.001.01 ReceiptAcknowledgementV01 / 4.4 Message Building Blocks / 4.4.2 Report &lt;Rpt&gt; / 4.4.2.2 RequestHandling &lt;ReqHdlg&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00030.md) | 36–37 |

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

- [Report query request activity](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md)
- [Resend request activity](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md)
- [Receipt acknowledgement — receipt status](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p162-scenario-1a.md)
- [Receipt acknowledgement — business-processing rejection](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p168-scenario-1b.md)
- [Query the latest available report](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p175-report-query-request-business-transaction-admi-005.md)
- [Resend an existing message or file](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p179-resend-request-business-transaction-admi-006.md)
- [Central-system receipt acknowledgement](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p189-scenario-1-receipt-acknowledgement-sent-by-central-system-e-g-t2s-plat.md)
