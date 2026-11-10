---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02"]
file_pages: [173, 174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 173 to 174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
11 camt.073.001.02
IntraBalanceMovementModificationRequestSt
atusAdviceV02
11.1 MessageDefinition Functionality
The IntraBalanceMovementModificationRequestStatusAdvice message is sent from a settlement
infrastructure to an account owner/requestor to advise the status of an intra-balance movement
modification request previously sent by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementModificationRequestStatusAdviceV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. RequestReference
Reference of the original intra-balance movement modification request.
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. RequestDetails
Details of the request providing the changes and references of the instruction for which the
modification is requested.
G. ProcessingStatus
Provides details on the processing status of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 173 August 2026
```

## File page 174

```text
H. UnderlyingIntraBalance
Intra-balance movement transaction details.
I. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 174 August 2026
```

