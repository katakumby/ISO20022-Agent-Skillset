---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.018.001.01"
message_family: "reda.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.018.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "38 reda.018.001.01 SecuritiesAccountCreationRequestV01", "file_pages": [2098, 2105]}, {"source_id": "src-000372", "heading": "2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "file_pages": [6, 13]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.018.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 38 reda.018.001.01 SecuritiesAccountCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2098–2105; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 38 reda.018.001.01 SecuritiesAccountCreationRequestV01, Functionality, file p2098.**

The SecuritiesAccountCreationRequest message message is sent by an instructing party to the
executing party to instruct the creation of a new securities account with the required account attributes
details.
Usage:
Processing and confirmation of the securities account creation request message are provided via a
SecuritiesAccountStatusAdvice message.
Outline
The SecuritiesAccountCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecuritiesAccount
Securities account to be created in the executing party system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities 2098 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01480.md) | 2098–2098 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01481.md) | 2099–2099 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01482.md) | 2100–2100 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks / 38.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 38.4.2.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01483.md) | 2101–2101 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks / 38.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 38.4.2.3 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01484.md) | 2102–2102 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks / 38.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 38.4.2.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01485.md) | 2103–2103 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks / 38.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 38.4.2.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 38.4.2.8.1 Name &lt;Nm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01486.md) | 2104–2104 |
| [38 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 38.4 Message Building Blocks / 38.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 38.4.2.10 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01487.md) | 2105–2105 |

## src-000372 — 2 reda.018.001.01 SecuritiesAccountCreationRequestV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp6–13; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 2 reda.018.001.01 SecuritiesAccountCreationRequestV01, Functionality, file p6.**

The SecuritiesAccountCreationRequest message message is sent by an instructing party to the
executing party to instruct the creation of a new securities account with the required account attributes
details.
Usage:
Processing and confirmation of the securities account creation request message are provided via a
SecuritiesAccountStatusAdvice message.
Outline
The SecuritiesAccountCreationRequestV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecuritiesAccount
Securities account to be created in the executing party system.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 6 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00004.md) | 6–6 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00005.md) | 7–7 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00006.md) | 8–8 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 2.4.2.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00007.md) | 9–9 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 2.4.2.3 Type &lt;Tp&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00008.md) | 10–10 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 2.4.2.4 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00009.md) | 11–11 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 2.4.2.8 MarketSpecificAttribute &lt;MktSpcfcAttr&gt; / 2.4.2.8.1 Name &lt;Nm&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00010.md) | 12–12 |
| [2 reda.018.001.01 SecuritiesAccountCreationRequestV01 / 2.4 Message Building Blocks / 2.4.2 SecuritiesAccount &lt;SctiesAcct&gt; / 2.4.2.10 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00011.md) | 13–13 |

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

- [Create a securities account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md)
