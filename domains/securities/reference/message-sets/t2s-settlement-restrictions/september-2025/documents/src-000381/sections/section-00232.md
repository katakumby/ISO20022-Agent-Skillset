---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.11 RejectionOrRepairStatus38Choice", "9.1.21.11.2 Reason <Rsn>", "9.1.21.11.2.1 Code <Cd>"]
file_pages: [278]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.11.2.1 Code <Cd>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 278 to 278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 278

```text
Reason <Rsn> contains the following RejectionOrRepairReason32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..*]  278
{Or     Code <Cd> [1..1] CodeSet 278
Or}     Proprietary <Prtry> [1..1] ± 279
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 279
9.1.21.11.2.1  Code <Cd>
Presence: [0..*]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason32Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 278
Or}   Proprietary <Prtry> [1..1] ± 279
9.1.21.11.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason33Code" on page 334
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
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 278 September 2025
```

