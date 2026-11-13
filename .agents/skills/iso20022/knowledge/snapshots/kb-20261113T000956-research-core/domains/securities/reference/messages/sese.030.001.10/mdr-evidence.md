---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.030.001.10"
message_family: "sese.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.030.001.10"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "file_pages": [783, 801]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.030.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp783–801; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10, Functionality, file p783.**

Scope
An account owner sends a SecuritiesSettlementConditionsModificationRequest to an account servicer
to request the modification of a processing indicator or another non-matching information.
The account owner/servicer relationship may be:
- a central securities depository participant which has an account with a central securities depository.
It could also be, if agreed in a service level agreement:
- a global custodian which has an account with its local agent (sub-custodian), or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
In markets where this applies (for example, securities market infrastructures with no pre-settlement
matching process), it is used by a party to approve, cancel or reject a transaction instructed by the
counterparty.
This message cannot be used to request the modification of trade or event details.
The use of AdditionalInformation and its fields must be pre-agreed between account servicer and
account owner. The fields in that sequence cannot be used to amend a trade or event detail unless
authorised by country market practice.
Outline
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 783 March 2026

**src-000197, 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10, Functionality, file p784.**

The SecuritiesSettlementConditionsModificationRequestV10 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. AccountOwner
Party that legally owns the account.
B. SafekeepingAccount
Account to or from which a securities entry is made.
C. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
D. RequestDetails
Details of the request.
E. AdditionalInformation
Additional information that cannot be captured in the structured elements and/or any other specific
block.
F. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 784 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00516.md) | 783–784 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00517.md) | 785–785 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00518.md); [Constraints continuation C21–C25 (file p788)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00519.md#file-page-788) | 786–787 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00519.md) | 788–788 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.3 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00520.md) | 789–789 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.4 RequestDetails &lt;ReqDtls&gt; / 24.4.4.1 Reference &lt;Ref&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00521.md) | 790–790 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.4 RequestDetails &lt;ReqDtls&gt; / 24.4.4.2 RestrictionReference &lt;RstrctnRef&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00522.md) | 791–791 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.4 RequestDetails &lt;ReqDtls&gt; / 24.4.4.4 RetainIndicator &lt;RtnInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00523.md) | 792–792 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.4 RequestDetails &lt;ReqDtls&gt; / 24.4.4.8 PartialSettlementIndicator &lt;PrtlSttlmInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00524.md) | 793–793 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.4 RequestDetails &lt;ReqDtls&gt; / 24.4.4.11 MatchingDenial &lt;MtchgDnl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00525.md) | 794–794 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00526.md) | 795–795 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00527.md) | 796–796 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.5 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00528.md) | 797–797 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.6 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00529.md) | 798–798 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.9 CutOffDate &lt;CutOffDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00530.md) | 799–799 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.12 ReceivingParty1 &lt;RcvgPty1&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00531.md) | 800–800 |
| [24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10 / 24.4 Message Building Blocks / 24.4.5 AdditionalInformation &lt;AddtlInf&gt; / 24.4.5.13 TransactionSubjectToBuyIn &lt;TxSbjtToBuyIn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00532.md) | 801–801 |

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
