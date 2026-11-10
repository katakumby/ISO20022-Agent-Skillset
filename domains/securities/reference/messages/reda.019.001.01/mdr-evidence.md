---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.019.001.01"
message_family: "reda.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.019.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "39 reda.019.001.01 SecuritiesAccountQueryV01", "file_pages": [2106, 2117]}, {"source_id": "src-000372", "heading": "3 reda.019.001.01 SecuritiesAccountQueryV01", "file_pages": [14, 25]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.019.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 39 reda.019.001.01 SecuritiesAccountQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2106–2117; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 39 reda.019.001.01 SecuritiesAccountQueryV01, Functionality, file p2106.**

The SecuritiesAccountQuery message sent by an instructing party to the executing party to request the
details related to the securities account.
Outline
The SecuritiesAccountQueryV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the query message.
B. SearchCriteria
Defines the criteria to be used to query the securities account reference data by the executing
system.
C. ReturnCriteria
Defines the expected securities account reference data to be returned.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2106 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [39 reda.019.001.01 SecuritiesAccountQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01488.md) | 2106–2106 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01489.md) | 2107–2107 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01490.md) | 2108–2108 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01491.md) | 2109–2109 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01492.md) | 2110–2110 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01493.md) | 2111–2111 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.5 OpeningDate &lt;OpngDt&gt; / 39.4.2.5.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01494.md) | 2112–2112 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.6 ClosingDate &lt;ClsgDt&gt; / 39.4.2.6.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01495.md) | 2113–2113 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.7 AccountType &lt;AcctTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01496.md) | 2114–2114 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.2 SearchCriteria &lt;SchCrit&gt; / 39.4.2.8 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01497.md) | 2115–2115 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.3 ReturnCriteria &lt;RtrCrit&gt; / 39.4.3.3 PartyType &lt;PtyTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01498.md) | 2116–2116 |
| [39 reda.019.001.01 SecuritiesAccountQueryV01 / 39.4 Message Building Blocks / 39.4.3 ReturnCriteria &lt;RtrCrit&gt; / 39.4.3.8 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01499.md) | 2117–2117 |

## src-000372 — 3 reda.019.001.01 SecuritiesAccountQueryV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp14–25; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 3 reda.019.001.01 SecuritiesAccountQueryV01, Functionality, file p14.**

The SecuritiesAccountQuery message sent by an instructing party to the executing party to request the
details related to the securities account.
Outline
The SecuritiesAccountQueryV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the query message.
B. SearchCriteria
Defines the criteria to be used to query the securities account reference data by the executing
system.
C. ReturnCriteria
Defines the expected securities account reference data to be returned.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 14 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 reda.019.001.01 SecuritiesAccountQueryV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00012.md) | 14–14 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00013.md) | 15–15 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.3 Constraints](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00014.md) | 16–16 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00015.md) | 17–17 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00016.md) | 18–18 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00017.md) | 19–19 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.5 OpeningDate &lt;OpngDt&gt; / 3.4.2.5.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00018.md) | 20–20 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.6 ClosingDate &lt;ClsgDt&gt; / 3.4.2.6.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00019.md) | 21–21 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.7 AccountType &lt;AcctTp&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00020.md) | 22–22 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.2 SearchCriteria &lt;SchCrit&gt; / 3.4.2.8 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00021.md) | 23–23 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.3 PartyType &lt;PtyTp&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00022.md) | 24–24 |
| [3 reda.019.001.01 SecuritiesAccountQueryV01 / 3.4 Message Building Blocks / 3.4.3 ReturnCriteria &lt;RtrCrit&gt; / 3.4.3.8 EndInvestorFlag &lt;EndInvstrFlg&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00023.md) | 25–25 |

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

- [Query securities account data or audit trail](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
