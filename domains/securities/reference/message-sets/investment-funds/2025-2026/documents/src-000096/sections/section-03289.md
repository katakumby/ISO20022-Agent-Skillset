---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.3 OtherAsset2", "66.1.19.3.1 OtherAssetType <OthrAsstTp>", "66.1.19.3.1.2 Proprietary <Prtry>"]
file_pages: [4526]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.3.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4526 to 4526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4526

```text
CodeName Name Definition
DIMA Discretionary Asset is a discretionary investment
manager account
EXIA ExternalAccount Asset is an external investment account.
MOVE MovableProperty Property that is not real estate. Also
known as 'movable chattels'.
PROP Property Property that is real estate.
TIPP TrusteeInvestmentPlan Asset is a trustee investment plan (TIP).
66.1.19.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Other asset type specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.19.3.2  Identification <Id>
Presence: [1..1]
Definition: Technical identification of the asset.
Datatype: "Max35Text" on page 5403
66.1.19.3.3  Name <Nm>
Presence: [0..1]
Definition: Name of the asset.
Datatype: "Max35Text" on page 5403
66.1.19.3.4  Description <Desc>
Presence: [0..1]
Definition: Description of the asset.
Datatype: "Max35Text" on page 5403
66.1.19.3.5  OtherIdentification <OthrId>
Presence: [0..5]
Definition: Additional identification of the asset.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4526 May 2026
```

