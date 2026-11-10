---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.7 SubBalance <SubBal>", "15.4.7.2 Movement <Mvmnt>", "15.4.7.2.9 PreviouslySettledAmount <PrevslySttldAmt>"]
file_pages: [352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.7.2.9 PreviouslySettledAmount <PrevslySttldAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 352 to 352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
SettledAmount <SttldAmt> contains one of the following elements (see "Amount2Choice" on
page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
15.4.7.2.9  PreviouslySettledAmount <PrevslySttldAmt>
Presence: [0..1]
Definition: Amount of money previously settled.
PreviouslySettledAmount <PrevslySttldAmt> contains one of the following elements (see
"Amount2Choice" on page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
15.4.7.2.10  RemainingSettlementAmount <RmngSttlmAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingSettlementAmount <RmngSttlmAmt> contains one of the following elements (see
"Amount2Choice" on page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
15.4.7.2.11  EffectiveSettlementDate <FctvSttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is moved.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
15.4.7.2.12  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
352 March 2024
```

