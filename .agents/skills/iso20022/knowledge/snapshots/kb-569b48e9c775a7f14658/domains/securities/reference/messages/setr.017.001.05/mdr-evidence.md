---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.017.001.05"
message_family: "setr.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.017.001.05"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "57 setr.017.001.05 OrderCancellationStatusReportV05", "file_pages": [4205, 4231]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# setr.017.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 57 setr.017.001.05 OrderCancellationStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp4205–4231; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 57 setr.017.001.05 OrderCancellationStatusReportV05, Functionality, file p4205.**

Scope
The OrderCancellationStatusReport message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
report the status of an order cancellation request that was previously received.
Usage
The OrderCancellationStatusReport message is used to provide the status of:
- one or more individual order cancellation requests by using IndividualCancellationStatusReport, or,
- an order cancellation request message by using CancellationStatusReport.
If the OrderCancellationStatusReport message is used to report the status of an individual order
cancellation request, then the repetitive IndividualCancellationStatusReport sequence is used and the
order reference of the individual order is quoted in OrderReference. The message identification of the
message in which the individual order was conveyed may also be quoted in RelatedReference but this
is not recommended.
If the OrderCancellationStatusReport message is used to report the status of an entire order
cancellation request message, for example, the SubscriptionBulkOrderCancellationRequest, or a
SubscriptionOrderCancellationRequest containing several orders, then the CancellationStatusReport
sequence is used. The message identification of the order cancellation request message may also be
quoted in RelatedReference but this is not recommended. All the order cancellation requests within the
message must have the same status.
One of the following statuses can be reported:
- the order cancellation is pending, or,
- the order cancellation request is rejected, or,
- the order is cancelled.
When the cancellation is rejected, the reason for the rejection must be specified.
Outline
The OrderCancellationStatusReportV05 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. StatusReport
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4205 May 2026

**src-000096, 57 setr.017.001.05 OrderCancellationStatusReportV05, Functionality, file p4206.**

Status of the order cancellation.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4206 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03004.md) | 4205–4206 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03005.md) | 4207–4208 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03006.md) | 4209–4209 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03007.md) | 4210–4212 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.1 CancellationStatusReport &lt;CxlStsRpt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03008.md) | 4213–4213 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.1 CancellationStatusReport &lt;CxlStsRpt&gt; / 57.4.3.1.2 CancellationStatus &lt;CxlSts&gt; / 57.4.3.1.2.1 Status &lt;Sts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03009.md) | 4214–4214 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.1 CancellationStatusReport &lt;CxlStsRpt&gt; / 57.4.3.1.2 CancellationStatus &lt;CxlSts&gt; / 57.4.3.1.2.2 Rejected &lt;Rjctd&gt; / 57.4.3.1.2.2.1 Reason &lt;Rsn&gt; / 57.4.3.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03010.md) | 4215–4215 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.1 CancellationStatusReport &lt;CxlStsRpt&gt; / 57.4.3.1.3 StatusInitiator &lt;StsInitr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03011.md) | 4216–4217 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03012.md) | 4218–4218 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.3 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03013.md) | 4219–4219 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.6 CancellationStatus &lt;CxlSts&gt; / 57.4.3.2.6.2 Rejected &lt;Rjctd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03014.md) | 4220–4220 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.6 CancellationStatus &lt;CxlSts&gt; / 57.4.3.2.6.2 Rejected &lt;Rjctd&gt; / 57.4.3.2.6.2.1 Reason &lt;Rsn&gt; / 57.4.3.2.6.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03015.md) | 4221–4221 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03016.md) | 4222–4222 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 57.4.3.2.8.4 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03017.md) | 4223–4223 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 57.4.3.2.8.8 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03018.md) | 4224–4225 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03019.md) | 4226–4226 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.1 Identification &lt;Id&gt; / 57.4.3.2.9.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03020.md) | 4227–4227 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.1 Identification &lt;Id&gt; / 57.4.3.2.9.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03021.md) | 4228–4228 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.1 Identification &lt;Id&gt; / 57.4.3.2.9.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 57.4.3.2.9.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03022.md) | 4229–4229 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03023.md) | 4230–4230 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 57.4 Message Building Blocks / 57.4.3 StatusReport &lt;StsRpt&gt; / 57.4.3.2 IndividualCancellationStatusReport &lt;IndvCxlStsRpt&gt; / 57.4.3.2.9 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 57.4.3.2.9.9 SeriesIdentification &lt;SrsId&gt; / 57.4.3.2.9.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03024.md) | 4231–4231 |

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
