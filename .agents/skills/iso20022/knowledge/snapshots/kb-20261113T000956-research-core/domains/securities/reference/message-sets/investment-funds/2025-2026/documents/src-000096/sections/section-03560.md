---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.3 TargetMarket5Choice"]
file_pages: [4810]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.3 TargetMarket5Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4810 to 4810.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4810

```text
66.1.27.3  TargetMarket5Choice
Definition: Choice of formats for the specification of how a financial product is in scope of a target
market parameter.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 4810
Or}   Other <Othr> [1..1] CodeSet 4810
66.1.27.3.1  Type <Tp>
Presence: [1..1]
Definition: Specifies how the financial product is in scope of the target market parameter.
Datatype: "InvestorType4Code" on page 5328
CodeName Name Definition
BOT3 BothProfessionalPerSeAndElectiveProfessional Investor is both professional per se and
elective professional.
NPRF NotProfessionalPerSeElectiveProfessional Investor is neither professional per se or
elective professional.
PRF3 ProfessionalPerSeNotElectiveProfessional Investor is professional per se but not
elective professional.
PRF4 ElectiveProfessionalNotProfessionalPerSe Investor is an elective professional but
not professional per se.
66.1.27.3.2  Other <Othr>
Presence: [1..1]
Definition: Specifies whether the financial product is in scope of the target market parameter.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
66.1.27.4  OtherTargetMarketRiskTolerance1
Definition: Risk tolerance target market.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4810 May 2026
```

