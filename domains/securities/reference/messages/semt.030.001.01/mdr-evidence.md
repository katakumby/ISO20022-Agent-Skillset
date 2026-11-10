---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.030.001.01"
message_family: "semt.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.030.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "file_pages": [2642, 2651]}, {"source_id": "src-000381", "heading": "4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "file_pages": [87, 96]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.030.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2642–2651; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01, Functionality, file p2642.**

The SecuritiesSettlementConditionsModificationRequestQuery message is sent from an account owner/
requestor to a settlement infrastructure to query for the status of settlement or intra-position movement
modification instruction(s) based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The SecuritiesSettlementConditionsModificationRequestQueryV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement modification query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2642 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01930.md) | 2642–2642 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01931.md) | 2643–2643 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01932.md) | 2644–2644 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01933.md) | 2645–2645 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01934.md) | 2646–2646 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.2 SearchCriteria &lt;SchCrit&gt; / 75.4.1.2.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01935.md) | 2647–2647 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.2 SearchCriteria &lt;SchCrit&gt; / 75.4.1.2.6 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01936.md) | 2648–2648 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.2 SearchCriteria &lt;SchCrit&gt; / 75.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 75.4.1.2.7.1 Date &lt;Dt&gt; / 75.4.1.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01937.md) | 2649–2649 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.1 QueryDefinition &lt;QryDef&gt; / 75.4.1.2 SearchCriteria &lt;SchCrit&gt; / 75.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 75.4.1.2.7.2 DateTime &lt;DtTm&gt; / 75.4.1.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01938.md) | 2650–2650 |
| [75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 75.4 Message Building Blocks / 75.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01939.md) | 2651–2651 |

## src-000381 — 4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01

[src-000381](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp87–96; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01, Functionality, file p87.**

The SecuritiesSettlementConditionsModificationRequestQuery message is sent from an account owner/
requestor to a settlement infrastructure to query for the status of settlement or intra-position movement
modification instruction(s) based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The SecuritiesSettlementConditionsModificationRequestQueryV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement modification query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 August 2025 semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities - Settlement Restrictions 87 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00066.md) | 87–87 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00067.md) | 88–88 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00068.md) | 89–89 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00069.md) | 90–90 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00070.md) | 91–91 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.2 SearchCriteria &lt;SchCrit&gt; / 4.4.1.2.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00071.md) | 92–92 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.2 SearchCriteria &lt;SchCrit&gt; / 4.4.1.2.6 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00072.md) | 93–93 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.2 SearchCriteria &lt;SchCrit&gt; / 4.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 4.4.1.2.7.1 Date &lt;Dt&gt; / 4.4.1.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00073.md) | 94–94 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.1 QueryDefinition &lt;QryDef&gt; / 4.4.1.2 SearchCriteria &lt;SchCrit&gt; / 4.4.1.2.7 CreationDateTime &lt;CreDtTm&gt; / 4.4.1.2.7.2 DateTime &lt;DtTm&gt; / 4.4.1.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00074.md) | 95–95 |
| [4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01 / 4.4 Message Building Blocks / 4.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00075.md) | 96–96 |

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
