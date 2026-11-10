---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.021.001.09"
message_family: "semt.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.021.001.09"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "12 semt.021.001.09 SecuritiesStatementQueryV09", "file_pages": [412, 432]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.021.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 12 semt.021.001.09 SecuritiesStatementQueryV09

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp412–432; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 12 semt.021.001.09 SecuritiesStatementQueryV09, Functionality, file p412.**

Scope
An account owner sends a SecuritiesStatementQuery to an account servicer to request any existing
securities statement.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct to a
central securities depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesStatementQueryV09 MessageDefinition is composed of 7 MessageBuildingBlocks:
A. StatementRequested
Description of the statement requested.
B. StatementGeneralDetails
General information related to the report.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 412 March 2026

**src-000197, 12 semt.021.001.09 SecuritiesStatementQueryV09, Functionality, file p413.**

Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. AdditionalQueryParameters
Additional specific query criteria.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 413 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00276.md) | 412–413 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00277.md) | 414–414 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00278.md) | 415–415 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00279.md) | 416–417 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.5 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00280.md) | 418–418 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.1 Status &lt;Sts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00281.md) | 419–420 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00282.md) | 421–421 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.1 RepoCallAcknowledgementReason &lt;RepoCallAckRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00283.md) | 422–422 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.5 DeniedReason &lt;DndRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00284.md) | 423–426 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.7 PendingReason &lt;PdgRsn&gt; / 12.4.6.2.7.2 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00285.md) | 427–427 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.9 PendingProcessingReason &lt;PdgPrcgRsn&gt; / 12.4.6.2.9.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00286.md) | 428–428 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.9 PendingProcessingReason &lt;PdgPrcgRsn&gt; / 12.4.6.2.9.2 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00287.md) | 429–429 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 12.4 Message Building Blocks / 12.4.6 AdditionalQueryParameters &lt;AddtlQryParams&gt; / 12.4.6.2 Reason &lt;Rsn&gt; / 12.4.6.2.12 PendingModificationReason &lt;PdgModRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00288.md) | 430–432 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) | participant | src-000196, src-000197, src-000198 |
| [Account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) | participant | src-000196, src-000197, src-000198 |
| [Buy Side Party](../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) | participant | src-000196 |
| [Central Counterparty](../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) | participant | src-000196 |
| [Confirmation Party](../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) | participant | src-000196 |
| [CSD / ICSD](../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) | participant | src-000196 |
| [Executing/servicing party](../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) | participant | src-000196 |
| [Global Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) | participant | src-000196 |
| [Instructing party](../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) | participant | src-000196 |
| [Local Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) | participant | src-000196 |
| [Portfolio transfer client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) | participant | src-000196 |
| [Third party in securities reporting](../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) | participant | src-000196 |
| [Sell Side Party](../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) | participant | src-000196 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) | participant | src-000196 |
| [Stock Exchange](../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) | participant | src-000196 |
| [Cancellation advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md) | business-flow | src-000196 |
| [Cancellation request](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md) | business-flow | src-000196 |
| [Instruction and confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md) | business-flow | src-000196 |
| [Partial settlement confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md) | business-flow | src-000196 |
| [Portfolio transfer](../../message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md) | business-flow | src-000196 |
| [Reconciliation and reporting: pull mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md) | business-flow | src-000196 |
| [Reconciliation and reporting: push mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md) | business-flow | src-000196 |
| [Settlement reversal advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md) | business-flow | src-000196 |
| [Transaction generation notification](../../message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md) | business-flow | src-000196 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
