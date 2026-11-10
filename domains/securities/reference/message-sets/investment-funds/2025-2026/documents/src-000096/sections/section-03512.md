---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.15 ProcessingCharacteristics11", "66.1.26.15.15 SettlementCycle <SttlmCycl>", "66.1.26.15.15.2 Prepayment <Prepmt>"]
file_pages: [4762]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.15.15.2 Prepayment <Prepmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4762 to 4762.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4762

```text
66.1.26.15.15.2  Prepayment <Prepmt>
Presence: [1..1]
Definition: Indicates whether pre-payment is necessary.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.15.16  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the subscription processing characteristics.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.16  OtherInvestmentNeed1
Definition: Other investment need.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClientObjectivesAndNeedsType
<ClntObjctvsAndNeedsTp>
[0..1] Text 4762
   Target <Trgt> [0..1]  4762
{Or     Code <Cd> [1..1] CodeSet 4763
Or}     Proprietary <Prtry> [1..1] ± 4763
   AdditionalInformation <AddtlInf> [0..1] ± 4763
66.1.26.16.1  ClientObjectivesAndNeedsType <ClntObjctvsAndNeedsTp>
Presence: [0..1]
Definition: Type of return profile.
Datatype: "Max35Text" on page 5403
66.1.26.16.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of return
profile.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4762 May 2026
```

