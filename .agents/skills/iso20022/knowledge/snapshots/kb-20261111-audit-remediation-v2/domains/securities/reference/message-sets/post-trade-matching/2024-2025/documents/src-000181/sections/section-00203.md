---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.2 CommissionType6Choice", "7.1.8.2.2 Proprietary <Prtry>"]
file_pages: [257]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.2.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 257 to 257.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 257

```text
7.1.8.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Commission type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.8.3  Commission24
Definition: Amount of money due to a party as compensation for a service.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 257
   Commission <Comssn> [1..1] ± 257
   RecipientIdentification <RcptId> [0..1] ± 258
   CalculationDate <ClctnDt> [0..1] Date 258
   TotalCommission <TtlComssn> [0..1] ± 258
   TotalVATAmount <TtlVATAmt> [0..1] Amount C1, C9 259
   VATRate <VATRate> [0..1] Rate 259
7.1.8.3.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the commission type.
Type <Tp> contains one of the following elements (see "CommissionType6Choice" on page 255 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 255
Or}   Proprietary <Prtry> [1..1] ± 257
7.1.8.3.2  Commission <Comssn>
Presence: [1..1]
Definition: Amount of money due to a party as compensation for a service.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 257 February 2025
```

