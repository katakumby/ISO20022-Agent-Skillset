---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.5 Financial Instrument Quantity", "4.1.5.1 FinancialInstrumentQuantity1Choice", "4.1.5.1.1 Unit <Unit>"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.5.1.1 Unit <Unit>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 55
Or   FaceAmount <FaceAmt> [1..1] Amount 55
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 55
4.1.5.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 81
4.1.5.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 74
4.1.5.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 74
4.1.6 Identification Information
4.1.6.1  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 55
   SchemeName <SchmeNm> [0..1] Text 55
   Issuer <Issr> [0..1] Text 56
4.1.6.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 83
4.1.6.1.2  SchemeName <SchmeNm>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
55 March 2024
```

