---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.16 RejectionOrRepairStatus38Choice", "82.1.30.16.2 Reason <Rsn>", "82.1.30.16.2.1 Code <Cd>"]
file_pages: [3148]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.16.2.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3148 to 3148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3148

```text
Reason <Rsn> contains the following RejectionOrRepairReason32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..*]  3148
{Or     Code <Cd> [1..1] CodeSet 3148
Or}     Proprietary <Prtry> [1..1] ± 3149
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3149
82.1.30.16.2.1  Code <Cd>
Presence: [0..*]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason32Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3148
Or}   Proprietary <Prtry> [1..1] ± 3149
82.1.30.16.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason33Code" on page 3283
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3148 August 2026
```

