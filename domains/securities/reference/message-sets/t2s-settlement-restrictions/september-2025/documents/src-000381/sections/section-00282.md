---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.37 RejectionReason34Code"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.37 RejectionReason34Code

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
CodeName Name Definition
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
9.2.2.37  RejectionReason34Code
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
OTHR Other Other. See Narrative.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 335 September 2025
```

