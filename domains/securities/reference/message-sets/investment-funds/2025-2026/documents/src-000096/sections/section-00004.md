---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08"]
file_pages: [20, 21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2 acmt.001.001.08 AccountOpeningInstructionV08

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 20 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
2 acmt.001.001.08
AccountOpeningInstructionV08
2.1 MessageDefinition Functionality
Scope
The AccountOpeningInstruction message is sent by an account owner, for example, an investor or its
designated agent to the account servicer, for example, a registrar, transfer agent, custodian or
securities depository, to instruct the opening of an account or the opening of an account and the
establishment of an investment plan.
Usage
The AccountOpeningInstruction is used to open an account directly or indirectly with the account
servicer or an intermediary.
In some markets, for example, Australia, and for some products in the United Kingdom, a first order
(also known as a deposit instruction) is placed at the same time as the account opening. To cater for
this scenario, an order message can be linked (via references in the message) to the
AccountOpeningInstruction message when needed.
Execution of the AccountOpeningInstruction is confirmed via an AccountDetailsConfirmation message.
Outline
The AccountOpeningInstructionV08 MessageDefinition is composed of 16 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. OrderReference
Identifies a related order or settlement transaction.
C. PreviousReference
Reference to a linked message that was previously sent.
D. InstructionDetails
Information about the opening instruction.
E. InvestmentAccount
Detailed information about the account to be opened.
F. AccountParties
Information related to parties that are related to the account, for example, primary account owner.
G. Intermediaries
Intermediary or other party related to the management of the account.
H. Placement
Referral information.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 20 May 2026
```

## File page 21

```text
I. NewIssueAllocation
Eligibility conditions applicable when there is an allocation of new issues for hedge fund account
opening.
J. SavingsInvestmentPlan
Plan that allows individuals to set aside a fixed amount of money at specified intervals, usually for a
special purpose, for example, retirement.
K. WithdrawalInvestmentPlan
Plan through which holdings are depleted through regular withdrawals at specified intervals.
L. CashSettlement
Cash settlement standing instruction associated to transactions on the account.
M. ServiceLevelAgreement
Identifies documents to be provided for the account opening.
N. AdditionalInformation
Additional information such as remarks or notes that must be conveyed about the account
management activity and or any limitations and restrictions.
O. MarketPracticeVersion
Identifies the market practice to which the message conforms.
P. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 21 May 2026
```

