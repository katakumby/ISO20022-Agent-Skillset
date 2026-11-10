---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12"]
file_pages: [727, 728]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 727 to 728.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 727

```text
22 sese.028.001.12
SecuritiesSettlementTransactionAllegementN
otificationV12
22.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementTransactionAllegementNotification to an account
owner to advise the account owner that a counterparty has alleged an instruction against the account
owner's account at the account servicer and that the account servicer could not find the corresponding
instruction of the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionAllegementNotificationV12 MessageDefinition is composed of 18
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the allegement notification known by the executing/servicing party.
B. SettlementTypeAndAdditionalParameters
Provides settlement type and identification information.
C. MarketInfrastructureTransactionIdentification
Identification of a transaction assigned by a market infrastructure other than a central securities
depository, for example, Target2-Securities.
D. CounterpartyMarketInfrastructureTransactionIdentification
Identification of a counterparty transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 727 March 2026
```

## File page 728

```text
E. TradeDetails
Details of the trade.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SecuritiesFinancingDetails
Details of the closing of the securities financing transaction.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. CashParties
Specifies cash parties in the framework of a corporate action event.
N. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
O. OtherAmounts
Other amounts than the settlement amount.
P. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
Q. OtherBusinessParties
Other business parties relevant to the transaction.
R. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 728 March 2026
```

