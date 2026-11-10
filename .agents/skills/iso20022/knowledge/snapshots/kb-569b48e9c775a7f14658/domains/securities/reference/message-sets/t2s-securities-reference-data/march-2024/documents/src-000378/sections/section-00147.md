---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.33 CapitalisedInterest <CptlsdIntrst>", "13.1.2.3.33.1 Code <Cd>"]
file_pages: [209]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.33.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 209 to 209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 209

```text
Definition: Specifies whether the interest amount is capitalised until maturity date or paid out at each
interest payment date.
CapitalisedInterest <CptlsdIntrst> contains one of the following DistributionPolicy2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 209
Or}   Proprietary <Prtry> [1..1] ± 209
13.1.2.3.33.1  Code <Cd>
Presence: [1..1]
Definition: Distribution policy expressed as an ISO 20022 code.
Datatype: "DistributionPolicy1Code" on page 513
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
13.1.2.3.33.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Distribution policy expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.3.34  ActualDenominationAmount <ActlDnmtnAmt>
Presence: [0..*]
Definition: Nominal value per security unit.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 209 March 2024
```

