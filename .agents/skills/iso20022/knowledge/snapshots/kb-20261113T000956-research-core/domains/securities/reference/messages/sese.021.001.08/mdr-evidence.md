---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.021.001.08"
message_family: "sese.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.021.001.08"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "15 sese.021.001.08 SecuritiesTransactionStatusQueryV08", "file_pages": [476, 481]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.021.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 15 sese.021.001.08 SecuritiesTransactionStatusQueryV08

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp476–481; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 15 sese.021.001.08 SecuritiesTransactionStatusQueryV08, Functionality, file p476.**

Scope
An account owner sends a SecuritiesTransactionStatusQuery to an account servicer to request a status
on a securities transaction.
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
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesTransactionStatusQueryV08 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. StatusAdviceRequested
Description of the status advice requested.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.021.001.08
SecuritiesTransactionStatusQueryV08
Settlement And Reconciliation - Maintenance 2025 - 2026 476 March 2026

**src-000197, 15 sese.021.001.08 SecuritiesTransactionStatusQueryV08, Functionality, file p477.**

Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 sese.021.001.08 SecuritiesTransactionStatusQueryV08](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00328.md) | 476–476 |
| [15 sese.021.001.08 SecuritiesTransactionStatusQueryV08 / 15.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00329.md) | 477–477 |
| [15 sese.021.001.08 SecuritiesTransactionStatusQueryV08 / 15.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00330.md) | 478–478 |
| [15 sese.021.001.08 SecuritiesTransactionStatusQueryV08 / 15.4 Message Building Blocks / 15.4.1 StatusAdviceRequested &lt;StsAdvcReqd&gt; / 15.4.1.2 References &lt;Refs&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00331.md) | 479–479 |
| [15 sese.021.001.08 SecuritiesTransactionStatusQueryV08 / 15.4 Message Building Blocks / 15.4.2 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00332.md) | 480–481 |

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
