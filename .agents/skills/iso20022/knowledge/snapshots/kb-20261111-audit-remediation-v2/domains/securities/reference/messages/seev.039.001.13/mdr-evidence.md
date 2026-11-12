---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.039.001.13"
message_family: "seev.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.039.001.13"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "11 seev.039.001.13 CorporateActionCancellationAdviceV13", "file_pages": [701, 718]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.039.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 11 seev.039.001.13 CorporateActionCancellationAdviceV13

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp701–718; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 11 seev.039.001.13 CorporateActionCancellationAdviceV13, Functionality, file p701.**

Scope
The CorporateActionCancellationAdvice message is sent by an account servicer to an account owner
or its designated agent to cancel a previously announced corporate action event in case of error from
the account servicer or in case of withdrawal by the issuer.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionCancellationAdviceV13 MessageDefinition is composed of 15
MessageBuildingBlocks:
A. CancellationAdviceGeneralInformation
General information about the event cancellation status and cancellation reason.
B. CorporateActionGeneralInformation
General information about the corporate action event.
C. AccountsDetails
General information about the safekeeping account and the account owner.
D. CorporateActionDetails
Information about the corporate action event.
E. AdditionalText
Provides additional information or specifies in more detail the content of a message. This field may
only be used when the information to be transmitted, cannot be coded.
F. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
G. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 701 February 2026

**src-000080, 11 seev.039.001.13 CorporateActionCancellationAdviceV13, Functionality, file p702.**

H. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
I. Registrar
Party/agent responsible for maintaining the register of a security.
J. ResellingAgent
Broker-dealer responsible for reselling to new investors securities (usually bonds) that have been
tendered for purchase by their owner.
K. PhysicalSecuritiesAgent
Trust company, bank or similar financial institution assigned by an issuer to accept presentations of
instruments, usually bonds, for transfer and or exchange.
L. DropAgent
Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent or
event agent where securities can be delivered in person.
M. SolicitationAgent
Trust company, bank or similar financial institution assigned by an issuer to maintain records of
investors and account balances and transactions for the consent of a material change.
N. InformationAgent
Trust company, bank or similar financial institution assigned by an Issuer to provide information
and copies of the offering documentation.
O. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 702 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00536.md) | 701–702 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00537.md) | 703–703 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00538.md); [Constraints continuation C6–C14 (file p705)](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00539.md#file-page-705) | 704–704 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00539.md) | 705–705 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.1 CancellationAdviceGeneralInformation &lt;CxlAdvcGnlInf&gt; / 11.4.1.1 CancellationReasonCode &lt;CxlRsnCd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00540.md) | 706–706 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.1 CancellationAdviceGeneralInformation &lt;CxlAdvcGnlInf&gt; / 11.4.1.3 ProcessingStatus &lt;PrcgSts&gt; / 11.4.1.3.2 EventConfirmationStatus &lt;EvtConfSts&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00541.md) | 707–707 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.2 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 11.4.2.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00542.md) | 708–708 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.2 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 11.4.2.5 MandatoryVoluntaryEventType &lt;MndtryVlntryEvtTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00543.md) | 709–709 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.3 AccountsDetails &lt;AcctsDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00544.md) | 710–710 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.3 AccountsDetails &lt;AcctsDtls&gt; / 11.4.3.2 AccountsList &lt;AcctsList&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00545.md) | 711–711 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.3 AccountsDetails &lt;AcctsDtls&gt; / 11.4.3.2 AccountsList &lt;AcctsList&gt; / 11.4.3.2.2 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00546.md) | 712–712 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.4 CorporateActionDetails &lt;CorpActnDtls&gt; / 11.4.4.1 DateDetails &lt;DtDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00547.md) | 713–713 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.4 CorporateActionDetails &lt;CorpActnDtls&gt; / 11.4.4.2 EventStage &lt;EvtStag&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00548.md) | 714–714 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.5 AdditionalText &lt;AddtlTxt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00549.md) | 715–715 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.9 Registrar &lt;Regar&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00550.md) | 716–716 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.12 DropAgent &lt;DrpAgt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00551.md) | 717–717 |
| [11 seev.039.001.13 CorporateActionCancellationAdviceV13 / 11.4 Message Building Blocks / 11.4.15 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00552.md) | 718–718 |

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
