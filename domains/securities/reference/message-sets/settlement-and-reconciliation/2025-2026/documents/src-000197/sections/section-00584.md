---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13"]
file_pages: [879, 880, 881]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27 sese.033.001.13 SecuritiesFinancingInstructionV13

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 879 to 881.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 879

```text
27 sese.033.001.13
SecuritiesFinancingInstructionV13
27.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesFinancingInstruction to a securities financing transaction account
servicer to notify the securities financing transaction account servicer of the details of a repurchase
agreement, reverse repurchase agreement, securities lending or securities borrowing transaction to
allow the account servicer to manage the settlement and follow-up of the opening and closing leg of the
transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct the
settlement of securities financing transactions to a central securities depository or another settlement
market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesFinancingInstructionV13 MessageDefinition is composed of 19 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. TransactionTypeAndAdditionalParameters
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing) and other parameters.
C. NumberCounts
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 879 March 2026
```

## File page 880

```text
Count of the number of transactions linked.
D. Linkages
Link to another transaction that must be processed after, before or at the same time.
E. TradeDetails
Details of the securities financing deal.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SecuritiesFinancingDetails
Details for the closing of the securities financing transaction.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
L. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
M. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
N. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
O. OpeningSettlementAmount
Total amount of money to be paid or received in exchange for the securities at the opening of a
securities financing transaction.
P. OtherAmounts
Other amounts than the settlement amount.
Q. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
R. OtherBusinessParties
Other business parties relevant to the transaction.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 880 March 2026
```

## File page 881

```text
S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 881 March 2026
```

