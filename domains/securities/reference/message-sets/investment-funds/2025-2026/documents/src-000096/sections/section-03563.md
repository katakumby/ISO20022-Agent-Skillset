---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.5 OtherTargetMarketInvestor1", "66.1.27.5.2 Target <Trgt>", "66.1.27.5.2.1 Type <Tp>"]
file_pages: [4813]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.5.2.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4813 to 4813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4813

```text
Target <Trgt> contains one of the following TargetMarket3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 4813
Or   Other <Othr> [1..1] CodeSet 4813
Or}   Proprietary <Prtry> [1..1] ± 4813
66.1.27.5.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies how a financial product is in scope of the target market parameter.
Datatype: "InvestorType2Code" on page 5327
CodeName Name Definition
BOT3 BothProfessionalPerSeAndElectiveProfessional Investor is both professional per se and
elective professional.
EPRO ElectiveProfessional Investor is an elective professional.
PRF2 ProfessionalOrPerSe Investor is professional or professional
per se.
66.1.27.5.2.2  Other <Othr>
Presence: [1..1]
Definition: Specifies whether a financial product is in scope of the target market parameter.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
66.1.27.5.2.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies whether the product is aimed at the target expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.27.5.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4813 May 2026
```

