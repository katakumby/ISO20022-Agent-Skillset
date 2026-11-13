---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.040.001.13"
message_family: "seev.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.040.001.13"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "file_pages": [719, 732]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.040.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp719–732; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13, Functionality, file p719.**

Scope
The CorporateActionInstructionCancellationRequest message is sent by an account owner to an
account servicer to request cancellation of a previously sent corporate action election instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionCancellationRequestV13 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. ChangeInstructionIndicator
Indicates that cancelled instruction will be replaced by a new corporate action instruction to be sent
later.
B. InstructionIdentification
Identification of a previously sent instruction document.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. AccountDetails
General information about the safekeeping account and the account owner.
E. CorporateActionInstruction
Information about the corporate action option.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
H. SupplementaryData
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 719 February 2026

**src-000080, 12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13, Functionality, file p720.**

Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 720 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00553.md) | 719–720 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00554.md) | 721–721 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00555.md); [Constraints continuation C19–C22 (file p724)](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00556.md#file-page-724) | 722–723 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00556.md) | 724–724 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00557.md) | 725–725 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 12.4.3.3 EventType &lt;EvtTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00558.md) | 726–726 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.4 AccountDetails &lt;AcctDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00559.md) | 727–727 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.4 AccountDetails &lt;AcctDtls&gt; / 12.4.4.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00560.md) | 728–728 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.4 AccountDetails &lt;AcctDtls&gt; / 12.4.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00561.md) | 729–729 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 12.4.5.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00562.md) | 730–730 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.6 ProtectInstruction &lt;PrtctInstr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00563.md) | 731–731 |
| [12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13 / 12.4 Message Building Blocks / 12.4.7 AdditionalInformation &lt;AddtlInf&gt; / 12.4.7.1 AdditionalText &lt;AddtlTxt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00564.md) | 732–732 |

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
