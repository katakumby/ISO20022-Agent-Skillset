---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.034.001.01"
message_family: "semt.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.034.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "79 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [2724, 2747]}, {"source_id": "src-000381", "heading": "8 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [169, 192]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.034.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 79 semt.034.001.01 IntraPositionMovementPendingReportV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2724–2747; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 79 semt.034.001.01 IntraPositionMovementPendingReportV01, Functionality, file p2724.**

This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an
account owner/request to report the intra-position movement instructions, previously sent by the
account owner, that have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementPendingReportV01 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. AccountOwner
Party that owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. Movements
Identifies the transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2724 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02001.md) | 2724–2724 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02002.md) | 2725–2725 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02003.md) | 2726–2727 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02004.md) | 2728–2728 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.1 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02005.md) | 2729–2729 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 79.4.2.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02006.md) | 2730–2730 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 79.4.2.7 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02007.md) | 2731–2731 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02008.md) | 2732–2733 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02009.md) | 2734–2735 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02010.md) | 2736–2736 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.5 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02011.md) | 2737–2738 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.11 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02012.md) | 2739–2740 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.12 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02013.md) | 2741–2741 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.14 StatusDate &lt;StsDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02014.md) | 2742–2742 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.16 Linkages &lt;Lnkgs&gt; / 79.4.5.2.16.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02015.md) | 2743–2743 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.16 Linkages &lt;Lnkgs&gt; / 79.4.5.2.16.3 Reference &lt;Ref&gt; / 79.4.5.2.16.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02016.md) | 2744–2744 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.16 Linkages &lt;Lnkgs&gt; / 79.4.5.2.16.3 Reference &lt;Ref&gt; / 79.4.5.2.16.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02017.md) | 2745–2745 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.19 CorporateActionEventType &lt;CorpActnEvtTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02018.md) | 2746–2746 |
| [79 semt.034.001.01 IntraPositionMovementPendingReportV01 / 79.4 Message Building Blocks / 79.4.5 Movements &lt;Mvmnts&gt; / 79.4.5.2 Movement &lt;Mvmnt&gt; / 79.4.5.2.23 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02019.md) | 2747–2747 |

## src-000381 — 8 semt.034.001.01 IntraPositionMovementPendingReportV01

[src-000381](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp169–192; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 8 semt.034.001.01 IntraPositionMovementPendingReportV01, Functionality, file p169.**

This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an
account owner/request to report the intra-position movement instructions, previously sent by the
account owner, that have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementPendingReportV01 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. AccountOwner
Party that owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. Movements
Identifies the transactions.
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 169 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00137.md) | 169–169 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00138.md) | 170–170 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00139.md) | 171–172 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00140.md) | 173–173 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.1 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00141.md) | 174–174 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 8.4.2.2 QueryReference &lt;QryRef&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00142.md) | 175–175 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 8.4.2.7 UpdateType &lt;UpdTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00143.md) | 176–176 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00144.md) | 177–178 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00145.md) | 179–180 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00146.md) | 181–181 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.5 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00147.md) | 182–183 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.11 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00148.md) | 184–185 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.12 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00149.md) | 186–186 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.14 StatusDate &lt;StsDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00150.md) | 187–187 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.16 Linkages &lt;Lnkgs&gt; / 8.4.5.2.16.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00151.md) | 188–188 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.16 Linkages &lt;Lnkgs&gt; / 8.4.5.2.16.3 Reference &lt;Ref&gt; / 8.4.5.2.16.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00152.md) | 189–189 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.16 Linkages &lt;Lnkgs&gt; / 8.4.5.2.16.3 Reference &lt;Ref&gt; / 8.4.5.2.16.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00153.md) | 190–190 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.19 CorporateActionEventType &lt;CorpActnEvtTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00154.md) | 191–191 |
| [8 semt.034.001.01 IntraPositionMovementPendingReportV01 / 8.4 Message Building Blocks / 8.4.5 Movements &lt;Mvmnts&gt; / 8.4.5.2 Movement &lt;Mvmnt&gt; / 8.4.5.2.23 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00155.md) | 192–192 |

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
