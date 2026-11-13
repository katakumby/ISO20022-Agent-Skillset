---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02"]
file_pages: [114, 115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 114 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 114

```text
8 camt.067.001.02
IntraBalanceMovementStatusAdviceV02
8.1 MessageDefinition Functionality
The IntraBalanceMovementStatusAdvice message is sent from a settlement infrastructure to an
account owner/requestor to advise the status of an intra-balance movement instruction previously sent
by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementStatusAdviceV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. SettlementStatus
Provides the settlement status of a transaction.
E. CashAccount
Account to or from which an entry is made.
F. CashAccountOwner
Party that legally owns the cash account.
G. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
H. UnderlyingIntraBalance
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 114 August 2026
```

## File page 115

```text
Intra-balance movement transaction details.
I. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 115 August 2026
```

