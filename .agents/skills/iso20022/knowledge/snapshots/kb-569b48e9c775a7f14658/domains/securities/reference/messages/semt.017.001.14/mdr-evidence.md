---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.017.001.14"
message_family: "semt.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.017.001.14"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "8 semt.017.001.14 SecuritiesTransactionPostingReportV14", "file_pages": [198, 272]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.017.001.14 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 8 semt.017.001.14 SecuritiesTransactionPostingReportV14

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp198–272; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 8 semt.017.001.14 SecuritiesTransactionPostingReportV14, Functionality, file p198.**

Scope
SecuritiesTransactionPostingReport is sent by an account servicer to an account owner to provide the
details of increases and decreases of holdings which occurred during a specified period, for all or
selected securities in the specified safekeeping account or sub-safekeeping account which the account
servicer holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participants
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
This message may be used as a trade date based or a settlement date based statement.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesTransactionPostingReportV14 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information to the report.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 198 March 2026

**src-000197, 8 semt.017.001.14 SecuritiesTransactionPostingReportV14, Functionality, file p199.**

E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. IntermediaryInformation
Information about the party that provides services relating to financial products to investors, for
example, advice on products and placement of orders for the investment fund.
G. FinancialInstrumentDetails
Reporting per financial instrument.
H. SubAccountDetails
Details at sub-account level.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 199 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00146.md) | 198–199 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00147.md) | 200–203 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00148.md) | 204–213 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00149.md) | 214–214 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.4 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00150.md) | 215–215 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00151.md) | 216–218 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00152.md) | 219–219 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.2 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00153.md) | 220–220 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.4 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00154.md) | 221–221 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.6 ClosingBalance &lt;ClsgBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00155.md) | 222–224 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00156.md) | 225–225 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.8 PoolIdentification &lt;PoolId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00157.md) | 226–226 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.15 MasterReference &lt;MstrRef&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00158.md) | 227–231 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.1 TransactionActivity &lt;TxActvty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00159.md) | 232–232 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.5 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00160.md) | 233–233 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.6 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00161.md) | 234–234 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.9 PostingQuantity &lt;PstngQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00162.md) | 235–235 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.12 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 8.4.7.7.19.12.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00163.md) | 236–236 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.12 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 8.4.7.7.19.12.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00164.md) | 237–237 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.12 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 8.4.7.7.19.12.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 8.4.7.7.19.12.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00165.md) | 238–238 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.16 SettlementDate &lt;SttlmDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00166.md) | 239–239 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.21 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00167.md) | 240–241 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.6 IntermediaryInformation &lt;IntrmyInf&gt; / 8.4.7.7 Transaction &lt;Tx&gt; / 8.4.7.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.7.7.19.22 ReversalIndicator &lt;RvslInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00168.md) | 242–244 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00169.md) | 245–245 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.3 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00170.md) | 246–248 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00171.md) | 249–249 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.2 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00172.md) | 250–250 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.4 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00173.md) | 251–251 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00174.md) | 252–254 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00175.md) | 255–255 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.8 PoolIdentification &lt;PoolId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00176.md) | 256–256 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.16 ClientReference &lt;ClntRef&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00177.md) | 257–261 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.1 TransactionActivity &lt;TxActvty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00178.md) | 262–262 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.5 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00179.md) | 263–263 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.6 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00180.md) | 264–264 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.9 PostingQuantity &lt;PstngQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00181.md) | 265–265 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.12 DigitalPaymentPostingSettlement &lt;DgtlPmtPstngSttlm&gt; / 8.4.8.5.7.19.12.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00182.md) | 266–266 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.12 DigitalPaymentPostingSettlement &lt;DgtlPmtPstngSttlm&gt; / 8.4.8.5.7.19.12.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00183.md) | 267–267 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.12 DigitalPaymentPostingSettlement &lt;DgtlPmtPstngSttlm&gt; / 8.4.8.5.7.19.12.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 8.4.8.5.7.19.12.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00184.md) | 268–268 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.16 SettlementDate &lt;SttlmDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00185.md) | 269–269 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.21 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00186.md) | 270–271 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 8.4 Message Building Blocks / 8.4.8 SubAccountDetails &lt;SubAcctDtls&gt; / 8.4.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 8.4.8.5.7 Transaction &lt;Tx&gt; / 8.4.8.5.7.19 TransactionDetails &lt;TxDtls&gt; / 8.4.8.5.7.19.22 ReversalIndicator &lt;RvslInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00187.md) | 272–272 |

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
