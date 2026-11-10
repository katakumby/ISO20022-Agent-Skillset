---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.2 SecurityIdentification25Choice", "66.1.19.2.15 OtherProprietaryIdentification <OthrPrtryId>", "66.1.19.2.15.2 IdentificationSource <IdSrc>"]
file_pages: [4525]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.2.15.2 IdentificationSource <IdSrc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4525 to 4525.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4525

```text
66.1.19.2.15.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
66.1.19.3  OtherAsset2
Definition: Identification of an asset.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherAssetType <OthrAsstTp> [1..1]  4525
{Or     Code <Cd> [1..1] CodeSet 4525
Or}     Proprietary <Prtry> [1..1] ± 4526
   Identification <Id> [1..1] Text 4526
   Name <Nm> [0..1] Text 4526
   Description <Desc> [0..1] Text 4526
   OtherIdentification <OthrId> [0..5] Text 4526
   AdditionalInformation <AddtlInf> [0..*] ± 4527
66.1.19.3.1  OtherAssetType <OthrAsstTp>
Presence: [1..1]
Definition: Type of asset.
OtherAssetType <OthrAsstTp> contains one of the following OtherAsset2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4525
Or}   Proprietary <Prtry> [1..1] ± 4526
66.1.19.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Other asset type specified as a code.
Datatype: "OtherAsset2Code" on page 5334
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4525 May 2026
```

