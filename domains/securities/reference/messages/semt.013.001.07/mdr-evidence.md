---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.013.001.07"
message_family: "semt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.013.001.07"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "4 semt.013.001.07 IntraPositionMovementInstructionV07", "file_pages": [135, 149]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.013.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 4 semt.013.001.07 IntraPositionMovementInstructionV07

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp135–149; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 4 semt.013.001.07 IntraPositionMovementInstructionV07, Functionality, file p135.**

Scope
An account owner sends a IntraPositionMovementInstruction to an account servicer to instruct the
movement of securities within its holding from one sub-balance to another, for example, blocking of
securities.
The account owner/servicer relationship may be:
- a global custodian which has an account with its local agent (sub-custodian), or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information.
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementInstructionV07 MessageDefinition is composed of 12
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. CorporateActionEventIdentification
Identification assigned by the account servicer to unambiguously identify a corporate action event.
C. NumberCounts
Count of the number of transactions linked.
D. Linkages
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 135 March 2026

**src-000197, 4 semt.013.001.07 IntraPositionMovementInstructionV07, Functionality, file p136.**

Link to another transaction that must be processed after, before or at the same time.
E. AccountOwner
Party that legally owns the account.
F. SafekeepingAccount
Account to or from which a securities entry is made.
G. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
H. SafekeepingPlace
Place where the securities are safe-kept, physically or notionally. This place can be, for example, a
local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
I. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
J. FinancialInstrumentAttributes
Elements characterising a financial instrument.
K. IntraPositionDetails
Intra-position movement transaction details.
L. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 136 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00095.md) | 135–136 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00096.md) | 137–139 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00097.md) | 140–140 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.5 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00098.md) | 141–141 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.8 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00099.md) | 142–142 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.10 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00100.md) | 143–145 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.11 IntraPositionDetails &lt;IntraPosDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00101.md) | 146–146 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.11 IntraPositionDetails &lt;IntraPosDtls&gt; / 4.4.11.1 Priority &lt;Prty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00102.md) | 147–147 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.11 IntraPositionDetails &lt;IntraPosDtls&gt; / 4.4.11.3 SecuritiesSubBalanceIdentification &lt;SctiesSubBalId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00103.md) | 148–148 |
| [4 semt.013.001.07 IntraPositionMovementInstructionV07 / 4.4 Message Building Blocks / 4.4.11 IntraPositionDetails &lt;IntraPosDtls&gt; / 4.4.11.6 BalanceTo &lt;BalTo&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00104.md) | 149–149 |

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
