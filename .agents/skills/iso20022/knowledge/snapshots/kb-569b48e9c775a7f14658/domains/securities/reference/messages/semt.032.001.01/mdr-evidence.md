---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.032.001.01"
message_family: "semt.032"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.032.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "file_pages": [2689, 2699]}, {"source_id": "src-000381", "heading": "6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "file_pages": [134, 144]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.032.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2689–2699; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01, Functionality, file p2689.**

The SecuritiesTransactionCancellationRequestQuery message is sent from an account owner/
requestor to a settlement infrastructure to query for the status of settlement or intra-position movement
cancellation instruction(s) based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The SecuritiesTransactionCancellationRequestQueryV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement cancellation query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2689 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01969.md) | 2689–2689 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01970.md) | 2690–2690 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01971.md) | 2691–2691 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01972.md) | 2692–2692 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01973.md) | 2693–2693 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt; / 77.4.1.2.2 InstructionQueryType &lt;InstrQryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01974.md) | 2694–2694 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt; / 77.4.1.2.3 ProcessingStatus &lt;PrcgSts&gt; / 77.4.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01975.md) | 2695–2695 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt; / 77.4.1.2.7 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01976.md) | 2696–2696 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt; / 77.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 77.4.1.2.7.1 Date &lt;Dt&gt; / 77.4.1.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01977.md) | 2697–2697 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.1 QueryDefinition &lt;QryDef&gt; / 77.4.1.2 SearchCriteria &lt;SchCrit&gt; / 77.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 77.4.1.2.7.2 DateTime &lt;DtTm&gt; / 77.4.1.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01978.md) | 2698–2698 |
| [77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 77.4 Message Building Blocks / 77.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01979.md) | 2699–2699 |

## src-000381 — 6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01

[src-000381](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp134–144; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01, Functionality, file p134.**

The SecuritiesTransactionCancellationRequestQuery message is sent from an account owner/
requestor to a settlement infrastructure to query for the status of settlement or intra-position movement
cancellation instruction(s) based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The SecuritiesTransactionCancellationRequestQueryV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement cancellation query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 134 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00105.md) | 134–134 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00106.md) | 135–135 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00107.md) | 136–136 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00108.md) | 137–137 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00109.md) | 138–138 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt; / 6.4.1.2.2 InstructionQueryType &lt;InstrQryTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00110.md) | 139–139 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt; / 6.4.1.2.3 ProcessingStatus &lt;PrcgSts&gt; / 6.4.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00111.md) | 140–140 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt; / 6.4.1.2.7 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00112.md) | 141–141 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt; / 6.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 6.4.1.2.7.1 Date &lt;Dt&gt; / 6.4.1.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00113.md) | 142–142 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.1 QueryDefinition &lt;QryDef&gt; / 6.4.1.2 SearchCriteria &lt;SchCrit&gt; / 6.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 6.4.1.2.7.2 DateTime &lt;DtTm&gt; / 6.4.1.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00114.md) | 143–143 |
| [6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01 / 6.4 Message Building Blocks / 6.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00115.md) | 144–144 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000380-central-counterparty.md) | participant | src-000380 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md) | participant | src-000380 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md) | participant | src-000380 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | participant | src-000380 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | participant | src-000380 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md) | participant | src-000380 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000380-t2s-operator.md) | participant | src-000380 |
| [Query Report Process](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p253-query-report-process.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) | business-flow | src-000380 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
