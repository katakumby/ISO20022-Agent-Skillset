---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.129 RejectionReason34Code"]
file_pages: [3284]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.129 RejectionReason34Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3284 to 3284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3284

```text
CodeName Name Definition
CASH CashAccount Unrecognised or invalid cash account.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
DMON SettlementAmountRejection Unrecognised or invalid settlement
amount.
NCRR SettlementAmountCurrencyRejection Unrecognised or invalid settlement
amount currency.
LATE MarketDeadlineMissed Received after market deadline.
INVL InvalidLink Invalid or unrecognized link.
INVB InvalidBalance Instruction aims at using an invalid
balance.
INVN InvalidLotNumber Invalid or unrecognized lot number.
VALR InvalidRule Account servicer validation rule rejection.
MONY InsufficientMoney Insufficient money in your account.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
OTHR Other Other. See Narrative.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
82.2.2.129  RejectionReason34Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
LATE MarketDeadlineMissed Received after market deadline.
CASH CashAccount Unrecognised or invalid cash account.
NRGM NoMatch More than one instruction match the
criteria.
NRGN NotFoundRejection Instruction could not be found.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3284 August 2026
```

