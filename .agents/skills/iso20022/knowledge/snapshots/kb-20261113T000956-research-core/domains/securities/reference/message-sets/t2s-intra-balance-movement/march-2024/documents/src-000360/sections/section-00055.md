---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 camt.072.001.02 IntraBalanceMovementModificationRequestV02"]
file_pages: [66, 67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 66 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
5 camt.072.001.02
IntraBalanceMovementModificationRequestV
02
5.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
66 March 2024
```

## File page 67

```text
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
67 March 2024
```

