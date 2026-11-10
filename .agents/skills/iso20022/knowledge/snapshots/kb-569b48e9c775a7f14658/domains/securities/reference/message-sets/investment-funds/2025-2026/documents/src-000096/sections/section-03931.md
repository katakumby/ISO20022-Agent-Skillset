---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.1 TaxableIncomePerDividend <TaxblIncmPerDvdd>"]
file_pages: [5223]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.1 TaxableIncomePerDividend <TaxblIncmPerDvdd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5223 to 5223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5223

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C1, C13 5223
   EUCapitalGain <EUCptlGn> [0..1]  5224
{Or     Code <Cd> [1..1] CodeSet 5224
Or}     Proprietary <Prtry> [1..1] ± 5224
   EUDividendStatus <EUDvddSts> [0..1]  5225
{Or     Code <Cd> [1..1] CodeSet 5225
Or}     Proprietary <Prtry> [1..1] ± 5225
   PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 5226
   IndividualTax <IndvTax> [0..*]  5226
     Type <Tp> [1..1]  5226
{Or       Code <Cd> [1..1] CodeSet 5227
Or}       Proprietary <Prtry> [1..1] ± 5228
     InformativeAmount <InftvAmt> [0..1] Amount C1, C13 5228
     InformativeRate <InftvRate> [0..1] Rate 5229
     Country <Ctry> [0..1] CodeSet C12 5229
     ExemptionIndicator <XmptnInd> [1..1] Indicator 5229
     ExemptionReason <XmptnRsn> [0..1]  5229
{Or       Code <Cd> [1..1] CodeSet 5230
Or}       Proprietary <Prtry> [1..1] ± 5232
     RecipientIdentification <RcptId> [0..1] ± 5233
     TaxCalculationDetails <TaxClctnDtls> [0..1]  5233
       Basis <Bsis> [0..1]  5233
{Or         Code <Cd> [1..1] CodeSet 5234
Or}         Proprietary <Prtry> [1..1] ± 5234
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5234
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
66.1.47.2.1  TaxableIncomePerDividend <TaxblIncmPerDvdd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5223 May 2026
```

