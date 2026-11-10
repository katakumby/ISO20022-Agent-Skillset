---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.3 Debt <Debt>", "28.4.2.1.1.1.3.42 PoolsPerTrade <PlsPerTrad>"]
file_pages: [1046]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.3.42 PoolsPerTrade <PlsPerTrad>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1046 to 1046.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1046

```text
Definition: Indicates per lot the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.1.3.42  PoolsPerTrade <PlsPerTrad>
Presence: [0..1]
Definition: Indicates per trade the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.1.3.43  ConstantPrePaymentPenaltyIndicator <CstPrePmtPnltyInd>
Presence: [0..1]
Definition: Indicates whether a penalty might be imposed to the borrower of a mortgage in case of
prepayments occurring during the lockout period.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.1.1.3.44  LotIdentification <LotId>
Presence: [0..1]
Definition: Identifies the lot constituting an asset backed or mortgage backed security issue.
Datatype: "Max35Text" on page 3328
28.4.2.1.1.1.3.45  ConstantPrePaymentYield <CstPrePmtYld>
Presence: [0..1]
Definition: Measure of prepayment as a yield of the current outstanding loan balance.
Datatype: "PercentageRate" on page 3325
28.4.2.1.1.1.3.46  WeightedAverageCoupon <WghtdAvrgCpn>
Presence: [0..1]
Definition: Contains the weighted average coupon of the fixed income instrument (expressed as a
percentage).
Datatype: "PercentageRate" on page 3325
28.4.2.1.1.1.3.47  WeightedAverageLife <WghtdAvrgLife>
Presence: [0..1]
Definition: Contains the weighted average life of the fixed income instrument (expressed in months).
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.1.3.48  WeightedAverageLoan <WghtdAvrgLn>
Presence: [0..1]
Definition: Contains the weighted average loan of the fixed income instrument (expressed in months).
Datatype: "DecimalNumber" on page 3324
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1046 August 2026
```

