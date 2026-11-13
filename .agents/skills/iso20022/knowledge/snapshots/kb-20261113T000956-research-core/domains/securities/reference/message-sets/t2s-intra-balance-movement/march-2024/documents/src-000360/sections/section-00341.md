---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.10 Financial Instrument Quantity", "17.1.10.1 FinancialInstrumentQuantity1Choice", "17.1.10.1.1 Unit <Unit>"]
file_pages: [407]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.10.1.1 Unit <Unit>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 407 to 407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 407

```text
17.1.10.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 495
17.1.10.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.10.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.11 Frequency
17.1.11.1  Frequency22Choice
Definition: Choice of format for a frequency, for example, the frequency of delivery of a statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 407
Or}   Proprietary <Prtry> [1..1] ± 408
17.1.11.1.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency7Code" on page 479
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
ADHO Adhoc Event takes place as necessary.
MNTH Monthly Event takes place every month or once a
month.
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
WEEK Weekly Event takes place once a week.
SEMI SemiAnnual Event takes place every six months or
two times a year.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
407 March 2024
```

