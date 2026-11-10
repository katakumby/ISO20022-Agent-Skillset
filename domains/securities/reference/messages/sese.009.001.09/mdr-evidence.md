---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.009.001.09"
message_family: "sese.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.009.001.09"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "32 sese.009.001.09 RequestForTransferStatusReportV09", "file_pages": [784, 808]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.009.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 32 sese.009.001.09 RequestForTransferStatusReportV09

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp784–808; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 32 sese.009.001.09 RequestForTransferStatusReportV09, Functionality, file p784.**

Scope
The RequestForTransferStatusReport is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent to
request the status of a previously instructed transfer.
The RequestForTransferStatusReport may also be sent by any party in the transfer transaction to
another party in the transfer transaction chain to request information relevant for the settlement of a
transfer transaction.
Usage
The RequestForTransferStatusReport is used to request either:
- the status of one or several information requests or transfer instructions or,
- the status of one or several transfer cancellation instructions, or
- information relevant to one or more transfer instructions.
Outline
The RequestForTransferStatusReportV09 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the transfer for which the status is requested.
C. MarketPracticeVersion
Identifies the market practice to which the message conforms.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 784 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00580.md) | 784–784 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00581.md) | 785–786 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00582.md) | 787–790 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.1 Reference &lt;Ref&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00583.md) | 791–791 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.2 TypeOfRequest &lt;TpOfReq&gt; / 32.4.2.2.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00584.md) | 792–792 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.5 ClientReference &lt;ClntRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00585.md) | 793–793 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00586.md) | 794–794 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt; / 32.4.2.7.1.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00587.md) | 795–795 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt; / 32.4.2.7.1.1 Identification &lt;Id&gt; / 32.4.2.7.1.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00588.md) | 796–796 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt; / 32.4.2.7.1.1 Identification &lt;Id&gt; / 32.4.2.7.1.1.3 CUSIP &lt;CUSIP&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00589.md) | 797–797 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt; / 32.4.2.7.1.1 Identification &lt;Id&gt; / 32.4.2.7.1.1.10 Dutch &lt;Dtch&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00590.md) | 798–798 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.1 Security &lt;Scty&gt; / 32.4.2.7.1.1 Identification &lt;Id&gt; / 32.4.2.7.1.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 32.4.2.7.1.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00591.md) | 799–799 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.7 Instrument &lt;Instrm&gt; / 32.4.2.7.3 OtherAsset &lt;OthrAsst&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00592.md) | 800–800 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 32.4.2.8.1 OwnerIdentification &lt;OwnrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00593.md) | 801–801 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 32.4.2.8.4 AccountName &lt;AcctNm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00594.md) | 802–802 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.8 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 32.4.2.8.8 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00595.md) | 803–803 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.10 QueryInformation &lt;QryInf&gt; / 32.4.2.10.1 QueryType &lt;QryTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00596.md) | 804–804 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.10 QueryInformation &lt;QryInf&gt; / 32.4.2.10.4 RejectionReason &lt;RjctnRsn&gt; / 32.4.2.10.4.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00597.md) | 805–806 |
| [31 sese.008.001.09 ReversalOfTransferInConfirmationV09 / 32.4 Message Building Blocks / 32.4.2.10 QueryInformation &lt;QryInf&gt; / 32.4.2.10.4 RejectionReason &lt;RjctnRsn&gt; / 32.4.2.10.4.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00598.md) | 807–808 |

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
