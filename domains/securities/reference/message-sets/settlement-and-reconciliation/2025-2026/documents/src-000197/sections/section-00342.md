---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.1 MessageDefinition Functionality"]
file_pages: [491, 492, 493]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 491 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
17 sese.023.001.13
SecuritiesSettlementTransactionInstructionV
13
17.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesSettlementTransactionInstruction to an account servicer to instruct
the receipt or delivery of financial instruments with or without payment, physically or by book-entry.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manages a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct the
settlement of transactions to a central securities depository or another settlement market infrastructure.
Usage
The instruction may be linked to other settlement instructions, for example, for a turnaround or back-to-
back, or other transactions, for example, foreign exchange deal, using the linkage functionality.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionInstructionV13 MessageDefinition is composed of 19
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. SettlementTypeAndAdditionalParameters
Provides settlement type and identification information.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 491 March 2026
```

## File page 492

```text
C. NumberCounts
Count of the number of transactions linked.
D. Linkages
Link to another transaction that must be processed after, before or at the same time.
E. TradeDetails
Details of the trade.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
J. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
N. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
O. OtherAmounts
Other amounts than the settlement amount.
P. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
Q. OtherBusinessParties
Other business parties relevant to the transaction.
R. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 492 March 2026
```

## File page 493

```text
S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 493 March 2026
```

