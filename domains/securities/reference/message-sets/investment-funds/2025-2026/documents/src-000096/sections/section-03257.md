---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.2 TaxEfficientProduct4", "66.1.18.2.4 AdditionalInformation <AddtlInf>"]
file_pages: [4493]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.2.4 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4493 to 4493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4493

```text
Constraints
• SpecificPreviousYearsGuideline
SpecificPreviousYears must not contain the current year.
66.1.18.2.4  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the tax efficient product.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.18.3  FinancialInstrument9
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, eg, dividend option or valuation currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4493
   Name <Nm> [0..1] Text 4494
   SupplementaryIdentification <SplmtryId> [0..1] Text 4494
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 4494
   ClassType <ClssTp> [0..1] Text 4495
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4495
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4495
   DualFundIndicator <DualFndInd> [1..1] Indicator 4495
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
66.1.18.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4493 May 2026
```

