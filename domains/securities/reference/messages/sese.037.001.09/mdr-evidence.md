---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.037.001.09"
message_family: "sese.037"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.037.001.09"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094, 1132]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.037.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 31 sese.037.001.09 PortfolioTransferNotificationV09

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp1094–1132; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 31 sese.037.001.09 PortfolioTransferNotificationV09, Functionality, file p1094.**

Scope
The PortfolioTransferNotification is sent by an account servicer to another account servicer to exchange
transfer settlement details information during a retail or institutional client portfolio transfer.
The account servicer will typically be local agent or global custodian acting on behalf of an investment
management institution, a broker/dealer or a retail client.
Usage
The exchange of transfer settlement details is the provision, by the delivering account servicer to the
receiving account servicer, of the settlement data (such as trade date, settlement date, delivering
settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio
transfer. This delivering account servicer message may also include, for validation, the receiving
settlement chain as provided by the client. In case the receiving settlement chain is not available to the
delivering account servicer, the receiving account servicer may in return provide to the delivering
account servicer the receiving settlement chain using the same message.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The PortfolioTransferNotificationV09 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information on the notification.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1094 March 2026

**src-000197, 31 sese.037.001.09 PortfolioTransferNotificationV09, Functionality, file p1095.**

Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. TransferNotificationDetails
Details of the transfer.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1095 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [31 sese.037.001.09 PortfolioTransferNotificationV09](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00736.md) | 1094–1095 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00737.md) | 1096–1097 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00738.md) | 1098–1101 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00739.md) | 1102–1102 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00740.md) | 1103–1103 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00741.md) | 1104–1106 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.1 NotificationSenderTransactionIdentification &lt;NtfctnSndrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00742.md) | 1107–1107 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.3 CommonIdentification &lt;CmonId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00743.md) | 1108–1108 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.6 Status &lt;Sts&gt; / 31.4.6.6.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00744.md) | 1109–1109 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.6 Status &lt;Sts&gt; / 31.4.6.6.4 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00745.md) | 1110–1110 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.10 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00746.md) | 1111–1111 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.11 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00747.md) | 1112–1113 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.12 Reporting &lt;Rptg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00748.md) | 1114–1114 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.14 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00749.md) | 1115–1115 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.14 SettlementParameters &lt;SttlmParams&gt; / 31.4.6.14.2 Registration &lt;Regn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00750.md) | 1116–1116 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.14 SettlementParameters &lt;SttlmParams&gt; / 31.4.6.14.6 TaxCapacity &lt;TaxCpcty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00751.md) | 1117–1118 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.16 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00752.md) | 1119–1120 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.17 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00753.md) | 1121–1121 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.1 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00754.md) | 1122–1122 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.3 CountryNationalFederalTax &lt;CtryNtlFdrlTax&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00755.md) | 1123–1123 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.6 Other &lt;Othr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00756.md) | 1124–1124 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.9 StampDuty &lt;StmpDty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00757.md) | 1125–1125 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.12 TransactionTax &lt;TxTax&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00758.md) | 1126–1126 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.18 OtherAmounts &lt;OthrAmts&gt; / 31.4.6.18.15 ConsumptionTax &lt;CsmptnTax&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00759.md) | 1127–1127 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.19 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 31.4.6.19.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00760.md) | 1128–1128 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.19 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 31.4.6.19.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00761.md) | 1129–1129 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.19 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 31.4.6.19.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00762.md) | 1130–1130 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.20 OtherBusinessParties &lt;OthrBizPties&gt; / 31.4.6.20.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00763.md) | 1131–1131 |
| [31 sese.037.001.09 PortfolioTransferNotificationV09 / 31.4 Message Building Blocks / 31.4.6 TransferNotificationDetails &lt;TrfNtfctnDtls&gt; / 31.4.6.21 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00764.md) | 1132–1132 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) | participant | src-000196, src-000197, src-000198 |
| [Account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) | participant | src-000196, src-000197, src-000198 |
| [Buy Side Party](../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) | participant | src-000196 |
| [Central Counterparty](../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) | participant | src-000196 |
| [Confirmation Party](../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) | participant | src-000196 |
| [CSD / ICSD](../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) | participant | src-000196 |
| [Executing/servicing party](../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) | participant | src-000196 |
| [Global Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) | participant | src-000196 |
| [Instructing party](../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) | participant | src-000196 |
| [Local Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) | participant | src-000196 |
| [Portfolio transfer client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) | participant | src-000196 |
| [Third party in securities reporting](../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) | participant | src-000196 |
| [Sell Side Party](../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) | participant | src-000196 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) | participant | src-000196 |
| [Stock Exchange](../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) | participant | src-000196 |
| [Cancellation advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md) | business-flow | src-000196 |
| [Cancellation request](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md) | business-flow | src-000196 |
| [Instruction and confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md) | business-flow | src-000196 |
| [Partial settlement confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md) | business-flow | src-000196 |
| [Portfolio transfer](../../message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md) | business-flow | src-000196 |
| [Reconciliation and reporting: pull mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md) | business-flow | src-000196 |
| [Reconciliation and reporting: push mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md) | business-flow | src-000196 |
| [Settlement reversal advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md) | business-flow | src-000196 |
| [Transaction generation notification](../../message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md) | business-flow | src-000196 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
