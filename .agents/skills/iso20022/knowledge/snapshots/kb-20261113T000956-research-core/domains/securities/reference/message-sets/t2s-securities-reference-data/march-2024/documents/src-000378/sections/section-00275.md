---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.35 WithholdingTaxRegime <WhldgTaxRgm>", "13.1.6.3.35.2 Country <Ctry>"]
file_pages: [360]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.35.2 Country <Ctry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 360 to 360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
WithholdingTaxValue <WhldgTaxVal> contains one of the following elements (see
"RateAndAmountFormat1Choice" on page 486 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 487
Or   Amount <Amt> [1..1] Amount C1, C5 487
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1]  487
{Or     Code <Cd> [1..1] CodeSet 487
Or}     Proprietary <Prtry> [1..1] ± 488
13.1.6.3.35.2  Country <Ctry>
Presence: [1..1]
Definition: Represents the tax authority.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.6.3.36  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 499 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 499
Or}   Proprietary <Prtry> [1..1] ± 500
13.1.6.3.37  InitialPhysicalForm <InitlPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities on the closing date.
InitialPhysicalForm <InitlPhysForm> contains one of the following InitialPhysicalForm4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 361
Or}   Proprietary <Prtry> [1..1] ± 361
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 360 March 2024
```

