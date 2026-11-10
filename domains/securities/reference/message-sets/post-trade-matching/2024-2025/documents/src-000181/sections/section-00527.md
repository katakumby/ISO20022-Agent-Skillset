---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.29 Transaction Type"]
file_pages: [605]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.29 Transaction Type

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 605 to 605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 605

```text
7.1.29 Transaction Type
7.1.29.1  SettlementTransactionCondition31Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 605
Or}   Proprietary <Prtry> [1..1] ± 606
7.1.29.1.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition7Code" on page 647
CodeName Name Definition
ASGN Assignment Transfer of ownership of the asset to
another party during the closing of an
option.
CLEN Clean Indicates that the trade was executed
clean, ie government tax must not be
paid on the accrued interest on the bond.
DIRT Dirty Indicates that the trade was executed
dirty, ie government tax must be paid on
the accrued interest on the bond.
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DRAW Drawn Settlement transactions relates to drawn
securities.
EXER Exercised Settlement transaction relates to options,
futures or derivatives that are exercised.
FRCL FreeCleanSettlement Delivery will be made free of payment
but a clean payment order will be sent.
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
PHYS Physical Securities are to be physically settled.
CSDP CSDPaymentOnly Transaction on a security that is not
eligible at the Central Securities
Depository (CSD) but for which the
payment will be enacted by the CSD.
SPCS SplitCurrencySettlement Settlement is in two different currencies.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 605 February 2025
```

