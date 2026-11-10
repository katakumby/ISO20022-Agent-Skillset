---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.59 IdentificationReference16Choice", "7.1.19.59.9 SecondaryAllocationIdentification <ScndryAllcnId>"]
file_pages: [386]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.59.9 SecondaryAllocationIdentification <ScndryAllcnId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 386 to 386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 386

```text
7.1.19.59.9  SecondaryAllocationIdentification <ScndryAllcnId>
Presence: [1..1]
Definition: Reference that can be shared across a number of allocation instruction or allocation report
messages, thereby making it possible to pass an identifier for an original allocation message on multiple
messages (for example from one party to a second to a third, across cancel and replace messages
etc).
Datatype: "Max35Text" on page 669
7.1.19.59.10  IndexIdentification <IndxId>
Presence: [1..1]
Definition: Reference identifying a index trade.
Datatype: "Max35Text" on page 669
7.1.19.59.11  CommonIdentification <CmonId>
Presence: [1..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 669
7.1.19.59.12  ComplianceIdentification <CmplcId>
Presence: [1..1]
Definition: Identification used to represent this transaction for compliance purposes.
Datatype: "Max35Text" on page 669
7.1.19.59.13  CancellationRequestIdentification <CxlReqId>
Presence: [1..1]
Definition: Unambiguous identification of the cancellation request as known by the instructing party.
Datatype: "Max35Text" on page 669
7.1.19.59.14  CollateralTransactionIdentification <CollTxId>
Presence: [1..1]
Definition: Unambiguous identification of a collateral transaction as assigned by the instructing party.
Datatype: "Max35Text" on page 669
7.1.19.59.15  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 665
7.1.19.60  IdentificationReference15Choice
Definition: Unique identifier of a document, message or transaction.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 386 February 2025
```

