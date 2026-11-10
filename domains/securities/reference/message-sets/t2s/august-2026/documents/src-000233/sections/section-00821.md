---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.3 PaymentFrequency <PmtFrqcy>"]
file_pages: [1226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.3 PaymentFrequency <PmtFrqcy>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1226 to 1226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1226

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.1.2.1.3.3  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency35Choice"
on page 2960 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2960
Or}   Proprietary <Prtry> [1..1] ± 2960
28.4.2.1.2.1.3.4  InterestFixingDate <IntrstFxgDt>
Presence: [0..1]
Definition: Date/time at which the rate determination is made, also called determination date.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.5  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date/time at which a security begins to accrue interest.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.6  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date/time at which the first interest payment is due to holders of the security.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.7  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.8  NextCouponDate <NxtCpnDt>
Presence: [0..1]
Definition: Date of the coupon attached to the physical security.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1226 August 2026
```

