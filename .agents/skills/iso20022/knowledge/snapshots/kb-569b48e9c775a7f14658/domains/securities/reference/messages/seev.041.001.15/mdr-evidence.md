---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.041.001.15"
message_family: "seev.041"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.041.001.15"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "file_pages": [733, 756]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.041.001.15 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp733–756; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15, Functionality, file p733.**

Scope
The CorporateActionInstructionCancellationRequestStatusAdvice message is sent by an account
servicer to an account owner or its designated agent to report the status of a previously received
CorporateActionInstructionCancellationRequest message sent by the account owner. This will include
the acknowledgement/rejection of a request to cancel an outstanding instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionCancellationRequestStatusAdviceV15 MessageDefinition is composed
of 8 MessageBuildingBlocks:
A. InstructionCancellationRequestIdentification
Identification of a related instruction cancellation request document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. InstructionCancellationRequestStatus
Provides information about the processing status of the instruction cancellation request.
E. CorporateActionInstruction
Information about the corporate action option.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 733 February 2026

**src-000080, 13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15, Functionality, file p734.**

H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 734 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00565.md) | 733–734 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00566.md) | 735–735 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00567.md) | 736–738 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00568.md) | 739–739 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00569.md) | 740–740 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 13.4.3.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00570.md) | 741–741 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.4 InstructionCancellationRequestStatus &lt;InstrCxlReqSts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00571.md) | 742–742 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.4 InstructionCancellationRequestStatus &lt;InstrCxlReqSts&gt; / 13.4.4.2 Accepted &lt;Accptd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00572.md) | 743–743 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.4 InstructionCancellationRequestStatus &lt;InstrCxlReqSts&gt; / 13.4.4.3 Rejected &lt;Rjctd&gt; / 13.4.4.3.2 Reason &lt;Rsn&gt; / 13.4.4.3.2.1 ReasonCode &lt;RsnCd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00573.md) | 744–744 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.4 InstructionCancellationRequestStatus &lt;InstrCxlReqSts&gt; / 13.4.4.3 Rejected &lt;Rjctd&gt; / 13.4.4.3.2 Reason &lt;Rsn&gt; / 13.4.4.3.2.1 ReasonCode &lt;RsnCd&gt; / 13.4.4.3.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00574.md) | 745–745 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.4 InstructionCancellationRequestStatus &lt;InstrCxlReqSts&gt; / 13.4.4.5 ProprietaryStatus &lt;PrtrySts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00575.md) | 746–747 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00576.md) | 748–748 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.4 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00577.md) | 749–749 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.8 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00578.md) | 750–750 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.10 TotalEligibleBalance &lt;TtlElgblBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00579.md) | 751–751 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.11 InstructedBalance &lt;InstdBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00580.md) | 752–752 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 13.4.5.14 StatusQuantity &lt;StsQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00581.md) | 753–753 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.6 ProtectInstruction &lt;PrtctInstr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00582.md) | 754–754 |
| [13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15 / 13.4 Message Building Blocks / 13.4.6 ProtectInstruction &lt;PrtctInstr&gt; / 13.4.6.5 UncoveredProtectQuantity &lt;UcvrdPrtctQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00583.md) | 755–756 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Designated agent of the corporate-action account owner](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md) | participant | src-000080 |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | participant | src-000079, src-000080 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | participant | src-000079, src-000080 |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000079-beneficial-owner.md) | participant | src-000079 |
| [Broker](../../../../../shared/reference/participants/participant-src-000079-broker.md) | participant | src-000079 |
| [Clearing Agent](../../../../../shared/reference/participants/participant-src-000079-clearing-agent.md) | participant | src-000079 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000079-csd-icsd.md) | participant | src-000079 |
| [CSD](../../../../../shared/reference/participants/participant-src-000079-csd.md) | participant | src-000079 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000079-fund-manager.md) | participant | src-000079 |
| [Global Custodian](../../../../../shared/reference/participants/participant-src-000079-global-custodian.md) | participant | src-000079 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000079-icsd.md) | participant | src-000079 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000079-institutional-investor.md) | participant | src-000079 |
| [Issuer Agent](../../../../../shared/reference/participants/participant-src-000079-issuer-agent.md) | participant | src-000079 |
| [Issuer](../../../../../shared/reference/participants/participant-src-000079-issuer.md) | participant | src-000079 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000079-market-data-provider.md) | participant | src-000079 |
| [Stock Exchange](../../../../../shared/reference/participants/participant-src-000079-stock-exchange.md) | participant | src-000079 |
| [Sub-Custodian](../../../../../shared/reference/participants/participant-src-000079-sub-custodian.md) | participant | src-000079 |
| [Event Notification](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p145-event-notification.md) | business-flow | src-000079 |
| [Eligibility / Entitlement Notification](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p146-eligibility-entitlement-notification.md) | business-flow | src-000079 |
| [Reminder](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p147-reminder.md) | business-flow | src-000079 |
| [Election](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p149-election.md) | business-flow | src-000079 |
| [Movement Preliminary Advice / Final Entitlement process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p150-movement-preliminary-advice-final-entitlement-process.md) | business-flow | src-000079 |
| [Movement Confirmation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p152-movement-confirmation.md) | business-flow | src-000079 |
| [Movement Reversal](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p153-movement-reversal.md) | business-flow | src-000079, src-000080 |
| [Cancellation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p154-cancellation.md) | business-flow | src-000079 |
| [Status Reporting](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p155-status-reporting.md) | business-flow | src-000079 |
| [Generic Corporate Action Process (Non Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p177-generic-corporate-action-process-non-elective-event.md) | business-flow | src-000079 |
| [Instruction Process (Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p180-instruction-process-elective-event.md) | business-flow | src-000079 |
| [Instruction Cancellation Request Process (Elective Event)](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p183-instruction-cancellation-request-process-elective-event.md) | business-flow | src-000079 |
| [Reminder Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p185-reminder-process.md) | business-flow | src-000079 |
| [Instruction Reporting Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p187-instruction-reporting-process.md) | business-flow | src-000079 |
| [Movement Preliminary Advice Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p189-movement-preliminary-advice-process.md) | business-flow | src-000079 |
| [Movement Preliminary Advice Cancellation Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p191-movement-preliminary-advice-cancellation-process.md) | business-flow | src-000079 |
| [Corporate Action Event Withdrawal Process](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p195-corporate-action-event-withdrawal-process.md) | business-flow | src-000079 |
| [Announcement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p207-announcement.md) | business-flow | src-000079, src-000080 |
| [Announcement and Cancellation of Event](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p217-announcement-and-cancellation-of-event.md) | business-flow | src-000079, src-000080 |
| [Announcement and Cancellation due to Processing Error](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p223-announcement-and-cancellation-due-to-processing-error.md) | business-flow | src-000079, src-000080 |
| [Final Entitlement Replacement Scenario](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p229-final-entitlement-replacement-scenario.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p238-election-and-final-entitlement.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement Cancellation Scenario](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p243-election-and-final-entitlement-cancellation-scenario.md) | business-flow | src-000079, src-000080 |
| [Election and Final Entitlement Replacement](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p251-election-and-final-entitlement-replacement.md) | business-flow | src-000079, src-000080 |
| [Reminder](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p257-reminder.md) | business-flow | src-000079, src-000080 |
| [Confirmation](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p265-confirmation.md) | business-flow | src-000079, src-000080 |
| [Instruction Reporting](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p282-instruction-reporting.md) | business-flow | src-000079, src-000080 |
| [Narrative](../../message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p285-narrative.md) | business-flow | src-000079, src-000080 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
