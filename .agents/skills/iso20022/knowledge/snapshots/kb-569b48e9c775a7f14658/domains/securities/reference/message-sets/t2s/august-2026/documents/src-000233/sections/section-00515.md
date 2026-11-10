---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.9 PutableDate <PutblDt>"]
file_pages: [679]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.9 PutableDate <PutblDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 679 to 679.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 679

```text
27.4.2.2.3.9  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODateTime" on page 3320
27.4.2.2.3.10  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date/time at which the issuer has the right to pay the securitiy prior to maturity.
Datatype: "ISODateTime" on page 3320
27.4.2.2.3.11  NextFactorDate <NxtFctrDt>
Presence: [0..1]
Definition: The date that the current factor will be changed to a new factor.
Datatype: "ISODateTime" on page 3320
27.4.2.2.3.12  ExpirationDate <XprtnDt>
Presence: [0..1]
Definition: Date/time at which an interest bearing security becomes due and assets are to be repaid.
Datatype: "ISODateTime" on page 3320
27.4.2.2.3.13  PaymentDirectionIndicator <PmtDrctnInd>
Presence: [0..1]
Definition: Indicates the direction of payment for asset or mortgage backed securities, ie, whether the
repaid capital is distributed (payment direction is down) or capitalized (payment direction is up).
Datatype: One of the following values must be used (see "PaymentDirectionIndicator" on page 3323):
• Meaning When True: Up
• Meaning When False: Down
27.4.2.2.3.14  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 3325
27.4.2.2.3.15  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Specifies the interest rate applicable to the next interest payment period.
Datatype: "PercentageRate" on page 3325
27.4.2.2.3.16  OddCouponIndicator <OddCpnInd>
Presence: [0..1]
Definition: Specifies whether the payment of the coupon (interest) on a bond is off the normal schedule.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 679 August 2026
```

