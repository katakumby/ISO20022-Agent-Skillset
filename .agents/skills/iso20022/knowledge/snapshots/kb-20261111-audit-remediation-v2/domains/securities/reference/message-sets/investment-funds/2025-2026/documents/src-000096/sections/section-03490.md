---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.7 ProcessingCharacteristics9", "66.1.26.7.13 LimitedPeriod <LtdPrd>"]
file_pages: [4740]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.7.13 LimitedPeriod <LtdPrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4740 to 4740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4740

```text
Following Must be True
    /NonWorkingDayAdjustment Must be present
66.1.26.7.13  LimitedPeriod <LtdPrd>
Presence: [0..1]
Definition: Specific period, for example, for some guaranteed funds, during which the units/shares may
be switched.
Datatype: "Max350Text" on page 5403
66.1.26.7.14  SettlementCycle <SttlmCycl>
Presence: [0..1]
Definition: Settlement timing.
SettlementCycle <SttlmCycl> contains one of the following TimeFrame8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TradePlus <TPlus> [1..1] Quantity 4740
Or}   RenunciationPlus <RPlus> [1..1] Quantity 4740
66.1.26.7.14.1  TradePlus <TPlus>
Presence: [1..1]
Definition: Number of days after the trade date (T) for the standard settlement timeframe.
Datatype: "Number" on page 5400
66.1.26.7.14.2  RenunciationPlus <RPlus>
Presence: [1..1]
Definition: Number of days after the renunciation of title documents are received used to define the
standard settlement timeframe.
Datatype: "Number" on page 5400
66.1.26.7.15  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the switch processing characteristics.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.8  FundOrderType4Choice
Definition: Choice of formats for the order type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4740 May 2026
```

