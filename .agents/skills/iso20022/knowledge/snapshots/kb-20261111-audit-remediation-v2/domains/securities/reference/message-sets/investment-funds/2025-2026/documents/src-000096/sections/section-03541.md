---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.29 ProcessingCharacteristics12", "66.1.26.29.15 SettlementCycle <SttlmCycl>", "66.1.26.29.15.2 RenunciationPlus <RPlus>"]
file_pages: [4791]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.29.15.2 RenunciationPlus <RPlus>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4791 to 4791.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4791

```text
66.1.26.29.15.2  RenunciationPlus <RPlus>
Presence: [1..1]
Definition: Number of days after the renunciation of title documents are received used to define the
standard settlement timeframe.
Datatype: "Number" on page 5400
66.1.26.29.16  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the redemption processing characteristics.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.30  DrawdownType2Choice
Definition: Choice of formats for a type of drawdown.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4791
Or}   Proprietary <Prtry> [1..1] ± 4791
66.1.26.30.1  Code <Cd>
Presence: [1..1]
Definition: Type of drawdown expressed as a code.
Datatype: "DrawdownType2Code" on page 5295
CodeName Name Definition
BOTH Both Drawdown type is both flexi-access and
capped.
CAPP CappedIncomeDrawdown Drawdown type is capped.
FLEX FlexibleAccessDrawdown Drawdown type is flexi-access.
66.1.26.30.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of drawdown expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4791 May 2026
```

