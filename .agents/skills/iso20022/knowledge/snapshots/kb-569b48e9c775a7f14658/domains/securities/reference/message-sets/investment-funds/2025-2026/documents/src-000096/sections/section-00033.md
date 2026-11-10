---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08"]
file_pages: [57, 58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4 acmt.003.001.08 AccountModificationInstructionV08

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 57 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
4 acmt.003.001.08
AccountModificationInstructionV08
4.1 MessageDefinition Functionality
Scope
The AccountModificationInstruction message is sent by an account owner, for example, an investor or
its designated agent to the account servicer, for example, a registrar, transfer agent, custodian bank or
securities depository to modify, that is, create, update or delete specific details of an existing account.
Usage
The AccountModificationInstruction message is used to modify the details of an existing account.
The AccountModificationInstruction message can be used to:
- maintain/update any of the existing account details, for example, to update the address of the
beneficiary or modify the preference to income from distribution to capitalisation, or,
- add/create specific details to the existing account when these details were not yet recorded at the time
of account creation, for example, to add a second address or to establish new cash settlement standing
instructions, or,
- delete specific account details, for example, delete cash standing instructions, or,
- instruct a change to the status of the account, for example, instruct the closure of the account.
The usage of this message may be subject to service level agreement (SLA) between the
counterparties.
Execution of the AccountModificationInstruction is confirmed via an AccountDetailsConfirmation
message.
Outline
The AccountModificationInstructionV08 MessageDefinition is composed of 16 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. InstructionDetails
Information about the modification instruction.
D. InvestmentAccountSelection
Identifies the account for which the information is modified.
E. ModifiedInvestmentAccount
Information related to general characteristics of the account to be inserted, updated or deleted.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 57 May 2026
```

## File page 58

```text
F. ModifiedAccountParties
Information related to an account party to be inserted, updated or deleted.
G. ModifiedIntermediaries
Information related to intermediaries to be inserted, updated or deleted.
H. ModifiedPlacement
Information related to referral information to be inserted, updated or deleted.
I. ModifiedIssueAllocation
Eligibility conditions related to allocation of new issues to be inserted, updated or deleted.
J. ModifiedSavingsInvestmentPlan
Information related to a savings plan to be inserted, updated or deleted.
K. ModifiedWithdrawalInvestmentPlan
Information related to a withdrawal plan to be inserted, updated or deleted.
L. ModifiedCashSettlement
Cash settlement standing instruction to be either inserted or deleted.
M. ModifiedServiceLevelAgreement
Information related to documents to be added, deleted or updated.
N. ModifiedAdditionalInformation
Information related to additional information to be added, deleted or updated.
O. MarketPracticeVersion
Identifies the market practice to which the message conforms.
P. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 58 May 2026
```

