---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "seev.033.001.14"
message_family: "seev.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.033.001.14"
source_ids: ["src-000080"]
source_locations: [{"source_id": "src-000080", "heading": "5 seev.033.001.14 CorporateActionInstructionV14", "file_pages": [274, 319]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2026"]
---

# seev.033.001.14 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000080 — 5 seev.033.001.14 CorporateActionInstructionV14

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); file pp274–319; publication February 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000080, 5 seev.033.001.14 CorporateActionInstructionV14, Functionality, file p274.**

Scope
The CorporateActionInstruction message is sent by an account owner to an account servicer to instruct
election on a corporate action event.
This message is used to provide the custodian with instructions on how the account owner wishes to
proceed with a corporate action event. Instructions include investment decisions regarding the exercise
of rights issues, the election of stock or cash when the option is available, and decisions on the
conversion or tendering of securities.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionV14 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. ChangeInstructionIndicator
Indicates that the current instruction is replacing a previous one that was cancelled earlier.
B. CancelledInstructionIdentification
Identification of a previously sent cancelled instruction document.
C. InstructionCancellationRequestIdentification
Identification of a previously sent instruction cancellation request document.
D. OtherDocumentIdentification
Identification of other documents as well as the document number.
E. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
F. CorporateActionGeneralInformation
General information about the corporate action event.
G. AccountDetails
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 274 February 2026

**src-000080, 5 seev.033.001.14 CorporateActionInstructionV14, Functionality, file p275.**

General information about the safekeeping account, owner and account balance.
H. BeneficialOwnerDetails
Information about the beneficial owner of the securities.
I. CorporateActionInstruction
Information about the corporate action instruction.
J. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
K. AdditionalInformation
Provides additional information.
L. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 275 February 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/corporate-actions/2025-2026/documents/src-000080/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 seev.033.001.14 CorporateActionInstructionV14](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00206.md) | 274–275 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.2 Structure](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00207.md) | 276–278 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.3 Constraints](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00208.md) | 279–282 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00209.md) | 283–283 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.4 OtherDocumentIdentification &lt;OthrDocId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00210.md) | 284–285 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.1 CorporateActionEventIdentification &lt;CorpActnEvtId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00211.md) | 286–286 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00212.md) | 287–287 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt; / 5.4.6.4.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00213.md) | 288–288 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt; / 5.4.6.4.2 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00214.md) | 289–289 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt; / 5.4.6.4.6 NextCouponDate &lt;NxtCpnDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00215.md) | 290–290 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt; / 5.4.6.4.13 DatedDate &lt;DtdDt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00216.md) | 291–291 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.6 CorporateActionGeneralInformation &lt;CorpActnGnlInf&gt; / 5.4.6.4 UnderlyingSecurity &lt;UndrlygScty&gt; / 5.4.6.4.20 ContractSize &lt;CtrctSz&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00217.md) | 292–293 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.1 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00218.md) | 294–294 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00219.md) | 295–295 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt; / 5.4.7.5.1 TotalEligibleBalance &lt;TtlElgblBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00220.md) | 296–296 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt; / 5.4.7.5.4 CollateralInBalance &lt;CollInBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00221.md) | 297–297 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt; / 5.4.7.5.7 PendingDeliveryBalance &lt;PdgDlvryBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00222.md) | 298–298 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt; / 5.4.7.5.10 SettlementPositionBalance &lt;SttlmPosBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00223.md) | 299–299 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.7 AccountDetails &lt;AcctDtls&gt; / 5.4.7.5 Balance &lt;Bal&gt; / 5.4.7.5.13 InTransshipmentBalance &lt;InTrnsShipmntBal&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00224.md) | 300–300 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.8 BeneficialOwnerDetails &lt;BnfclOwnrDtls&gt; / 5.4.8.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00225.md) | 301–301 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.8 BeneficialOwnerDetails &lt;BnfclOwnrDtls&gt; / 5.4.8.3 DomicileCountry &lt;DmclCtry&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00226.md) | 302–302 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.8 BeneficialOwnerDetails &lt;BnfclOwnrDtls&gt; / 5.4.8.6 CertificationType &lt;CertfctnTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00227.md) | 303–304 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.1 OptionNumber &lt;OptnNb&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00228.md) | 305–305 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.3 OptionFeatures &lt;OptnFeatrs&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00229.md) | 306–306 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.7 SolicitationDealerFeeIndicator &lt;SlctnDealrFeeInd&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00230.md) | 307–307 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.10 CurrencyOption &lt;CcyOptn&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00231.md) | 308–308 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.12 SecuritiesQuantityOrInstructedAmount &lt;SctiesQtyOrInstdAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00232.md) | 309–309 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.12 SecuritiesQuantityOrInstructedAmount &lt;SctiesQtyOrInstdAmt&gt; / 5.4.9.12.1 SecuritiesQuantity &lt;SctiesQty&gt; / 5.4.9.12.1.1 ConditionalQuantity &lt;CondlQty&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00233.md) | 310–310 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.12 SecuritiesQuantityOrInstructedAmount &lt;SctiesQtyOrInstdAmt&gt; / 5.4.9.12.2 InstructedAmount &lt;InstdAmt&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00234.md) | 311–311 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00235.md) | 312–312 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.14 RateAndAmountDetails &lt;RateAndAmtDtls&gt; / 5.4.9.14.4 RequestedSecondLevelTaxRate &lt;ReqdScndLvlTaxRate&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00236.md) | 313–313 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.15 PriceDetails &lt;PricDtls&gt; / 5.4.9.15.1 IndicativeOrMarketPrice &lt;IndctvOrMktPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00237.md) | 314–314 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.15 PriceDetails &lt;PricDtls&gt; / 5.4.9.15.1 IndicativeOrMarketPrice &lt;IndctvOrMktPric&gt; / 5.4.9.15.1.2 MarketPrice &lt;MktPric&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00238.md) | 315–315 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.15 PriceDetails &lt;PricDtls&gt; / 5.4.9.15.4 GenericCashPricePaidPerProduct &lt;GncCshPricPdPerPdct&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00239.md) | 316–316 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.9 CorporateActionInstruction &lt;CorpActnInstr&gt; / 5.4.9.17 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00240.md) | 317–317 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.10 ProtectInstruction &lt;PrtctInstr&gt; / 5.4.10.1 TransactionType &lt;TxTp&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00241.md) | 318–318 |
| [5 seev.033.001.14 CorporateActionInstructionV14 / 5.4 Message Building Blocks / 5.4.11 AdditionalInformation &lt;AddtlInf&gt; / 5.4.11.1 RegistrationDetails &lt;RegnDtls&gt;](../../message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00242.md) | 319–319 |

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
