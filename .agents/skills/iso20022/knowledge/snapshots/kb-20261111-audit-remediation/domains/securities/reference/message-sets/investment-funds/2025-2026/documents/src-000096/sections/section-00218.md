---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.15 ProductCategoryGermany <PdctCtgyDE>"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.15 ProductCategoryGermany <PdctCtgyDE>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
Products Association (EUSIPA) code should be used as defined in the scope of European MiFID
Template (EMT) reference 00095.
Datatype: "Max140Text" on page 5402
15.4.5.8.15  ProductCategoryGermany <PdctCtgyDE>
Presence: [0..1]
Definition: Designation of the respective product category or nature for Germany.
If the financial instrument is distributed in the German market, then the German classification of
financial instruments code should be used. When used in reference to MiFID, this is in the scope of the
European MiFID Template (EMT) reference 00090.
Datatype: "Max140Text" on page 5402
15.4.5.8.16  NotionalOrUnitBased <NtnlOrUnitBased>
Presence: [0..1]
Definition: Specifies whether the financial instrument is unit based or notional (nominal). When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 00085.
NotionalOrUnitBased <NtnlOrUnitBased> contains one of the following
NotionalOrUnitBased1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 318
Or}   Proprietary <Prtry> [1..1] ± 318
15.4.5.8.16.1  Code <Cd>
Presence: [1..1]
Definition: Type of unit basis for a financial instrument expressed as a code.
Datatype: "NotionalOrUnitBased1Code" on page 5331
CodeName Name Definition
UNIT Unit Basis of a financial instrument is unit.
NOTI Notional Basis of a financial instrument is
notional.
15.4.5.8.16.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of unit basis for a financial instrument expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 318 May 2026
```

