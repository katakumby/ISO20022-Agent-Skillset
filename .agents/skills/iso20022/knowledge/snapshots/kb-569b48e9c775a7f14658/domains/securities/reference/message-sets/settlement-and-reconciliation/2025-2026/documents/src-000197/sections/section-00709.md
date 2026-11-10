---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10"]
file_pages: [1059, 1060]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1059 to 1060.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1059

```text
30 sese.036.001.10
SecuritiesFinancingModificationInstructionV1
0
30.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesFinancingModificationInstruction to a securities financing
transaction account servicer to notify the securities financing transaction account servicer of an update
in the details of a repurchase agreement, reverse repurchase agreement, securities lending or
securities borrowing transaction that does not impact the original transaction securities quantity.
Such a change may be:
- the providing of closing details not available at the time of the sending of the Securities Financing
Instruction, for example, termination date for an open repo,
- the providing of a new rate, for example, a repo rate,
- the rollover of a position extending the closing or maturity date.
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
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1059 March 2026
```

## File page 1060

```text
The SecuritiesFinancingModificationInstructionV10 MessageDefinition is composed of 11
MessageBuildingBlocks:
A. TransactionTypeAndModificationAdditionalParameters
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing), modification information and
other parameters.
B. TradeDetails
Details of the securities financing deal.
C. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
D. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
E. SecuritiesFinancingAdditionalDetails
Details of the closing of the securities financing transaction.
F. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
G. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
H. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
I. OpeningSettlementAmount
Total amount of money to be paid or received in exchange for the securities at the opening of a
securities financing transaction.
J. OpeningDigitalSettlementAmount
Amount of digital asset that is to be/was posted to the account as a means of payment.
K. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1060 March 2026
```

