---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.42 PoolsPerTrade <PlsPerTrad>"]
file_pages: [686]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.42 PoolsPerTrade <PlsPerTrad>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 686 to 686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 686

```text
Definition: Indicates per lot the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
27.4.2.2.3.42  PoolsPerTrade <PlsPerTrad>
Presence: [0..1]
Definition: Indicates per trade the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
27.4.2.2.3.43  ConstantPrePaymentPenaltyIndicator <CstPrePmtPnltyInd>
Presence: [0..1]
Definition: Indicates whether a penalty might be imposed to the borrower of a mortgage in case of
prepayments occurring during the lockout period.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.44  LotIdentification <LotId>
Presence: [0..1]
Definition: Identifies the lot constituting an asset backed or mortgage backed security issue.
Datatype: "Max35Text" on page 3328
27.4.2.2.3.45  ConstantPrePaymentYield <CstPrePmtYld>
Presence: [0..1]
Definition: Measure of prepayment as a yield of the current outstanding loan balance.
Datatype: "PercentageRate" on page 3325
27.4.2.2.3.46  WeightedAverageCoupon <WghtdAvrgCpn>
Presence: [0..1]
Definition: Contains the weighted average coupon of the fixed income instrument (expressed as a
percentage).
Datatype: "PercentageRate" on page 3325
27.4.2.2.3.47  WeightedAverageLife <WghtdAvrgLife>
Presence: [0..1]
Definition: Contains the weighted average life of the fixed income instrument (expressed in months).
Datatype: "DecimalNumber" on page 3324
27.4.2.2.3.48  WeightedAverageLoan <WghtdAvrgLn>
Presence: [0..1]
Definition: Contains the weighted average loan of the fixed income instrument (expressed in months).
Datatype: "DecimalNumber" on page 3324
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 686 August 2026
```

