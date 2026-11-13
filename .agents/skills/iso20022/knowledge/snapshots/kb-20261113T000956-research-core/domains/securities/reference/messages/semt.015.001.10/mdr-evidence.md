---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.015.001.10"
message_family: "semt.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "6 semt.015.001.10 IntraPositionMovementConfirmationV10", "file_pages": [162, 177]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.015.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 6 semt.015.001.10 IntraPositionMovementConfirmationV10

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp162–177; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 6 semt.015.001.10 IntraPositionMovementConfirmationV10, Functionality, file p162.**

Scope
The IntraPositionMovementConfirmation is sent by an account servicer to an account owner to confirm
the movement of securities within its holding from one sub-balance to another, for example, blocking of
securities.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participant
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementConfirmationV10 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. AdditionalParameters
Additional parameters for the transaction.
B. Linkage
Link to another transaction that triggered the intra-position movement.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 162 March 2026

**src-000197, 6 semt.015.001.10 IntraPositionMovementConfirmationV10, Functionality, file p163.**

F. SafekeepingPlace
Place where the securities are safe-kept, physically or notionally. This place can be, for example, a
local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
G. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
H. FinancialInstrumentAttributes
Elements characterising a financial instrument.
I. IntraPositionDetails
Intra-position movement transaction details.
J. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 163 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00117.md) | 162–163 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00118.md) | 164–164 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00119.md); [Constraints continuation C21 (file p167)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00120.md#file-page-167) | 165–166 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00120.md) | 167–167 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00121.md) | 168–168 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.7 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00122.md) | 169–169 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.8 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00123.md) | 170–171 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00124.md) | 172–172 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt; / 6.4.9.1 SettledQuantity &lt;SttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00125.md) | 173–173 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt; / 6.4.9.2 SecuritiesSubBalanceIdentification &lt;SctiesSubBalId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00126.md) | 174–174 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt; / 6.4.9.5 RemainingToBeSettledQuantity &lt;RmngToBeSttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00127.md) | 175–175 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt; / 6.4.9.7 AvailableDate &lt;AvlblDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00128.md) | 176–176 |
| [6 semt.015.001.10 IntraPositionMovementConfirmationV10 / 6.4 Message Building Blocks / 6.4.9 IntraPositionDetails &lt;IntraPosDtls&gt; / 6.4.9.10 BalanceTo &lt;BalTo&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00129.md) | 177–177 |

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
