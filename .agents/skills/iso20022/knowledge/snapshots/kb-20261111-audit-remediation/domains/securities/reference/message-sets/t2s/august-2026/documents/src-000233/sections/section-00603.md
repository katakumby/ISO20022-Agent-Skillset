---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.37 WithholdingTaxRegime <WhldgTaxRgm>", "27.4.2.3.37.2 Country <Ctry>"]
file_pages: [788]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.37.2 Country <Ctry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 788 to 788.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 788

```text
WithholdingTaxValue <WhldgTaxVal> contains one of the following elements (see
"RateAndAmountFormat1Choice" on page 3004 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3004
Or   Amount <Amt> [1..1] Amount C1, C4 3005
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1]  3005
{Or     Code <Cd> [1..1] CodeSet 3005
Or}     Proprietary <Prtry> [1..1] ± 3005
27.4.2.3.37.2  Country <Ctry>
Presence: [1..1]
Definition: Represents the tax authority.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
27.4.2.3.38  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 3166 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3167
Or}   Proprietary <Prtry> [1..1] ± 3167
27.4.2.3.39  InitialPhysicalForm <InitlPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities on the closing date.
InitialPhysicalForm <InitlPhysForm> contains one of the following InitialPhysicalForm4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 789
Or}   Proprietary <Prtry> [1..1] ± 789
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 788 August 2026
```

