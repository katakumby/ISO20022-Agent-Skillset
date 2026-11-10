---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.022.001.08"
message_family: "sese.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.022.001.08"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "file_pages": [482, 490]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.022.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp482–490; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08, Functionality, file p482.**

Scope
An account servicer sends a SecuritiesStatusOrStatementQueryStatusAdvice to an account owner to
advise the status of a status query or statement query previously sent by the account owner.
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
The SecuritiesStatusOrStatementQueryStatusAdviceV08 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. QueryDetails
Unambiguous identification of the query as per the account owner.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. StatusOrStatementRequested
Details of the request.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 482 March 2026

**src-000197, 16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08, Functionality, file p483.**

F. ProcessingStatus
Provides details on the processing status of the request.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00333.md) | 482–482 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00334.md) | 483–483 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00335.md) | 484–484 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.1 QueryDetails &lt;QryDtls&gt; / 16.4.1.2 Reference &lt;Ref&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00336.md) | 485–485 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.4 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00337.md) | 486–486 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.5 StatusOrStatementRequested &lt;StsOrStmtReqd&gt; / 16.4.5.1 StatusAdvice &lt;StsAdvc&gt; / 16.4.5.1.1 Number &lt;Nb&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00338.md) | 487–487 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.5 StatusOrStatementRequested &lt;StsOrStmtReqd&gt; / 16.4.5.2 Statement &lt;Stmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00339.md) | 488–488 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.6 ProcessingStatus &lt;PrcgSts&gt; / 16.4.6.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00340.md) | 489–489 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 16.4 Message Building Blocks / 16.4.7 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00341.md) | 490–490 |

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
