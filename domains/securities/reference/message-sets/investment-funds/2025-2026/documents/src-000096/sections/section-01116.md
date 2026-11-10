---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.3 Pension <Pnsn>", "40.4.15.5.3.21 MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc>"]
file_pages: [1561]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.3.21 MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1561 to 1561.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1561

```text
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.3.21  MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc>
Presence: [0..1]
Definition: Money Purchase Annual Allowance (MPAA) details.
MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc> contains the following elements (see
"MoneyPurchaseAnnualAllowance1" on page 4754 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Triggered <Trggrd> [1..1] Indicator 4754
   TriggeredDate <TrggrdDt> [0..1] Date 4755
40.4.15.5.3.22  SafeguardBenefit <SfgrdBnft>
Presence: [0..1]
Definition: Indicates whether the pension policy, plan or scheme is covered by a safeguard benefit.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.3.23  NonSafeguardedGuaranteedBenefits <NonSfgrddGrntedBnfts>
Presence: [0..1]
Definition: Indicates whether the pension policy, plan or scheme has non-safeguarded guaranteed
benefits.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.3.24  LifetimeAllowanceProtection <LftmAllwncPrtcn>
Presence: [0..1]
Definition: Indicates whether the pension policy, plan or scheme has lifetime allowance protection.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.3.25  ClientLifetimeAllowanceProtection <ClntLftmAllwncPrtcn>
Presence: [0..1]
Definition: Indicates whether the client has any lifetime allowance protection.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1561 May 2026
```

