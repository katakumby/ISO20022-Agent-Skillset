---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.2.2.37 WithholdingTaxRegime <WhldgTaxRgm>", "28.4.2.2.2.37.2 Country <Ctry>"]
file_pages: [1712]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.2.37.2 Country <Ctry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1712 to 1712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1712

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
28.4.2.2.2.37.2  Country <Ctry>
Presence: [1..1]
Definition: Represents the tax authority.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
28.4.2.2.2.38  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 3166 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3167
Or}   Proprietary <Prtry> [1..1] ± 3167
28.4.2.2.2.39  InitialPhysicalForm <InitlPhysForm>
Presence: [0..1]
Definition: Indicates the physical form of the securities on the closing date.
InitialPhysicalForm <InitlPhysForm> contains one of the following InitialPhysicalForm4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1713
Or}   Proprietary <Prtry> [1..1] ± 1713
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1712 August 2026
```

