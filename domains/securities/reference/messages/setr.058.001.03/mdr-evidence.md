---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.058.001.03"
message_family: "setr.058"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.058.001.03"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03", "file_pages": [4303, 4322]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# setr.058.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp4303–4322; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03, Functionality, file p4303.**

Scope
The RequestForOrderConfirmationStatusReport message is ent by an executing party, for example, a
transfer agent, to the instructing party, for example, an investment manager or its authorised
representative, to request the status of one or more order confirmations.
Usage
The RequestForOrderConfirmationStatusReport message is used to request the status of either:
- one or several individual order confirmations, or,
- one or several order confirmation messages.
The response to a RequestForOrderConfirmationStatusReport message is the
OrderConfirmationStatusReport message.
When the RequestForOrderConfirmationStatusReport message is used to request the status of several
individual order confirmations or one or more order confirmation messages, the executing party may
receive several OrderConfirmationStatusReport messages from the instructing party.
When the RequestForOrderConfirmationStatusReport is used to request the status of one or more
individual order confirmations, each individual order confirmation is identified with its order reference.
The message identification of the message in which the individual order confirmation was conveyed
may also be quoted in PreviousReference.
When the RequestForOrderConfirmationStatusReport is used to request the status of an order
confirmation message, then the message identification of the order confirmation message is identified in
PreviousReference.
Outline
The RequestForOrderConfirmationStatusReportV03 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the order confirmation for which the status is requested.
C. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4303 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03083.md) | 4303–4303 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03084.md) | 4304–4304 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03085.md) | 4305–4305 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03086.md) | 4306–4306 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03087.md) | 4307–4308 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.1 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03088.md) | 4309–4309 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.1 Reference &lt;Ref&gt; / 65.4.2.1.1 PreviousReference &lt;PrvsRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03089.md) | 4310–4311 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03090.md) | 4312–4312 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.5 DealReference &lt;DealRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03091.md) | 4313–4313 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.7 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 65.4.2.3.7.2 AccountName &lt;AcctNm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03092.md) | 4314–4314 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.7 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 65.4.2.3.7.7 SubAccountDetails &lt;SubAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03093.md) | 4315–4316 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03094.md) | 4317–4317 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.1 Identification &lt;Id&gt; / 65.4.2.3.8.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03095.md) | 4318–4318 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.1 Identification &lt;Id&gt; / 65.4.2.3.8.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03096.md) | 4319–4319 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.1 Identification &lt;Id&gt; / 65.4.2.3.8.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 65.4.2.3.8.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03097.md) | 4320–4320 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03098.md) | 4321–4321 |
| [62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 / 65.4 Message Building Blocks / 65.4.2 RequestDetails &lt;ReqDtls&gt; / 65.4.2.3 OrderReference &lt;OrdrRef&gt; / 65.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 65.4.2.3.8.9 SeriesIdentification &lt;SrsId&gt; / 65.4.2.3.8.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03099.md) | 4322–4322 |

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
