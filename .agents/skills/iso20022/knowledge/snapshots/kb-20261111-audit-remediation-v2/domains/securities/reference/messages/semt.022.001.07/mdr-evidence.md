---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.022.001.07"
message_family: "semt.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.022.001.07"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433, 457]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.022.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp433–457; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07, Functionality, file p433.**

Scope
This message is sent by the Market Infrastructure to the CSD to advise of the history of all the statuses,
modifications, replacement and cancellation of a specific transaction during its whole life cycle when the
instructing party is a direct participant to the Settlement Infrastructure.
Usage
The message may also be used to:
- re-send a message sent by the market infrastructure to the direct participant,
- provide a third party with a copy of a message being sent by the market infrastructure for information,
- re-send to a third party a copy of a message being sent by the market infrastructure for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionAuditTrailReportV07 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. QueryReference
Identification of the message sent to request this report.
C. TransactionIdentification
Provides unambiguous transaction identification information.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. AccountOwner
Party that legally owns the account.
G. StatusTrail
Provides the history of status and reasons for a pending, posted or cancelled transaction.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 433 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00289.md) | 433–433 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00290.md) | 434–434 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00291.md); [Constraints continuation C2–C8 (file p436)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00292.md#file-page-436) | 435–435 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00292.md) | 436–436 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.2 QueryReference &lt;QryRef&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00293.md) | 437–437 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.5 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00294.md) | 438–439 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.1 StatusDate &lt;StsDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00295.md) | 440–440 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.3 UserIdentification &lt;UsrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00296.md) | 441–441 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00297.md) | 442–442 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.3 Rejected &lt;Rjctd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00298.md) | 443–443 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.5 Cancelled &lt;Canc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00299.md) | 444–444 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.6 PendingCancellation &lt;PdgCxl&gt; / 13.4.7.4.6.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00300.md) | 445–445 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.6 PendingCancellation &lt;PdgCxl&gt; / 13.4.7.4.6.2 Reason &lt;Rsn&gt; / 13.4.7.4.6.2.1 Code &lt;Cd&gt; / 13.4.7.4.6.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00301.md) | 446–446 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.4 ProcessingStatus &lt;PrcgSts&gt; / 13.4.7.4.8 CancellationRequested &lt;CxlReqd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00302.md) | 447–447 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.5 InferredMatchingStatus &lt;IfrrdMtchgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00303.md) | 448–448 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00304.md) | 449–449 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 13.4.7.8.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00305.md) | 450–450 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 13.4.7.8.3 Denied &lt;Dnd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00306.md) | 451–451 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 13.4.7.8.6 Modified &lt;Modfd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00307.md) | 452–452 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 13.4.7.8.6 Modified &lt;Modfd&gt; / 13.4.7.8.6.2 Reason &lt;Rsn&gt; / 13.4.7.8.6.2.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00308.md) | 453–453 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.8 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 13.4.7.8.6 Modified &lt;Modfd&gt; / 13.4.7.8.6.2 Reason &lt;Rsn&gt; / 13.4.7.8.6.2.2 AdditionalReasonInformation &lt;AddtlRsnInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00309.md) | 454–454 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.9 CancellationStatus &lt;CxlSts&gt; / 13.4.7.9.2 Rejected &lt;Rjctd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00310.md) | 455–455 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.9 CancellationStatus &lt;CxlSts&gt; / 13.4.7.9.5 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00311.md) | 456–456 |
| [11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07 / 13.4 Message Building Blocks / 13.4.6 AccountOwner &lt;AcctOwnr&gt; / 13.4.7.10 Settled &lt;Sttld&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00312.md) | 457–457 |

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
