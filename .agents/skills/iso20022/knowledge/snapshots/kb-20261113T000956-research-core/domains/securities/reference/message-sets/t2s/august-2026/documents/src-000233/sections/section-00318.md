---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.11 MovementDetails <MvmntDtls>", "17.4.4.1.5.11.5 PreviouslySettledAmount <PrevslySttldAmt>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.11.5 PreviouslySettledAmount <PrevslySttldAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
SettledAmount <SttldAmt> contains one of the following elements (see "Amount2Choice" on
page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
17.4.4.1.5.11.5  PreviouslySettledAmount <PrevslySttldAmt>
Presence: [0..1]
Definition: Amount of money previously settled.
PreviouslySettledAmount <PrevslySttldAmt> contains one of the following elements (see
"Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
17.4.4.1.5.11.6  RemainingSettlementAmount <RmngSttlmAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingSettlementAmount <RmngSttlmAmt> contains one of the following elements (see
"Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
17.4.4.1.5.11.7  IntendedSettlementDate <IntnddSttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is intended to be moved.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
17.4.4.1.5.11.8  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the amount of money is moved.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 415 August 2026
```

