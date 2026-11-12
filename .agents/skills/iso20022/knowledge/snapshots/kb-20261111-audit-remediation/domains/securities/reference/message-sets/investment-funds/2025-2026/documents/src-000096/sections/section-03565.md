---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.27 Market", "66.1.27.6 OtherTargetMarketInvestorKnowledge1", "66.1.27.6.2 Target <Trgt>", "66.1.27.6.2.2 Proprietary <Prtry>"]
file_pages: [4815]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.27.6.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4815 to 4815.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4815

```text
CodeName Name Definition
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
66.1.27.6.2.2  Proprietary <Prtry>
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
66.1.27.6.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the target market and the investor knowledge and experience.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.28 Miscellaneous
66.1.28.1  MiFIDClassification1
Definition: Details about the MIFID classification of the account owner.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Classification <Clssfctn> [1..1] CodeSet 4815
   Narrative <Nrrtv> [0..1] Text 4816
66.1.28.1.1  Classification <Clssfctn>
Presence: [1..1]
Definition: MiFID classification of the account owner.
Datatype: "OrderOriginatorEligibility1Code" on page 5332
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4815 May 2026
```

