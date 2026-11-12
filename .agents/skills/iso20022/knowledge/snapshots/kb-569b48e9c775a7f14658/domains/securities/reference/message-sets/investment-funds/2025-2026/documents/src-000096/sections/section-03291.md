---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.4 CashAsset2", "66.1.19.4.1 CashAssetType <CshAsstTp>", "66.1.19.4.1.2 Proprietary <Prtry>"]
file_pages: [4528]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.4.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4528 to 4528.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4528

```text
66.1.19.4.1.2  Proprietary <Prtry>
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
66.1.19.4.2  HoldingCurrency <HldgCcy>
Presence: [1..1]
Definition: Currency of the asset in the holding.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.19.4.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the cash asset.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.20 Financial Instrument Quantity
66.1.20.1  UnitsOrAmount1Choice
Definition: Choice between an amount or number of units.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4528 May 2026
```

