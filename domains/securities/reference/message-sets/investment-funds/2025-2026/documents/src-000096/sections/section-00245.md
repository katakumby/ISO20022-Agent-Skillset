---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.3 KnowledgeAndOrExperience <KnwldgAndOrExprnc>"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.3 KnowledgeAndOrExperience <KnwldgAndOrExprnc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
15.4.5.22.3  KnowledgeAndOrExperience <KnwldgAndOrExprnc>
Presence: [0..1]
Definition: Knowledge and/or experience of the investor.
KnowledgeAndOrExperience <KnwldgAndOrExprnc> contains the following InvestorKnowledge1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BasicInvestor <BsicInvstr> [0..1] CodeSet 349
   InformedInvestor <InfrmdInvstr> [0..1] CodeSet 349
   AdvancedInvestor <AdvncdInvstr> [0..1] CodeSet 350
   ExpertInvestorGermany <ExprtInvstrDE> [0..1] CodeSet 350
   Other <Othr> [0..*] ± 350
15.4.5.22.3.1  BasicInvestor <BsicInvstr>
Presence: [0..1]
Definition: Specifies whether the investor is a basic investor. A basic investor has one, or more, of the
following characteristics:
- a basic knowledge of relevant financial instruments (a basic investor can make an informed
investment decision based on the regulated and authorised offering documentation or with the help of
basic information provided at the point of sale),
- no financial industry experience, that is, suited to a first time investor.
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
02010.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.3.2  InformedInvestor <InfrmdInvstr>
Presence: [0..1]
Definition: Specifies whether the investor is an informed investor. An informed investor has one, or
more, of the following characteristics:
- average knowledge of relevant financial products (an informed investor can make an informed
investment decision based on the regulated and authorised offering documentation, together with
knowledge and understanding of the specific factors/risks highlighted within them only),
- some financial industry experience.
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
02020.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 349 May 2026
```

