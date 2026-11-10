---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.020.001.01"
message_family: "reda.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.020.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "40 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "file_pages": [2118, 2123]}, {"source_id": "src-000372", "heading": "4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "file_pages": [26, 31]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.020.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 40 reda.020.001.01 SecuritiesAccountStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2118–2123; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 40 reda.020.001.01 SecuritiesAccountStatusAdviceV01, Functionality, file p2118.**

The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party
to provide the status of the execution of an creation, modification or deletion of securities account
reference data.
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is succesfully performed, the message includes the related securities account
identification.
Outline
The SecuritiesAccountStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecuritiesAccountStatus
Status of the securities account involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2118 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [40 reda.020.001.01 SecuritiesAccountStatusAdviceV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01500.md) | 2118–2118 |
| [40 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 40.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01501.md) | 2119–2119 |
| [40 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 40.4 Message Building Blocks / 40.4.1 MessageHeader &lt;MsgHdr&gt; / 40.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01502.md) | 2120–2120 |
| [40 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 40.4 Message Building Blocks / 40.4.2 SecuritiesAccountStatus &lt;SctiesAcctSts&gt; / 40.4.2.1 RelatedSecuritiesAccount &lt;RltdSctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01503.md) | 2121–2121 |
| [40 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 40.4 Message Building Blocks / 40.4.2 SecuritiesAccountStatus &lt;SctiesAcctSts&gt; / 40.4.2.3 StatusReason &lt;StsRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01504.md) | 2122–2123 |

## src-000372 — 4 reda.020.001.01 SecuritiesAccountStatusAdviceV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp26–31; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 4 reda.020.001.01 SecuritiesAccountStatusAdviceV01, Functionality, file p26.**

The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party
to provide the status of the execution of an creation, modification or deletion of securities account
reference data.
Usage:
When processing information is negative - a failure occurred in applying the changes the message
accordingly also delivers information about the reason why the creation or update could not be
processed.
When the processing is succesfully performed, the message includes the related securities account
identification.
Outline
The SecuritiesAccountStatusAdviceV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. SecuritiesAccountStatus
Status of the securities account involved in the originating message.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 26 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 reda.020.001.01 SecuritiesAccountStatusAdviceV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00024.md) | 26–26 |
| [4 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 4.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00025.md) | 27–27 |
| [4 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.1 MessageHeader &lt;MsgHdr&gt; / 4.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00026.md) | 28–28 |
| [4 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 SecuritiesAccountStatus &lt;SctiesAcctSts&gt; / 4.4.2.1 RelatedSecuritiesAccount &lt;RltdSctiesAcct&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00027.md) | 29–29 |
| [4 reda.020.001.01 SecuritiesAccountStatusAdviceV01 / 4.4 Message Building Blocks / 4.4.2 SecuritiesAccountStatus &lt;SctiesAcctSts&gt; / 4.4.2.3 StatusReason &lt;StsRsn&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00028.md) | 30–31 |

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
- [Modify a securities account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p154-modify-a-securities-account.md)
- [Delete a securities account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md)
