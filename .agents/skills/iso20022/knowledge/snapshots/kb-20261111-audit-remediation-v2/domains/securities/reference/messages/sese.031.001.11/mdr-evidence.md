---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.031.001.11"
message_family: "sese.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.031.001.11"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "file_pages": [802, 814]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.031.001.11 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp802–814; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11, Functionality, file p802.**

Scope
An account servicer sends a SecuritiesSettlementConditionsModificationStatusAdvice to an account
owner to advise the status of a modification request previously instructed by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
A SecuritiesSettlementConditionsModificationRequest may contain requests on multiple transactions.
However, one SecuritiesSettlementConditionsModificationStatusAdvice must be sent per transaction
modified unless the SecuritiesSettlementConditionsModificationRequest is rejected as a whole.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementConditionModificationStatusAdviceV11 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. RequestReference
Identification of the SecuritiesSettlementConditionsModificationRequest.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 802 March 2026

**src-000197, 25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11, Functionality, file p803.**

Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. RequestDetails
Details of the request.
F. ProcessingStatus
Provides details on the processing status of the request.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 803 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00533.md) | 802–803 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00534.md) | 804–804 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00535.md) | 805–805 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00536.md) | 806–806 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.5 RequestDetails &lt;ReqDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00537.md) | 807–807 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.5 RequestDetails &lt;ReqDtls&gt; / 25.4.5.1 Reference &lt;Ref&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00538.md) | 808–808 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.5 RequestDetails &lt;ReqDtls&gt; / 25.4.5.3 AutomaticBorrowing &lt;AutomtcBrrwg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00539.md) | 809–809 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.5 RequestDetails &lt;ReqDtls&gt; / 25.4.5.7 OtherProcessing &lt;OthrPrcg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00540.md) | 810–810 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.5 RequestDetails &lt;ReqDtls&gt; / 25.4.5.10 HoldIndicator &lt;HldInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00541.md) | 811–811 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.6 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00542.md) | 812–812 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.6 ProcessingStatus &lt;PrcgSts&gt; / 25.4.6.3 Completed &lt;Cmpltd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00543.md) | 813–813 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 25.4 Message Building Blocks / 25.4.6 ProcessingStatus &lt;PrcgSts&gt; / 25.4.6.6 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00544.md) | 814–814 |

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
