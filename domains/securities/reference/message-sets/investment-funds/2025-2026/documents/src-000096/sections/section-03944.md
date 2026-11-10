---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.4 Tax38"]
file_pages: [5237]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.4 Tax38

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5237 to 5237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5237

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.47.4  Tax38
Definition: Tax related to an investment fund order.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5237
{Or     Code <Cd> [1..1] CodeSet 5238
Or}     Proprietary <Prtry> [1..1] ± 5238
   Basis <Bsis> [0..1]  5239
{Or     Code <Cd> [1..1] CodeSet 5239
Or}     Proprietary <Prtry> [1..1] ± 5239
   Amount <Amt> [1..1] Amount C1, C13 5239
   Country <Ctry> [0..1] CodeSet C12 5240
   ExemptionIndicator <XmptnInd> [1..1] Indicator 5240
   ExemptionReason <XmptnRsn> [0..1]  5240
{Or     Code <Cd> [1..1] CodeSet 5241
Or}     Proprietary <Prtry> [1..1] ± 5243
   RecipientIdentification <RcptId> [0..1] ± 5244
   TaxCalculationDetails <TaxClctnDtls> [0..1]  5244
     Basis <Bsis> [0..1]  5244
{Or       Code <Cd> [1..1] CodeSet 5245
Or}       Proprietary <Prtry> [1..1] ± 5245
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5245
66.1.47.4.1  Type <Tp>
Presence: [1..1]
Definition: Type of tax.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5237 May 2026
```

