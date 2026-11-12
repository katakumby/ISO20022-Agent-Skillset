---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.035.001.01"
message_family: "reda.035"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "55 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "file_pages": [2236, 2240]}, {"source_id": "src-000372", "heading": "8 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "file_pages": [59, 63]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.035.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 55 reda.035.001.01 SecuritiesAccountActivityAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2236–2240; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 55 reda.035.001.01 SecuritiesAccountActivityAdviceV01, Functionality, file p2236.**

The SecuritieAccountActivityReport message is sent by the executing party to an instructing party
containing information about changes on securities account reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities account reference
data.
Outline
The SecuritiesAccountActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecuritiesAccountActivity
Activity report of changes occurred for a specific securities account defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities 2236 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [55 reda.035.001.01 SecuritiesAccountActivityAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01609.md) | 2236–2236 |
| [55 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 55.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01610.md) | 2237–2237 |
| [55 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 55.4 Message Building Blocks / 55.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01611.md) | 2238–2238 |
| [55 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 55.4 Message Building Blocks / 55.4.3 SecuritiesAccountActivity &lt;SctiesAcctActvty&gt; / 55.4.3.2 Change &lt;Chng&gt; / 55.4.3.2.1 SecuritiesAccountIdentification &lt;SctiesAcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01612.md) | 2239–2239 |
| [55 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 55.4 Message Building Blocks / 55.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01613.md) | 2240–2240 |

## src-000372 — 8 reda.035.001.01 SecuritiesAccountActivityAdviceV01

[src-000372](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp59–63; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 8 reda.035.001.01 SecuritiesAccountActivityAdviceV01, Functionality, file p59.**

The SecuritieAccountActivityReport message is sent by the executing party to an instructing party
containing information about changes on securities account reference data.
Scope and usage:
It aims at informing about the changes occurred during a business date for securities account reference
data.
Outline
The SecuritiesAccountActivityAdviceV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. SecuritiesAccountActivity
Activity report of changes occurred for a specific securities account defined in the system.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities - Securities Account Reference Data 59 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 reda.035.001.01 SecuritiesAccountActivityAdviceV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00053.md) | 59–59 |
| [8 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 8.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00054.md) | 60–60 |
| [8 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 8.4 Message Building Blocks / 8.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00055.md) | 61–61 |
| [8 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 8.4 Message Building Blocks / 8.4.3 SecuritiesAccountActivity &lt;SctiesAcctActvty&gt; / 8.4.3.2 Change &lt;Chng&gt; / 8.4.3.2.1 SecuritiesAccountIdentification &lt;SctiesAcctId&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00056.md) | 62–62 |
| [8 reda.035.001.01 SecuritiesAccountActivityAdviceV01 / 8.4 Message Building Blocks / 8.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00057.md) | 63–63 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000371-bank.md) | participant | src-000371 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000371-central-securities-depositories-csd.md) | participant | src-000371 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000371-corporate.md) | participant | src-000371 |
| [CSD](../../../../../shared/reference/participants/participant-src-000371-csd.md) | participant | src-000371 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | participant | src-000371 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | participant | src-000371 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000371-market-data-provider.md) | participant | src-000371 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000371-market-infrastructure.md) | participant | src-000371 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000371-national-central-bank-ncb.md) | participant | src-000371 |
| [Create Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md) | business-flow | src-000371 |
| [Delete Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md) | business-flow | src-000371 |
| [Query](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md) | business-flow | src-000371 |
| [Generate Statement](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md) | business-flow | src-000371 |
| [Creation Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p162-creation-process.md) | business-flow | src-000371 |
| [Modification Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p164-modification-process.md) | business-flow | src-000371 |
| [Deletion Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p166-deletion-process.md) | business-flow | src-000371 |
| [Query/Query Response process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p169-query-query-response-process.md) | business-flow | src-000371 |
| [Statement process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p172-statement-process.md) | business-flow | src-000371 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- SECACCOUNT-FLOWS -->
## Securities account reference flows

- [Receive unsolicited securities account activity](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md)
