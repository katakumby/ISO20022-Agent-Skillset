---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.057.001.03"
message_family: "setr.057"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.057.001.03"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283, 4302]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# setr.057.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 64 setr.057.001.03 OrderConfirmationStatusReportV03

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp4283–4302; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 64 setr.057.001.03 OrderConfirmationStatusReportV03, Functionality, file p4283.**

Scope
The OrderConfirmationStatusReport message is sent by an instructing party, for example, an
investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to report the status of an order confirmation or an order confirmation amendment.
Usage
The OrderConfirmationStatusReport message is used to report on the status of one or more individual:
- subscription confirmations,
- subscription confirmation amendments,
- redemption confirmations,
- redemption confirmation amendments,
- switch order confirmations,
- switch order confirmation amendments.
One of the following statuses can be reported:
- confirmation rejected, or,
- amendment rejected, or,
- sent to next party, or,
- communication problem with next party, or,
- confirmation accepted, or,
- confirmation received.
It is likely that the OrderConfirmationStatusReport is only sent by the order instructing party to the order
executing party to reject an order confirmation or to reject an order confirmation amendment, although if
an intermediary party is used, the statuses sent to next party and communication problem with next
party are also likely be used. The statuses confirmation accepted and confirmation received would only
be used in the event the order executing party sends a RequestForOrderConfirmationStatusReport
message and one of the other statuses does not apply.
If the status being reported is either confirmation rejected or amendment rejected, then a reason for the
rejection must be given.
The individual order confirmation or confirmation amendment for which the status is given is identified
with its order reference. The message identification of the message in which the individual order
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4283 May 2026

**src-000096, 64 setr.057.001.03 OrderConfirmationStatusReportV03, Functionality, file p4284.**

confirmation or confirmation amendment was conveyed may also be quoted in RelatedReference, but
this is not recommended.
Outline
The OrderConfirmationStatusReportV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. IndividualOrderConfirmationDetailsReport
Status report details of an individual order confirmation.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4284 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03066.md) | 4283–4284 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03067.md) | 4285–4285 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03068.md); [Constraints continuation C2–C9 (file p4287)](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03069.md#file-page-4287) | 4286–4286 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03069.md) | 4287–4287 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03070.md) | 4288–4289 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03071.md) | 4290–4290 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.3 Confirmation &lt;Conf&gt; / 64.4.3.3.1 ConfirmationRejected &lt;ConfRjctd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03072.md) | 4291–4291 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.3 Confirmation &lt;Conf&gt; / 64.4.3.3.3 Status &lt;Sts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03073.md) | 4292–4292 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03074.md) | 4293–4293 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 64.4.3.8.3 AccountDesignation &lt;AcctDsgnt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03075.md) | 4294–4294 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 64.4.3.8.7 SubAccountDetails &lt;SubAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03076.md) | 4295–4296 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03077.md) | 4297–4297 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.1 Identification &lt;Id&gt; / 64.4.3.9.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03078.md) | 4298–4298 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.1 Identification &lt;Id&gt; / 64.4.3.9.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03079.md) | 4299–4299 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.1 Identification &lt;Id&gt; / 64.4.3.9.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 64.4.3.9.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03080.md) | 4300–4300 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03081.md) | 4301–4301 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 64.4 Message Building Blocks / 64.4.3 IndividualOrderConfirmationDetailsReport &lt;IndvOrdrConfDtlsRpt&gt; / 64.4.3.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 64.4.3.9.9 SeriesIdentification &lt;SrsId&gt; / 64.4.3.9.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03082.md) | 4302–4302 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000095-beneficial-owner.md) | participant | src-000095 |
| [Concentrator](../../../../../shared/reference/participants/participant-src-000095-concentrator.md) | participant | src-000095 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000095-csd-icsd.md) | participant | src-000095 |
| [CSD](../../../../../shared/reference/participants/participant-src-000095-csd.md) | participant | src-000095 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md) | participant | src-000095 |
| [Distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md) | participant | src-000095 |
| [Executing Party / Registering Party](../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md) | participant | src-000095 |
| [Executing Party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | participant | src-000095 |
| [Fund Accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | participant | src-000095 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md) | participant | src-000095 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000095-icsd.md) | participant | src-000095 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000095-institutional-investor.md) | participant | src-000095 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | participant | src-000095 |
| [Intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | participant | src-000095 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | participant | src-000095 |
| [Paying Agent](../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | participant | src-000095 |
| [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md) | participant | src-000095 |
| [Reporting Party](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | participant | src-000095 |
| [Requesting Party](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | participant | src-000095 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | participant | src-000095 |
| [Transferee's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md) | participant | src-000095 |
| [Transferee's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md) | participant | src-000095 |
| [Transferor's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md) | participant | src-000095 |
| [Transferor's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md) | participant | src-000095 |
| [Account Administration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p185-account-administration.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p186-order-processing.md) | business-flow | src-000095 |
| [Order Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | business-flow | src-000095 |
| [Payment Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p188-payment-execution.md) | business-flow | src-000095 |
| [Payment Execution - Advance Pay In](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | business-flow | src-000095 |
| [Payment Execution - Pay In Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p190-payment-execution-pay-in-arrears.md) | business-flow | src-000095 |
| [Payment Execution - Pay Out Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | business-flow | src-000095 |
| [Tax Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | business-flow | src-000095 |
| [Fund Valuation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p193-fund-valuation.md) | business-flow | src-000095 |
| [Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Transaction Based Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Trailer Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | business-flow | src-000095 |
| [Reconciliation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p197-reconciliation.md) | business-flow | src-000095 |
| [Distribution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | business-flow | src-000095 |
| [Registration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | business-flow | src-000095 |
| [Account Opening](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | business-flow | src-000095 |
| [Account Modification](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | business-flow | src-000095 |
| [Reporting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | business-flow | src-000095 |
| [Custody and Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | business-flow | src-000095 |
| [Transparency of Holdings](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | business-flow | src-000095 |
| [Stock Transfers (Single Leg Transfer)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Single Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | business-flow | src-000095 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
