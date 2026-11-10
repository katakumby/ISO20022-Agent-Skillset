---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.25 LumpSumType1Choice", "66.1.26.25.2 Proprietary <Prtry>"]
file_pages: [4781]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.25.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4781 to 4781.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4781

```text
Datatype: "LumpSumType1Code" on page 5329
CodeName Name Definition
DEAB DeathBenefit Lump sum is a death benefit lump sum.
PCLS PensionCommencement Lump sum is a pension commencement
lump sum.
UFPL Uncrystallised Lump sum is an uncrystallised fund
pension lump sum.
66.1.26.25.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of lump sum expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.26.26  DistributionStrategy1Choice
Definition: Choice of formats for the specification of a distribution strategy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.26.1  Code <Cd>
Presence: [1..1]
Definition: Distribution strategy expressed as a code.
Datatype: "InvestorType3Code" on page 5327
CodeName Name Definition
RETL Retail Investor is a retail investor.
PRF2 ProfessionalOrPerSe Investor is professional or professional
per se.
NEI1 NeitherProfessionalOrRetail Investor is neither professional or retail.
BOT2 BothProfessionalAndRetail Investor is both professional and retail.
66.1.26.26.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Distribution strategy expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4781 May 2026
```

