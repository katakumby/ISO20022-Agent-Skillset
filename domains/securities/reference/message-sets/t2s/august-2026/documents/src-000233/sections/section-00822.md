---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.9 PutableDate <PutblDt>"]
file_pages: [1227]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.9 PutableDate <PutblDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1227 to 1227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1227

```text
28.4.2.1.2.1.3.9  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.10  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date/time at which the issuer has the right to pay the securitiy prior to maturity.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.11  NextFactorDate <NxtFctrDt>
Presence: [0..1]
Definition: The date that the current factor will be changed to a new factor.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.12  ExpirationDate <XprtnDt>
Presence: [0..1]
Definition: Date/time at which an interest bearing security becomes due and assets are to be repaid.
Datatype: "ISODateTime" on page 3320
28.4.2.1.2.1.3.13  PaymentDirectionIndicator <PmtDrctnInd>
Presence: [0..1]
Definition: Indicates the direction of payment for asset or mortgage backed securities, ie, whether the
repaid capital is distributed (payment direction is down) or capitalized (payment direction is up).
Datatype: One of the following values must be used (see "PaymentDirectionIndicator" on page 3323):
• Meaning When True: Up
• Meaning When False: Down
28.4.2.1.2.1.3.14  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.3.15  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Specifies the interest rate applicable to the next interest payment period.
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.3.16  OddCouponIndicator <OddCpnInd>
Presence: [0..1]
Definition: Specifies whether the payment of the coupon (interest) on a bond is off the normal schedule.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1227 August 2026
```

