---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.023.001.01"
message_family: "reda.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "file_pages": [2155, 2162]}, {"source_id": "src-000372", "heading": "6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "file_pages": [48, 55]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.023.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 43 reda.023.001.01 SecuritiesAccountModificationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2155–2162; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 43 reda.023.001.01 SecuritiesAccountModificationRequestV01, Functionality, file p2155.**

The SecuritiesAccountModificationRequest message is sent by an instructing party to the executing
party to instruct the update of an existing securities account by amending its existing attributes or by
providing additional attibutes details.
Usage:
Processing and confirmation of the securities account creation request message are provided via a
SecuritiesAccountStatusAdvice message.
Outline
The SecuritiesAccountModificationRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountIdentification
Identification of the securities account to be updated in the executing party system.
C. Modification
Further details about the requested modification.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2155 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01533.md) | 2155–2155 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01534.md) | 2156–2156 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.4 Message Building Blocks / 43.4.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01535.md) | 2157–2157 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.4 Message Building Blocks / 43.4.3 Modification &lt;Mod&gt; / 43.4.3.1 ScopeIndication &lt;ScpIndctn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01536.md) | 2158–2158 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.4 Message Building Blocks / 43.4.3 Modification &lt;Mod&gt; / 43.4.3.2 RequestedModification &lt;ReqdMod&gt; / 43.4.3.2.1 SystemSecuritiesAccount &lt;SysSctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01537.md) | 2159–2159 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.4 Message Building Blocks / 43.4.3 Modification &lt;Mod&gt; / 43.4.3.2 RequestedModification &lt;ReqdMod&gt; / 43.4.3.2.1 SystemSecuritiesAccount &lt;SysSctiesAcct&gt; / 43.4.3.2.1.3 NegativePosition &lt;NegPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01538.md) | 2160–2160 |
| [43 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 43.4 Message Building Blocks / 43.4.3 Modification &lt;Mod&gt; / 43.4.3.2 RequestedModification &lt;ReqdMod&gt; / 43.4.3.2.2 SystemRestriction &lt;SysRstrctn&gt; / 43.4.3.2.2.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01539.md) | 2161–2162 |

## src-000372 — 6 reda.023.001.01 SecuritiesAccountModificationRequestV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp48–55; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 6 reda.023.001.01 SecuritiesAccountModificationRequestV01, Functionality, file p48.**

The SecuritiesAccountModificationRequest message is sent by an instructing party to the executing
party to instruct the update of an existing securities account by amending its existing attributes or by
providing additional attibutes details.
Usage:
Processing and confirmation of the securities account creation request message are provided via a
SecuritiesAccountStatusAdvice message.
Outline
The SecuritiesAccountModificationRequestV01 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. AccountIdentification
Identification of the securities account to be updated in the executing party system.
C. Modification
Further details about the requested modification.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 48 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00044.md) | 48–48 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00045.md) | 49–49 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.4 Message Building Blocks / 6.4.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00046.md) | 50–50 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.1 ScopeIndication &lt;ScpIndctn&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00047.md) | 51–51 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.1 SystemSecuritiesAccount &lt;SysSctiesAcct&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00048.md) | 52–52 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.1 SystemSecuritiesAccount &lt;SysSctiesAcct&gt; / 6.4.3.2.1.3 NegativePosition &lt;NegPos&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00049.md) | 53–53 |
| [6 reda.023.001.01 SecuritiesAccountModificationRequestV01 / 6.4 Message Building Blocks / 6.4.3 Modification &lt;Mod&gt; / 6.4.3.2 RequestedModification &lt;ReqdMod&gt; / 6.4.3.2.2 SystemRestriction &lt;SysRstrctn&gt; / 6.4.3.2.2.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00050.md) | 54–55 |

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

- [Modify a securities account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p154-modify-a-securities-account.md)
