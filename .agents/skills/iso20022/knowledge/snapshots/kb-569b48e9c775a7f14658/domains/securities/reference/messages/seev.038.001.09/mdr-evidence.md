---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.038.001.09"
message_family: "seev.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "10 seev.038.001.09 CorporateActionNarrativeV09", "file_pages": [692, 700]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.038.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 10 seev.038.001.09 CorporateActionNarrativeV09

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp692–700; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 10 seev.038.001.09 CorporateActionNarrativeV09, Functionality, file p692.**

Scope
The CorporateActionNarrative message is sent between an account servicer and an account owner or
its designated agent to cater for such processes that cannot be handled using messages such as the
CorporateActionNotification. It is not to be used for event narrative as that should be included in the
CorporateActionNotification. Examples of when the CorporateActionNarrative message may be used
include tax reclaims, restrictions, documentation requirements. This message should only be used
when bilaterally agreed. This message is bi-directional.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionNarrativeV09 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. AccountDetails
General information about the safekeeping account and the account owner.
B. UnderlyingSecurity
Provides information about the securitised right for entitlement.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. AdditionalInformation
Provides additional information.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 692 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 seev.038.001.09 CorporateActionNarrativeV09](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00527.md) | 692–692 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00528.md) | 693–693 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00529.md) | 694–694 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.1 AccountDetails &lt;AcctDtls&gt; / 10.4.1.1 ForAllAccounts &lt;ForAllAccts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00530.md) | 695–695 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.1 AccountDetails &lt;AcctDtls&gt; / 10.4.1.2 AccountsListAndBalanceDetails &lt;AcctsListAndBalDtls&gt; / 10.4.1.2.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00531.md) | 696–696 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.1 AccountDetails &lt;AcctDtls&gt; / 10.4.1.2 AccountsListAndBalanceDetails &lt;AcctsListAndBalDtls&gt; / 10.4.1.2.4 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00532.md) | 697–697 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00533.md) | 698–698 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.3 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 10.4.3.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00534.md) | 699–699 |
| [10 seev.038.001.09 CorporateActionNarrativeV09 / 10.4 Message Building Blocks / 10.4.4 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00535.md) | 700–700 |

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
