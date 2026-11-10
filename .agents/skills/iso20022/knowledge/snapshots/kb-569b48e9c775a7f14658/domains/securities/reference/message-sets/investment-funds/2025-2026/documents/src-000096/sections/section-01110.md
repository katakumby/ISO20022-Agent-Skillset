---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.3 Pension <Pnsn>", "40.4.15.5.3.1 Identification <Id>", "40.4.15.5.3.1.1 Identifier <Idr>"]
file_pages: [1555]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.3.1.1 Identifier <Idr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1555 to 1555.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1555

```text
Identification <Id> contains the following PensionPolicy1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identifier <Idr> [1..1] Text 1555
   SubIdentifier <SubIdr> [0..1] Text 1555
   AdditionalInformation <AddtlInf> [0..1] ± 1555
40.4.15.5.3.1.1  Identifier <Idr>
Presence: [1..1]
Definition: Reference number of the pension policy, plan or scheme.
Datatype: "Max35Text" on page 5403
40.4.15.5.3.1.2  SubIdentifier <SubIdr>
Presence: [0..1]
Definition: Sub-identification of the pension policy, plan or scheme, such as a member reference.
Datatype: "Max35Text" on page 5403
40.4.15.5.3.1.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the identification of the pension policy, plan or scheme.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
40.4.15.5.3.2  Type <Tp>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme.
Type <Tp> contains one of the following PensionSchemeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1555
Or}   Proprietary <Prtry> [1..1] ± 1556
40.4.15.5.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme expressed as a code.
Datatype: "PensionSchemeType3Code" on page 5340
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1555 May 2026
```

