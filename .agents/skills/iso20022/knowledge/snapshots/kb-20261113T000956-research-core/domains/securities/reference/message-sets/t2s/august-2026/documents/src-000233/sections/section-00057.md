---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["7 camt.066.001.02 IntraBalanceMovementInstructionV02"]
file_pages: [93, 94]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 7 camt.066.001.02 IntraBalanceMovementInstructionV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 93 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 93

```text
7 camt.066.001.02
IntraBalanceMovementInstructionV02
7.1 MessageDefinition Functionality
The IntraBalanceMovementInstruction message is sent from an account owner/requestor to a
settlement infrastructure to instruct the movement of an amount of money within its holdings from one
sub-balance to another.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementInstructionV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. CorporateActionEventIdentification
Identification assigned by the account servicer to unambiguously identify a corporate action event.
C. NumberCounts
Count of the number of transactions linked.
D. Linkages
Link to another transaction that must be processed after, before or at the same time.
E. CashAccount
Account to or from which an entry is made.
F. CashAccountOwner
Party that legally owns the cash account.
G. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
H. IntraBalance
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities 93 August 2026
```

## File page 94

```text
Intra-balance movement transaction details.
I. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities 94 August 2026
```

