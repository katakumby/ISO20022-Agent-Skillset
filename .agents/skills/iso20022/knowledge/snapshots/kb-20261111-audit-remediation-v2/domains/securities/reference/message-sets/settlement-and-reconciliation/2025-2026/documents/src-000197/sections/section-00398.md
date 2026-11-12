---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13"]
file_pages: [599, 600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 599 to 600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 599

```text
19 sese.025.001.13
SecuritiesSettlementTransactionConfirmation
V13
19.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementTransactionConfirmation to an account owner to
confirm the partial or full delivery or receipt of financial instruments, free or against of payment,
physically or by book-entry.
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
The SecuritiesSettlementTransactionConfirmationV13 MessageDefinition is composed of 18
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Provides transaction type and identification information.
B. Linkages
Link to another transaction - provided for information only.
C. AdditionalParameters
Additional parameters for the transaction.
D. TradeDetails
Details of the trade.
E. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 599 March 2026
```

## File page 600

```text
F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
H. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
I. StandingSettlementInstructionDetails
Settlement standing instruction database to be used to derive the settlement parties involved in the
transaction.
J. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
K. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
L. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
M. SettledAmount
Amount effectively settled and which will be credited to/debited from the account owner's cash
account. It may differ from the instructed settlement amount based on market tolerance level.
N. OtherAmounts
Other amounts than the settlement amount.
O. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
P. OtherBusinessParties
Other business parties relevant to the transaction.
Q. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
R. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 600 March 2026
```

