---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.034.001.16"
message_family: "seev.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.034.001.16"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "file_pages": [320, 359]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.034.001.16 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp320–359; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16, Functionality, file p320.**

Scope
The CorporateActionInstructionStatusAdvice message is sent by an account servicer to an account
owner or its designated agent, to report the status of a received corporate action election instruction.
This message is used to advise the status, or a change in status, of a corporate action-related
transaction previously instructed by, or executed on behalf of, the account owner. This will include the
acknowledgement/rejection of a corporate action instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionStatusAdviceV16 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. InstructionIdentification
Identification of a related instruction document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. InstructionProcessingStatus
Information about the processing status of the instruction.
E. CorporateActionInstruction
Information about the corporate action instruction.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 320 February 2026

**src-000080, 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16, Functionality, file p321.**

H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 321 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00243.md) | 320–321 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00244.md) | 322–323 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00245.md) | 324–329 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00246.md) | 330–330 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00247.md) | 331–331 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 6.4.3.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00248.md) | 332–332 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00249.md) | 333–334 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.1 Cancelled &lt;Canc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00250.md) | 335–335 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.3 Forwarded &lt;Fwdd&gt; / 6.4.4.3.1 ForwardedQuantity &lt;FwddQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00251.md) | 336–336 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.4 Rejected &lt;Rjctd&gt; / 6.4.4.4.1 RejectedQuantity &lt;RjctdQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00252.md) | 337–337 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.4 Rejected &lt;Rjctd&gt; / 6.4.4.4.2 RejectedReason &lt;RjctdRsn&gt; / 6.4.4.4.2.2 Reason &lt;Rsn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00253.md) | 338–340 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.4 Rejected &lt;Rjctd&gt; / 6.4.4.4.2 RejectedReason &lt;RjctdRsn&gt; / 6.4.4.4.2.2 Reason &lt;Rsn&gt; / 6.4.4.4.2.2.1 ReasonCode &lt;RsnCd&gt; / 6.4.4.4.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00254.md) | 341–341 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.5 Pending &lt;Pdg&gt; / 6.4.4.5.2 PendingReason &lt;PdgRsn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00255.md) | 342–342 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.5 Pending &lt;Pdg&gt; / 6.4.4.5.2 PendingReason &lt;PdgRsn&gt; / 6.4.4.5.2.2 Reason &lt;Rsn&gt; / 6.4.4.5.2.2.1 ReasonCode &lt;RsnCd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00256.md) | 343–343 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.5 Pending &lt;Pdg&gt; / 6.4.4.5.2 PendingReason &lt;PdgRsn&gt; / 6.4.4.5.2.2 Reason &lt;Rsn&gt; / 6.4.4.5.2.2.1 ReasonCode &lt;RsnCd&gt; / 6.4.4.5.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00257.md) | 344–344 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.6 Returned &lt;Rtrd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00258.md) | 345–345 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.6 Returned &lt;Rtrd&gt; / 6.4.4.6.2 ReturnedReason &lt;RtrdRsn&gt; / 6.4.4.6.2.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00259.md) | 346–346 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.6 Returned &lt;Rtrd&gt; / 6.4.4.6.2 ReturnedReason &lt;RtrdRsn&gt; / 6.4.4.6.2.2 Reason &lt;Rsn&gt; / 6.4.4.6.2.2.1 ReasonCode &lt;RsnCd&gt; / 6.4.4.6.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00260.md) | 347–347 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.4 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 6.4.4.8 StandingInstruction &lt;StgInstr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00261.md) | 348–348 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00262.md) | 349–349 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00263.md) | 350–350 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.3 OptionFeatures &lt;OptnFeatrs&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00264.md) | 351–351 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.8 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00265.md) | 352–352 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.10 TotalEligibleBalance &lt;TtlElgblBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00266.md) | 353–353 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.11 InstructedBalance &lt;InstdBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00267.md) | 354–354 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.13 ProtectBalance &lt;PrtctBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00268.md) | 355–355 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.5 CorporateActionInstruction &lt;CorpActnInstr&gt; / 6.4.5.15 StatusCashAmount &lt;StsCshAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00269.md) | 356–356 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.6 ProtectInstruction &lt;PrtctInstr&gt; / 6.4.6.1 TransactionType &lt;TxTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00270.md) | 357–357 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.6 ProtectInstruction &lt;PrtctInstr&gt; / 6.4.6.4 ProtectSafekeepingAccount &lt;PrtctSfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00271.md) | 358–358 |
| [6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 / 6.4 Message Building Blocks / 6.4.8 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00272.md) | 359–359 |

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
