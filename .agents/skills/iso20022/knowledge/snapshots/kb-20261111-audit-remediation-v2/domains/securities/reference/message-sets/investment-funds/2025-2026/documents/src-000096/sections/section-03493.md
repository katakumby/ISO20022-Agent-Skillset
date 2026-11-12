---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.9 PensionOrder1", "66.1.26.9.2 AdditionalInformation <AddtlInf>"]
file_pages: [4743]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.9.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4743 to 4743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4743

```text
66.1.26.9.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the pension order.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.10  InvestmentNeed2Choice
Definition: Choice of formats for an investment need.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4743
Or}   Proprietary <Prtry> [1..1] ± 4743
66.1.26.10.1  Code <Cd>
Presence: [1..1]
Definition: Investment need expressed as a code.
Datatype: "InvestmentNeed2Code" on page 5326
CodeName Name Definition
NSPE None No specific need.
OTHR Other Other specific need.
ISLB IslamicBanking Investment need is for Islamic banking.
66.1.26.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investment need expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.26.11  ModificationScope41
Definition: Scope of the modification to be applied on an identified set of information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4743 May 2026
```

