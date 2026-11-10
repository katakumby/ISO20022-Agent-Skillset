---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.044.001.13"
message_family: "seev.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.044.001.13"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "file_pages": [813, 828]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.044.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13

[src-000080](../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf); file pp813–828; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13, Functionality, file p813.**

Scope
The CorporateActionMovementPreliminaryAdviceCancellationAdvice message is sent by an account
servicer to an account owner or its designated agent to cancel a previously announced
CorporateActionMovementPreliminaryAdvice.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 MessageDefinition is
composed of 14 MessageBuildingBlocks:
A. MovementPreliminaryAdviceIdentification
Identification of a previously sent movement preliminary advice document.
B. CorporateActionGeneralInformation
General information about the corporate action event.
C. AccountDetails
General information about the safekeeping account and the account owner.
D. CorporateActionDetails
Information about the corporate action event.
E. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
F. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
G. SubPayingAgent
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 813 February 2026

**src-000080, 15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13, Functionality, file p814.**

Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
H. Registrar
Party/agent responsible for maintaining the register of a security.
I. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
J. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
K. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
L. SolicitationAgent
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
M. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
N. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 814 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00623.md) | 813–814 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00624.md) | 815–815 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00625.md) | 816–816 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00626.md) | 817–817 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.2 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00627.md) | 818–818 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.2 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 15.4.2.4 EventType &lt;EvtTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00628.md) | 819–819 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.3 AccountDetails &lt;AcctDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00629.md) | 820–820 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.3 AccountDetails &lt;AcctDtls&gt; / 15.4.3.1 ForAllAccounts &lt;ForAllAccts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00630.md) | 821–821 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.3 AccountDetails &lt;AcctDtls&gt; / 15.4.3.2 AccountsList &lt;AcctsList&gt; / 15.4.3.2.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00631.md) | 822–822 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.4 CorporateActionDetails &lt;CorpActnDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00632.md) | 823–823 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.4 CorporateActionDetails &lt;CorpActnDtls&gt; / 15.4.4.1 DateDetails &lt;DtDtls&gt; / 15.4.4.1.2 ExDividendDate &lt;ExDvddDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00633.md) | 824–824 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.5 IssuerAgent &lt;IssrAgt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00634.md) | 825–825 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.8 Registrar &lt;Regar&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00635.md) | 826–826 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.11 DropAgent &lt;DrpAgt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00636.md) | 827–827 |
| [15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13 / 15.4 Message Building Blocks / 15.4.14 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00637.md) | 828–828 |

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
