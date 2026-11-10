---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02"]
file_pages: [198, 199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
---

# 12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 198 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
12 camt.074.001.02
IntraBalanceMovementCancellationRequestV
02
12.1 MessageDefinition Functionality
The IntraBalanceMovementCancellationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the cancellation of a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementCancellationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. UnderlyingIntraBalance
Intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 198 August 2026
```

## File page 199

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 199 August 2026
```

