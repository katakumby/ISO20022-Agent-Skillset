---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.4 PercentageOfDebtClaim <PctgOfDebtClm>"]
file_pages: [5226]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.4 PercentageOfDebtClaim <PctgOfDebtClm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5226 to 5226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5226

```text
66.1.47.2.4  PercentageOfDebtClaim <PctgOfDebtClm>
Presence: [0..1]
Definition: Percentage of the underlying assets of the funds that represents a debt and is in the scope of
the European directive on taxation of savings income in the form of interest payments (Council Directive
2003/48/EC 3 June).
Datatype: "PercentageRate" on page 5401
66.1.47.2.5  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Information related to a specific tax that is provided for information purposes.
IndividualTax <IndvTax> contains the following Tax40 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5226
{Or     Code <Cd> [1..1] CodeSet 5227
Or}     Proprietary <Prtry> [1..1] ± 5228
   InformativeAmount <InftvAmt> [0..1] Amount C1, C13 5228
   InformativeRate <InftvRate> [0..1] Rate 5229
   Country <Ctry> [0..1] CodeSet C12 5229
   ExemptionIndicator <XmptnInd> [1..1] Indicator 5229
   ExemptionReason <XmptnRsn> [0..1]  5229
{Or     Code <Cd> [1..1] CodeSet 5230
Or}     Proprietary <Prtry> [1..1] ± 5232
   RecipientIdentification <RcptId> [0..1] ± 5233
   TaxCalculationDetails <TaxClctnDtls> [0..1]  5233
     Basis <Bsis> [0..1]  5233
{Or       Code <Cd> [1..1] CodeSet 5234
Or}       Proprietary <Prtry> [1..1] ± 5234
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5234
66.1.47.2.5.1  Type <Tp>
Presence: [1..1]
Definition: Type of tax applied.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5226 May 2026
```

