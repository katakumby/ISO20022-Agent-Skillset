---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.1 MessageDefinition Functionality"]
file_pages: [815, 816]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 815 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 815

```text
26 sese.032.001.13
SecuritiesSettlementTransactionGenerationN
otificationV13
26.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementTransactionGenerationNotification to an account
owner to advise the account owner of a securities settlement transaction that has been generated/
created by the account servicer for the account owner. The reason for creation can range from the
automatic transformation of pending settlement instructions following a corporate event to the recovery
of an account owner transactions' database initiated by its account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionGenerationNotificationV13 MessageDefinition is composed of 19
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Provides transaction type and identification information.
B. NumberCounts
Count of the number of transactions linked.
C. Linkages
Link to another transaction that must be processed after, before or at the same time.
D. TradeDetails
Details of the trade.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 815 March 2026
```

## File page 816

```text
E. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
H. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
I. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
J. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
K. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
L. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
M. OtherAmounts
Other amounts than the settlement amount.
N. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
O. OtherBusinessParties
Other business parties relevant to the transaction.
P. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
Q. GeneratedReason
Specifies the reason why the transaction was generated.
R. StatusAndReason
Status and reason of the transaction.
S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 816 March 2026
```

