---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.35 WithholdingTaxRegime <WhldgTaxRgm>", "32.4.3.1.1.3.35.2 Country <Ctry>"]
file_pages: [1991]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.35.2 Country <Ctry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1991 to 1991.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1991

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
32.4.3.1.1.3.35.2  Country <Ctry>
Presence: [1..1]
Definition: Represents the tax authority.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
32.4.3.1.1.3.36  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 3166 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3167
Or}   Proprietary <Prtry> [1..1] ± 3167
32.4.3.1.1.3.37  InitialPhysicalForm <InitlPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities on the closing date.
InitialPhysicalForm <InitlPhysForm> contains one of the following InitialPhysicalForm4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1992
Or}   Proprietary <Prtry> [1..1] ± 1992
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1991 August 2026
```

