---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.6 OtherTargetMarketInvestorKnowledge1"]
file_pages: [4814]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.6 OtherTargetMarketInvestorKnowledge1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4814 to 4814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4814

```text
Definition: Additional information about the target market and the investor type.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.27.6  OtherTargetMarketInvestorKnowledge1
Definition: Investor knowledge and experience target market.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestorKnowledgeType <InvstrKnwldgTp> [0..1] Text 4814
   Target <Trgt> [0..1]  4814
{Or     Code <Cd> [1..1] CodeSet 4814
Or}     Proprietary <Prtry> [1..1] ± 4815
   AdditionalInformation <AddtlInf> [0..1] ± 4815
66.1.27.6.1  InvestorKnowledgeType <InvstrKnwldgTp>
Presence: [0..1]
Definition: Type of investor knowledge and experience.
Datatype: "Max35Text" on page 5403
66.1.27.6.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of
knowledge or experience of the investor.
Target <Trgt> contains one of the following TargetMarket1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4814
Or}   Proprietary <Prtry> [1..1] ± 4815
66.1.27.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies whether the product is aimed at the target expressed as a code.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4814 May 2026
```

