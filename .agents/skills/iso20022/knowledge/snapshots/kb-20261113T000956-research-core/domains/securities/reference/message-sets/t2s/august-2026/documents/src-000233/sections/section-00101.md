---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.4 Message Building Blocks", "9.4.6 IntraBalance <IntraBal>", "9.4.6.2 PreviouslySettledAmount <PrevslySttldAmt>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.4.6.2 PreviouslySettledAmount <PrevslySttldAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
SettledAmount <SttldAmt> contains one of the following elements (see "Amount2Choice" on
page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
9.4.6.2  PreviouslySettledAmount <PrevslySttldAmt>
Presence: [0..1]
Definition: Amount of money previously settled.
PreviouslySettledAmount <PrevslySttldAmt> contains one of the following elements (see
"Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
9.4.6.3  RemainingSettlementAmount <RmngSttlmAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingSettlementAmount <RmngSttlmAmt> contains one of the following elements (see
"Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
9.4.6.4  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
9.4.6.5  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 142 August 2026
```

