---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.014.001.09"
message_family: "semt.014"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.014.001.09"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "5 semt.014.001.09 IntraPositionMovementStatusAdviceV09", "file_pages": [150, 161]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.014.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 5 semt.014.001.09 IntraPositionMovementStatusAdviceV09

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp150–161; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 5 semt.014.001.09 IntraPositionMovementStatusAdviceV09, Functionality, file p150.**

Scope
An account servicer sends a IntraPositionMovementStatusAdvice to an account owner to advise the
status of an intra-position movement instruction previously sent by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The IntraPositionMovementStatusAdviceV09 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
B. Linkage
Link to another transaction that triggered the intra-position movement.
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. SettlementStatus
Provides the status of settlement of a transaction.
E. TransactionDetails
Identifies the details of the transaction.
F. SupplementaryData
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 150 March 2026

**src-000197, 5 semt.014.001.09 IntraPositionMovementStatusAdviceV09, Functionality, file p151.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00105.md) | 150–150 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00106.md) | 151–151 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00107.md) | 152–152 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00108.md) | 153–153 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.3.1 Rejected &lt;Rjctd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00109.md) | 154–154 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.3.3 Cancelled &lt;Canc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00110.md) | 155–155 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00111.md) | 156–156 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt; / 5.4.5.1 PoolIdentification &lt;PoolId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00112.md) | 157–157 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt; / 5.4.5.2 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00113.md) | 158–158 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt; / 5.4.5.6 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00114.md) | 159–159 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt; / 5.4.5.7 LotNumber &lt;LotNb&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00115.md) | 160–160 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 5.4 Message Building Blocks / 5.4.5 TransactionDetails &lt;TxDtls&gt; / 5.4.5.10 BalanceFrom &lt;BalFr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00116.md) | 161–161 |

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
