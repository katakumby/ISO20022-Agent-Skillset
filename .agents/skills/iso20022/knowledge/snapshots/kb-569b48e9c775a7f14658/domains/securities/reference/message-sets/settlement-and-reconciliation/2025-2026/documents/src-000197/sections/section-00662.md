---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13"]
file_pages: [994, 995]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29 sese.035.001.13 SecuritiesFinancingConfirmationV13

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 994 to 995.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 994

```text
29 sese.035.001.13
SecuritiesFinancingConfirmationV13
29.1 MessageDefinition Functionality
Scope
A securities financing transaction account servicer sends a SecuritiesFinancingConfirmation to an
account owner to confirm or advise of the partial or full settlement of the opening or closing leg of a
securities financing transaction.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure managing securities
financing transactions on behalf of their participants
- an agent (sub-custodian) managing securities financing transactions on behalf of their global
custodian customer, or
- a custodian managing securities financing transactions on behalf of an investment management
institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesFinancingConfirmationV13 MessageDefinition is composed of 17
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing) and other parameters.
B. AdditionalParameters
Additional parameters for the transaction.
C. TradeDetails
Details of the securities financing deal.
D. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 994 March 2026
```

## File page 995

```text
E. FinancialInstrumentAttributes
Elements characterising a financial instrument.
F. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
G. SecuritiesFinancingDetails
Details of the closing of the securities financing transaction.
H. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
I. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
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
Q. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 995 March 2026
```

