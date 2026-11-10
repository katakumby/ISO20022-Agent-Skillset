---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.020.001.07"
message_family: "semt.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "file_pages": [406, 411]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.020.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp406–411; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07, Functionality, file p406.**

Scope
An account servicer sends a SecuritiesMessageCancellationAdvice to an account owner to inform of
the cancellation of a securities message previously sent by an account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The previously sent message may be:
- a securities settlement transaction confirmation
- a report (transactions, pending transactions, allegements, accounting and custody securities balance)
- a allegement notification (when sent by mistake or because the counterparty cancelled its instruction)
- a portfolio transfer notification
- an intra-position movement confirmation
- a transaction generation notification
The previously sent message cannot be a status advice message (any). If a status advice should not
have been sent, a new status advice with the correct status should be sent, not a cancellation advice.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
Approved by the Securities SEG on 27 January 2026 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
Settlement And Reconciliation - Maintenance 2025 - 2026 406 March 2026

**src-000197, 11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07, Functionality, file p407.**

The SecuritiesMessageCancellationAdviceV07 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Reference
Reference to the message advised to be cancelled by the account servicer.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00272.md) | 406–406 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 11.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00273.md) | 407–407 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 11.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00274.md) | 408–409 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 11.4 Message Building Blocks / 11.4.2 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00275.md) | 410–411 |

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
