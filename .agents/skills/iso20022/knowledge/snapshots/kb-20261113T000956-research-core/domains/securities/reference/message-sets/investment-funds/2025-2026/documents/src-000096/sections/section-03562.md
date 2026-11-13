---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.4 OtherTargetMarketRiskTolerance1", "66.1.27.4.3 AdditionalInformation <AddtlInf>"]
file_pages: [4812]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.4.3 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4812 to 4812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4812

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.27.4.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the target market and the investor's risk tolerance.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.27.5  OtherTargetMarketInvestor1
Definition: Investor type target market.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestorType <InvstrTp> [0..1] Text 4812
   Target <Trgt> [0..1]  4812
{Or     Type <Tp> [1..1] CodeSet 4813
Or     Other <Othr> [1..1] CodeSet 4813
Or}     Proprietary <Prtry> [1..1] ± 4813
   AdditionalInformation <AddtlInf> [0..1] ± 4813
66.1.27.5.1  InvestorType <InvstrTp>
Presence: [0..1]
Definition: Type of investor.
Datatype: "Max35Text" on page 5403
66.1.27.5.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of investor.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4812 May 2026
```

