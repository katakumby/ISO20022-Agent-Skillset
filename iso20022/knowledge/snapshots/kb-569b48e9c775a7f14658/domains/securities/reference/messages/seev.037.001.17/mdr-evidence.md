---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.037.001.17"
message_family: "seev.037"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.037.001.17"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "file_pages": [665, 691]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.037.001.17 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 9 seev.037.001.17 CorporateActionMovementReversalAdviceV17

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp665–691; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 9 seev.037.001.17 CorporateActionMovementReversalAdviceV17, Functionality, file p665.**

Scope
The CorporateActionMovementReversalAdvice message is sent by an account servicer to an account
owner or its designated agent to reverse a previously confirmed posting of securities or cash.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionMovementReversalAdviceV17 MessageDefinition is composed of 14
MessageBuildingBlocks:
A. MovementConfirmationIdentification
Identification of a previously sent movement confirmation document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
D. ReversalReason
Reason for the reversal.
E. TransactionIdentification
Transaction type and identification information.
F. CorporateActionGeneralInformation
General information about the corporate action event.
G. AccountDetails
General information about the safekeeping account, owner and account balance.
H. CorporateActionDetails
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 665 February 2026

**src-000080, 9 seev.037.001.17 CorporateActionMovementReversalAdviceV17, Functionality, file p666.**

Information about the corporate action event.
I. CorporateActionConfirmationDetails
Information about the corporate action option.
J. AdditionalInformation
Provides additional information.
K. IssuerAgent
Party appointed to administer the event on behalf of the issuer company/offeror. The party may be
contacted for more information about the event.
L. PayingAgent
Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate action
event on behalf of the issuer company/offeror.
M. SubPayingAgent
Sub-agent appointed to execute the payment for the corporate action event on behalf of the issuer
company/offeror.
N. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 666 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00504.md) | 665–666 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00505.md) | 667–668 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00506.md) | 669–670 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00507.md) | 671–671 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.3 EventsLinkage &lt;EvtsLkg&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00508.md) | 672–672 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.4 ReversalReason &lt;RvslRsn&gt; / 9.4.4.1 Reason &lt;Rsn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00509.md) | 673–673 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.4 ReversalReason &lt;RvslRsn&gt; / 9.4.4.2 AdditionalReasonInformation &lt;AddtlRsnInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00510.md) | 674–674 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 9.4.6.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00511.md) | 675–675 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 9.4.6.5 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00512.md) | 676–676 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 9.4.6.6 FractionalQuantity &lt;FrctnlQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00513.md) | 677–677 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.7 AccountDetails &lt;AcctDtls&gt; / 9.4.7.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00514.md) | 678–678 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.8 CorporateActionDetails &lt;CorpActnDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00515.md) | 679–679 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.8 CorporateActionDetails &lt;CorpActnDtls&gt; / 9.4.8.1 DateDetails &lt;DtDtls&gt; / 9.4.8.1.2 ExDividendDate &lt;ExDvddDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00516.md) | 680–680 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.8 CorporateActionDetails &lt;CorpActnDtls&gt; / 9.4.8.4 FollowingEventTypeIndicator &lt;FllwngEvtTpInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00517.md) | 681–681 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00518.md) | 682–682 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.3 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00519.md) | 683–683 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.3 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 9.4.9.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00520.md) | 684–684 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.3 SecuritiesMovementDetails &lt;SctiesMvmntDtls&gt; / 9.4.9.3.4 PostingDate &lt;PstngDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00521.md) | 685–685 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.4 CashMovementDetails &lt;CshMvmntDtls&gt; / 9.4.9.4.1 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00522.md) | 686–686 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.4 CashMovementDetails &lt;CshMvmntDtls&gt; / 9.4.9.4.2 Account &lt;Acct&gt; / 9.4.9.4.2.2 ChargesAccount &lt;ChrgsAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00523.md) | 687–687 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.9 CorporateActionConfirmationDetails &lt;CorpActnConfDtls&gt; / 9.4.9.4 CashMovementDetails &lt;CshMvmntDtls&gt; / 9.4.9.4.5 ValueDate &lt;ValDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00524.md) | 688–688 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.10 AdditionalInformation &lt;AddtlInf&gt; / 9.4.10.1 AdditionalText &lt;AddtlTxt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00525.md) | 689–689 |
| [9 seev.037.001.17 CorporateActionMovementReversalAdviceV17 / 9.4 Message Building Blocks / 9.4.12 PayingAgent &lt;PngAgt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00526.md) | 690–691 |

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
