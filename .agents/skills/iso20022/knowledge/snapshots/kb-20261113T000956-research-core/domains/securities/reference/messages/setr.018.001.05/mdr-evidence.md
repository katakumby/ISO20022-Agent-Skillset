---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.018.001.05"
message_family: "setr.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.018.001.05"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "58 setr.018.001.05 RequestForOrderStatusReportV05", "file_pages": [4232, 4252]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# setr.018.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 58 setr.018.001.05 RequestForOrderStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp4232–4252; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 58 setr.018.001.05 RequestForOrderStatusReportV05, Functionality, file p4232.**

Scope
The RequestForOrderStatusReport message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
request the status of one or more order instructions or order cancellation requests.
Usage
The RequestForOrderStatusReport message is used to request the status of:
- one or several individual order instructions, or,
- one or several order messages, or
- one or several individual order cancellation requests, or,
- one or several order cancellation request messages.
The response to a RequestForOrderStatusReport message is the OrderInstructionStatusReport
message or OrderCancellationStatusReport message.
If the RequestForOrderStatusReport message is used to request the status of several individual order
instructions or one or more order instruction messages, then the instructing party may receive several
OrderInstructionStatusReport messages from the executing party.
If the RequestForOrderStatusReport message is used to request the status of several individual order
cancellation requests or one or more order cancellation messages, then the instructing party may
receive several OrderCancellationStatusReport messages from the executing party.
When the RequestForOrderStatusReport is used to request the status of one or more individual orders
or order cancellations, each individual order is identified with its order reference. The investment
account and/or financial instrument related to the order can also be identified. The message
identification of the message in which the individual order was conveyed may also be quoted in
PreviousReference.
When the RequestForOrderStatusReport is used to request the status of an order message or an order
cancellations request message, then the message identification of the order or cancellation message is
identified in PreviousReference.
The RequestForOrderStatusReport message may not be used to request the status of an investment
account, a transfer or the status of a financial instrument.
Outline
The RequestForOrderStatusReportV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageIdentification
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4232 May 2026

**src-000096, 58 setr.018.001.05 RequestForOrderStatusReportV05, Functionality, file p4233.**

Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the order(s) for which the status is requested.
C. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4233 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03025.md) | 4232–4233 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03026.md) | 4234–4234 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03027.md); [Constraints continuation C3–C9 (file p4236)](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03028.md#file-page-4236) | 4235–4235 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03028.md) | 4236–4236 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03029.md) | 4237–4238 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.1 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03030.md) | 4239–4239 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.1 Reference &lt;Ref&gt; / 58.4.2.1.1 PreviousReference &lt;PrvsRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03031.md) | 4240–4241 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03032.md) | 4242–4242 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.5 DealReference &lt;DealRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03033.md) | 4243–4243 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.7 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 58.4.2.3.7.2 AccountName &lt;AcctNm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03034.md) | 4244–4244 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.7 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 58.4.2.3.7.7 SubAccountDetails &lt;SubAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03035.md) | 4245–4246 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03036.md) | 4247–4247 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.1 Identification &lt;Id&gt; / 58.4.2.3.8.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03037.md) | 4248–4248 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.1 Identification &lt;Id&gt; / 58.4.2.3.8.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03038.md) | 4249–4249 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.1 Identification &lt;Id&gt; / 58.4.2.3.8.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 58.4.2.3.8.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03039.md) | 4250–4250 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03040.md) | 4251–4251 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 58.4 Message Building Blocks / 58.4.2 RequestDetails &lt;ReqDtls&gt; / 58.4.2.3 OrderReference &lt;OrdrRef&gt; / 58.4.2.3.8 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 58.4.2.3.8.9 SeriesIdentification &lt;SrsId&gt; / 58.4.2.3.8.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03041.md) | 4252–4252 |

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
