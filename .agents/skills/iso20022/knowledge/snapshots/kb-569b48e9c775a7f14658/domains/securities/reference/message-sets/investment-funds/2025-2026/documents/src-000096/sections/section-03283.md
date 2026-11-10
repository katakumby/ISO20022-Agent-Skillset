---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.1 CashAsset3", "66.1.19.1.1 CashAssetType <CshAsstTp>"]
file_pages: [4520]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.1.1 CashAssetType <CshAsstTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4520 to 4520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4520

```text
Constraints
• HoldingTransferCurrencyGuideline
When cash is transferred in a currency other than that of the cash, the currency should be specified
in TransferCurrency.
66.1.19.1.1  CashAssetType <CshAsstTp>
Presence: [1..1]
Definition: Type of cash asset.
CashAssetType <CshAsstTp> contains one of the following CashAssetType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4520
Or}   Proprietary <Prtry> [1..1] ± 4520
66.1.19.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of cash expressed as a code.
Datatype: "CashAssetType1Code" on page 5281
CodeName Name Definition
CSH2 CashInHolding Cash is cash in the holding not yet
invested.
CSH1 CashInvestment Cash is attributed to a cash investment.
66.1.19.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of cash expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.19.1.2  HoldingCurrency <HldgCcy>
Presence: [1..1]
Definition: Currency of the asset in the holding.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4520 May 2026
```

