---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02"]
file_pages: [149, 150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10 camt.072.001.02 IntraBalanceMovementModificationRequestV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 149 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
10 camt.072.001.02
IntraBalanceMovementModificationRequestV
02
10.1 MessageDefinition Functionality
The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the modification of a processing indicator on a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementModificationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. CashAccount
Account to or from which an entry is made.
C. CashAccountOwner
Party that legally owns the cash account.
D. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
E. RequestDetails
Details of the request providing the changes and references of the instruction for which the
modification is requested.
F. UnderlyingIntraBalance
Original intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 149 August 2026
```

## File page 150

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 150 August 2026
```

