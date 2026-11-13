---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.9 PutableDate <PutblDt>"]
file_pages: [204]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.9 PutableDate <PutblDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 204 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 204

```text
13.1.2.3.9  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date at which the holder has the right to ask for redemption of the security prior to final
maturity.
Datatype: "ISODateTime" on page 529
13.1.2.3.10  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Next date/time at which the issuer has the right to pay the securitiy prior to maturity.
Datatype: "ISODateTime" on page 529
13.1.2.3.11  NextFactorDate <NxtFctrDt>
Presence: [0..1]
Definition: The date that the current factor will be changed to a new factor.
Datatype: "ISODateTime" on page 529
13.1.2.3.12  ExpirationDate <XprtnDt>
Presence: [0..1]
Definition: Date/time at which an interest bearing security becomes due and assets are to be repaid.
Datatype: "ISODateTime" on page 529
13.1.2.3.13  PaymentDirectionIndicator <PmtDrctnInd>
Presence: [0..1]
Definition: Indicates the direction of payment for asset or mortgage backed securities, ie, whether the
repaid capital is distributed (payment direction is down) or capitalized (payment direction is up).
Datatype: One of the following values must be used (see "PaymentDirectionIndicator" on page 531):
• Meaning When True: Up
• Meaning When False: Down
13.1.2.3.14  InterestRate <IntrstRate>
Presence: [0..1]
Definition: Per annum ratio of interest paid to the principal amount of the financial instrument for a
specific period of time.
Datatype: "PercentageRate" on page 532
13.1.2.3.15  NextInterestRate <NxtIntrstRate>
Presence: [0..1]
Definition: Specifies the interest rate applicable to the next interest payment period.
Datatype: "PercentageRate" on page 532
13.1.2.3.16  OddCouponIndicator <OddCpnInd>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 204 March 2024
```

