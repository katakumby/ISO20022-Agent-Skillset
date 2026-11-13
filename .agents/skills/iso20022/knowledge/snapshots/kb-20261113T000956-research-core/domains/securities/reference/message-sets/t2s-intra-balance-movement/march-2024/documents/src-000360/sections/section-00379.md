---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.16 RejectionOrRepairStatus38Choice", "17.1.16.16.2 Reason <Rsn>", "17.1.16.16.2.1 Code <Cd>"]
file_pages: [445]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.16.2.1 Code <Cd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 445 to 445.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
Reason <Rsn> contains the following RejectionOrRepairReason32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..*]  445
{Or     Code <Cd> [1..1] CodeSet 445
Or}     Proprietary <Prtry> [1..1] ± 446
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
17.1.16.16.2.1  Code <Cd>
Presence: [0..*]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason32Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 445
Or}   Proprietary <Prtry> [1..1] ± 446
17.1.16.16.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason33Code" on page 490
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
445 March 2024
```

