---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.33 ProcessingCharacteristics10", "66.1.26.33.15 SettlementCycle <SttlmCycl>", "66.1.26.33.15.2 RenunciationPlus <RPlus>"]
file_pages: [4807]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.33.15.2 RenunciationPlus <RPlus>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4807 to 4807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4807

```text
66.1.26.33.15.2  RenunciationPlus <RPlus>
Presence: [1..1]
Definition: Number of days after the renunciation of title documents are received used to define the
standard settlement timeframe.
Datatype: "Number" on page 5400
66.1.26.33.16  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the redemption processing characteristics.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.27 Market
66.1.27.1  OtherTargetMarketLossBearing1
Definition: Loss bearing target market.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AbilityToBearLossesType <AbltyToBearLossesTp> [0..1] Text 4807
   Target <Trgt> [0..1]  4807
{Or     Code <Cd> [1..1] CodeSet 4808
Or}     Proprietary <Prtry> [1..1] ± 4808
   AdditionalInformation <AddtlInf> [0..1] ± 4808
66.1.27.1.1  AbilityToBearLossesType <AbltyToBearLossesTp>
Presence: [0..1]
Definition: Type of loss bearing.
Datatype: "Max35Text" on page 5403
66.1.27.1.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of loss
bearing.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4807 May 2026
```

