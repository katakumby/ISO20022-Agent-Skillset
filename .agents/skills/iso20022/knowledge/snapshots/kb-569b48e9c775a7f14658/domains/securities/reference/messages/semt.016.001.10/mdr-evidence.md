---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.016.001.10"
message_family: "semt.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.016.001.10"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "7 semt.016.001.10 IntraPositionMovementPostingReportV10", "file_pages": [178, 197]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.016.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 7 semt.016.001.10 IntraPositionMovementPostingReportV10

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp178–197; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 7 semt.016.001.10 IntraPositionMovementPostingReportV10, Functionality, file p178.**

Scope
The IntraPositionMovementPostingReport is sent by an account servicer to an account owner to
provide the details of increases and decreases in securities with a given status within a holding, that is,
intra-position transfers, which occurred during a specified period, for all or selected securities in a
specified safekeeping account which the account servicer holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participant
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
:
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementPostingReportV10 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
General information related to the report.
C. AccountOwner
Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 178 March 2026

**src-000197, 7 semt.016.001.10 IntraPositionMovementPostingReportV10, Functionality, file p179.**

D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. FinancialInstrument
Reporting per financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 179 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00130.md) | 178–179 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00131.md) | 180–180 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00132.md) | 181–182 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00133.md) | 183–183 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00134.md) | 184–184 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.5 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00135.md) | 185–185 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00136.md) | 186–186 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.2 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00137.md) | 187–189 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00138.md) | 190–190 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00139.md) | 191–191 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.2 BalanceFrom &lt;BalFr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00140.md) | 192–192 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.3 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.6.3.3.1 Identification &lt;Id&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00141.md) | 193–193 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.3 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.6.3.3.2 SettledQuantity &lt;SttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00142.md) | 194–194 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.3 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.6.3.3.5 SecuritiesSubBalanceIdentification &lt;SctiesSubBalId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00143.md) | 195–195 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.3 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.6.3.3.8 AvailableDate &lt;AvlblDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00144.md) | 196–196 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 7.4 Message Building Blocks / 7.4.6 FinancialInstrument &lt;FinInstrm&gt; / 7.4.6.3 SubBalance &lt;SubBal&gt; / 7.4.6.3.3 IntraPositionMovement &lt;IntraPosMvmnt&gt; / 7.4.6.3.3.11 CollateralMonitorAmount &lt;CollMntrAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00145.md) | 197–197 |

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
