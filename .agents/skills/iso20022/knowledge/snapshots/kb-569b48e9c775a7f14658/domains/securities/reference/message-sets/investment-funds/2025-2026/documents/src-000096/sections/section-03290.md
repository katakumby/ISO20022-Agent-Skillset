---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.3 OtherAsset2", "66.1.19.3.6 AdditionalInformation <AddtlInf>"]
file_pages: [4527]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.3.6 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4527 to 4527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4527

```text
66.1.19.3.6  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the other asset.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.19.4  CashAsset2
Definition: Identification of a cash asset.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAssetType <CshAsstTp> [1..1]  4527
{Or     Code <Cd> [1..1] CodeSet 4527
Or}     Proprietary <Prtry> [1..1] ± 4528
   HoldingCurrency <HldgCcy> [1..1] CodeSet C1 4528
   AdditionalInformation <AddtlInf> [0..1] ± 4528
66.1.19.4.1  CashAssetType <CshAsstTp>
Presence: [1..1]
Definition: Type of cash asset.
CashAssetType <CshAsstTp> contains one of the following CashAssetType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4527
Or}   Proprietary <Prtry> [1..1] ± 4528
66.1.19.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of cash expressed as a code.
Datatype: "CashAssetType1Code" on page 5281
CodeName Name Definition
CSH2 CashInHolding Cash is cash in the holding not yet
invested.
CSH1 CashInvestment Cash is attributed to a cash investment.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4527 May 2026
```

