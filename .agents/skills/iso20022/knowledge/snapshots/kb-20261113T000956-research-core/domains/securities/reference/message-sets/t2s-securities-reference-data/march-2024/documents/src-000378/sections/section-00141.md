---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.3 PaymentFrequency <PmtFrqcy>"]
file_pages: [203]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.3 PaymentFrequency <PmtFrqcy>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 203 to 203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 203

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.3.3  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency35Choice"
on page 477 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 477
Or}   Proprietary <Prtry> [1..1] ± 477
13.1.2.3.4  InterestFixingDate <IntrstFxgDt>
Presence: [0..1]
Definition: Date/time at which the rate determination is made, also called determination date.
Datatype: "ISODateTime" on page 529
13.1.2.3.5  DatedDate <DtdDt>
Presence: [0..1]
Definition: First date/time at which a security begins to accrue interest.
Datatype: "ISODateTime" on page 529
13.1.2.3.6  FirstPaymentDate <FrstPmtDt>
Presence: [0..1]
Definition: Date/time at which the first interest payment is due to holders of the security.
Datatype: "ISODateTime" on page 529
13.1.2.3.7  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: "ISODateTime" on page 529
13.1.2.3.8  NextCouponDate <NxtCpnDt>
Presence: [0..1]
Definition: Date of the coupon attached to the physical security.
Datatype: "ISODateTime" on page 529
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 203 March 2024
```

