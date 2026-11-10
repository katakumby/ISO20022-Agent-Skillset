---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.3 PaymentFrequency <PmtFrqcy>"]
file_pages: [1880]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.3 PaymentFrequency <PmtFrqcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1880 to 1880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1880

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
32.4.3.1.1.2.3.3  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency35Choice"
on page 2960 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2960
Or}   Proprietary <Prtry> [1..1] ± 2960
32.4.3.1.1.2.3.4  InterestFixingDate <IntrstFxgDt>
Presence: [0..1]
Definition: Date/time at which the rate determination is made, also called determination date.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.5  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date/time at which a security begins to accrue interest.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.6  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date/time at which the first interest payment is due to holders of the security.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.7  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.3.8  NextCouponDate <NxtCpnDt>
Presence: [0..1]
Definition: Date of the coupon attached to the physical security.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1880 August 2026
```

