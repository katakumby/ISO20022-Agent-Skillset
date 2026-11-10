---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "shared"
message_id: "head.002.001.01"
message_family: "head.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"
source_ids: ["src-000233", "src-000349"]
source_locations: [{"source_id": "src-000233", "heading": "26 head.002.001.01 BusinessFileHeaderV01", "file_pages": [614, 618]}, {"source_id": "src-000349", "heading": "2 head.002.001.01 BusinessFileHeaderV01", "file_pages": [4, 8]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "june-2024"]
---

# head.002.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 26 head.002.001.01 BusinessFileHeaderV01

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp614–618; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 26 head.002.001.01 BusinessFileHeaderV01, Functionality, file p614.**

The Business File Header contains information about the parties involved in the file exchange, as well
as information about the content and its structure.
The Business File headers has four major functions:
- Provides information about the sender of the file.
- Identifies the file exchanged: each file must have a unique File Identifier.
- Describes the type of message(s) exchanged: by default, the type of messages contained in a file will
be ISO 20022 message definitions.
- Provides processing information to the receiving party: that would be, for instance, the total number of
messages included in the file.
Usage: The Business File Header (head.002) is to be used exclusively in existing implementations,
such as the Eurosystem, and will be replaced for general use by the upcoming next version defined as
the Business File Envelope (nvlp.002). The Business File Header (head.002) will therefore not be
maintained in the future and any new implementation must use the Business File Envelope (nvlp.002).
Outline
The BusinessFileHeaderV01 MessageDefinition is composed of 2 MessageBuildingBlocks:
A. PayloadDescription
Contains information about the payload.
B. Payload
File Payload is used to include the exchanged documents within the file structure.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 614 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [26 head.002.001.01 BusinessFileHeaderV01](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00488.md) | 614–614 |
| [26 head.002.001.01 BusinessFileHeaderV01 / 26.2 Structure](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00489.md) | 615–615 |
| [26 head.002.001.01 BusinessFileHeaderV01 / 26.4 Message Building Blocks / 26.4.1 PayloadDescription &lt;PyldDesc&gt; / 26.4.1.1 PayloadData &lt;PyldData&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00490.md) | 616–616 |
| [26 head.002.001.01 BusinessFileHeaderV01 / 26.4 Message Building Blocks / 26.4.1 PayloadDescription &lt;PyldDesc&gt; / 26.4.1.2 ApplicationSpecifics &lt;ApplSpcfcs&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00491.md) | 617–617 |
| [26 head.002.001.01 BusinessFileHeaderV01 / 26.4 Message Building Blocks / 26.4.1 PayloadDescription &lt;PyldDesc&gt; / 26.4.1.3 PayloadType &lt;PyldTp&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00492.md) | 618–618 |

## src-000349 — 2 head.002.001.01 BusinessFileHeaderV01

[src-000349](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`; file pp4–8; publication june-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000349, 2 head.002.001.01 BusinessFileHeaderV01, Functionality, file p4.**

The Business File Header contains information about the parties involved in the file exchange, as well
as information about the content and its structure.
The Business File headers has four major functions:
- Provides information about the sender of the file.
- Identifies the file exchanged: each file must have a unique File Identifier.
- Describes the type of message(s) exchanged: by default, the type of messages contained in a file will
be ISO 20022 message definitions.
- Provides processing information to the receiving party: that would be, for instance, the total number of
messages included in the file.
Usage: The Business File Header (head.002) is to be used exclusively in existing implementations,
such as the Eurosystem, and will be replaced for general use by the upcoming next version defined as
the Business File Envelope (nvlp.002). The Business File Header (head.002) will therefore not be
maintained in the future and any new implementation must use the Business File Envelope (nvlp.002).
Outline
The BusinessFileHeaderV01 MessageDefinition is composed of 2 MessageBuildingBlocks:
A. PayloadDescription
Contains information about the payload.
B. Payload
File Payload is used to include the exchanged documents within the file structure.
Approved by the Cross SEG Harmonisation Group (CSH) on the 18th of June
2024.
head.002.001.01 BusinessFileHeaderV01
Target2-Securities - Business File Header 4 June 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 head.002.001.01 BusinessFileHeaderV01](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/sections/section-00004.md) | 4–4 |
| [2 head.002.001.01 BusinessFileHeaderV01 / 2.2 Structure](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/sections/section-00005.md) | 5–5 |
| [2 head.002.001.01 BusinessFileHeaderV01 / 2.4 Message Building Blocks / 2.4.1 PayloadDescription &lt;PyldDesc&gt; / 2.4.1.1 PayloadData &lt;PyldData&gt;](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/sections/section-00006.md) | 6–6 |
| [2 head.002.001.01 BusinessFileHeaderV01 / 2.4 Message Building Blocks / 2.4.1 PayloadDescription &lt;PyldDesc&gt; / 2.4.1.2 ApplicationSpecifics &lt;ApplSpcfcs&gt;](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/sections/section-00007.md) | 7–7 |
| [2 head.002.001.01 BusinessFileHeaderV01 / 2.4 Message Building Blocks / 2.4.1 PayloadDescription &lt;PyldDesc&gt; / 2.4.1.3 PayloadType &lt;PyldTp&gt;](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/sections/section-00008.md) | 8–8 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [bfh-authorised-signatory](../../participants/bfh-authorised-signatory.md) | participant | src-000349 |
| [bfh-file-receiver](../../participants/bfh-file-receiver.md) | participant | src-000349 |
| [bfh-file-sender](../../participants/bfh-file-sender.md) | participant | src-000349 |
| [bfh-service-provider](../../participants/bfh-service-provider.md) | participant | src-000349 |
| [bfh-system-administrator](../../participants/bfh-system-administrator.md) | participant | src-000349 |
| [bfh-system-user](../../participants/bfh-system-user.md) | participant | src-000349 |
| [bfh-file-exchange](../../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) | business-flow | src-000349 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../tracking/issues.md)
